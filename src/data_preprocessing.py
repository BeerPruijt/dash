import pandas as pd

def preprocess_data(df, column, preprocess_type):
    """Preprocesses the data based on the specified type."""
    df_copy = df.copy()
    
    if preprocess_type == 'mom':
        df_copy[column] = df_copy[column].pct_change() * 100
    elif preprocess_type == 'yoy':
        df_copy[column] = df_copy[column].pct_change(periods=12) * 100
    
    return df_copy.dropna(subset=[column])