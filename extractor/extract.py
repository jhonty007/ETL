import pandas as pd
from config.config import CSV_FILE_PATH

def extract():
    return pd.read_csv(CSV_FILE_PATH)