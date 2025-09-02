import pandas as pd
def load_excel(file):
    """Read Excel file and return dataframe"""
    try:
        df = pd.read_excel(file)
        return df
    except Exception as e:
        print("Error loading Excel:", e)
        return None