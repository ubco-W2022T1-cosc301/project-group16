import pandas as pd
import numpy as np

def load(path):
    df = pd.read_csv(path)
    data_clean =(
        df.copy()
        .drop(['budget_source','negative_format'], axis=1)
        .query("budget >0")
        .dropna(axis = 0)
    
    )
    return(data_clean)