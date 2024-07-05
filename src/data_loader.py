import pandas as pd

def load_data(file_path):
    """Loads data from the specified file path."""
    return pd.read_excel(file_path, index_col=0, parse_dates=True)
