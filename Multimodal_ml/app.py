import os
import sqlite3
from flask import Flask, render_template, request, jsonify

from analysis.pdf_analysis import analyze_pdf
from analysis.image_analysis import analyze_image
from analysis.video_analysis import analyze_video
from analysis.audio_analysis import analyze_audio
from analysis.csv_analysis import analyze_csv

from db import create_table, save_result
from db import fetch_all_results

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

create_table()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze/pdf", methods=["POST"])
def pdf():
    file = request.files["file"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    result = analyze_pdf(path)
    save_result(file.filename, "pdf", result)

    return jsonify(result)


@app.route("/analyze/image", methods=["POST"])
def image():
    file = request.files["file"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    result = analyze_image(path)
    save_result(file.filename, "image", result)

    return jsonify(result)


@app.route("/analyze/video", methods=["POST"])
def video():
    file = request.files["file"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    result = analyze_video(path)
    save_result(file.filename, "video", result)

    return jsonify(result)


@app.route("/analyze/audio", methods=["POST"])
def audio():
    file = request.files["file"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    result = analyze_audio(path)
    save_result(file.filename, "audio", result)

    return jsonify(result)


@app.route("/analyze/csv", methods=["POST"])
def csv():
    file = request.files["file"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    result = analyze_csv(path)
    save_result(file.filename, "csv", result)

    return render_template("csv_result.html", result=result)


@app.route("/history")
def history():
    data = fetch_all_results()
    return render_template("history.html", rows=data)

if __name__ == "__main__":
    app.run(debug=True)