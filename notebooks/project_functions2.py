import pandas as pd
import numpy as np

def load_and_process(csvpath):
    df1= pd.read_csv(csvpath)
    df1=(
        .copy().drop(['title','directors','camera_format','negative_format','budget_source','genres'], axis=1)
        .dropna(axis=0)
        .query("film_type==['D','F']")
        .query("budget>0")
    )
    df1["film_type"]=df1["film_type"].str.replace('F',"Film")
    df1["film_type"]=df1["film_type"].str.replace('D',"Digital")
    return(df1)