import pandas as pd
import numpy as np

def animation(genre):
    if 'Animation' in genre:
        return "yes"
    else:
        return "no"
def load_and_process(csvpath):
    df1= pd.read_csv(csvpath)
    df1["animated"]=df1.apply (lambda row: animation(row['genres']), axis=1)
    df1=(df1
        .copy().drop(['directors','camera_format','negative_format','budget_source', 'genres'], axis=1)
        .dropna(axis=0)
        .query("film_type==['D','F','D|F']")
        .query("budget>0")
    )
    return(df1)