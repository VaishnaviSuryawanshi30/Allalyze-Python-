import speech_recognition as sr

def analyze_audio(path):
    r = sr.Recognizer()

    with sr.AudioFile(path) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio)
    except:
        text = "Could not recognize speech"

    return {
        "recognized_text": text
    }
