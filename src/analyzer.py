import pandas as pd
import numpy as np
 
def get_summary(df: pd.DataFrame) -> dict:
    return {
        'total_revenue': df['total'].sum(),
        'avg_ticket': df['total'].mean(),
        'total_orders': len(df),
        'top_product': df.groupby('product')['total'].sum().idxmax(),
        'best_region': df.groupby('region')['total'].sum().idxmax()
    }
 
def monthly_revenue(df: pd.DataFrame) -> pd.Series:
    return df.groupby('month')['total'].sum()
 
def revenue_by_category(df: pd.DataFrame) -> pd.Series:
    return df.groupby('category')['total'].sum()
