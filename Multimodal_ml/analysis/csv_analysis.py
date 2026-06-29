import pandas as pd

def analyze_csv(path: str):
    # Read only metadata-friendly sample to infer schema fast
    df = pd.read_csv(path, nrows=1000)

    # Pandas dtype → SQLite dtype mapping
    def map_dtype(dtype):
        if pd.api.types.is_integer_dtype(dtype):
            return "INTEGER"
        elif pd.api.types.is_float_dtype(dtype):
            return "FLOAT"
        elif pd.api.types.is_bool_dtype(dtype):
            return "BOOLEAN"
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            return "TIMESTAMP"
        else:
            return "TEXT"

    column_types = {
        col: map_dtype(dtype)
        for col, dtype in df.dtypes.items()
    }

    return {
        "rows": int(pd.read_csv(path, usecols=[0]).shape[0]),  # fast row count
        "columns": int(df.shape[1]),
        "column_names": list(df.columns),
        "column_types": column_types
    }
