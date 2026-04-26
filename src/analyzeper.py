import pandas as pd
 
def load_data(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath, parse_dates=['date'])
    df['total'] = df['quantity'] * df['unit_price']
    df['month'] = df['date'].dt.to_period('M')
    df.dropna(inplace=True)
    return df
