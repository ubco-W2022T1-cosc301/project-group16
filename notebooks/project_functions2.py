def load_and_process(csvpath):
    df1= pd.read_csv(csvpath)
    df1=(
        df1[~df1['genres'].str.contains('Animation')]
        .copy().drop(['title','directors','camera_format','negative_format','budget_source','genres'], axis=1)
        .dropna(axis=0)
        .query("film_type!=['U','F|U']")
        .query("budget>0")
    )
return(df1)