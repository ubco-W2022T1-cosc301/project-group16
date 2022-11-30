# Imports
import pandas as pd
import seaborn as sns
import numpy as np

# Seaborn Theme
sns.set_theme(style="ticks", font_scale=1.3)
sns.set_context("paper")
import matplotlib.pyplot as plt
plt.rc("axes.spines", top=False, right=False)

# Function to Load and Process Data Frame
def load_and_process(url_or_path_to_csv_file):
    # Method Chain 1 (Load data and deal with missing data)
    df1 = (
        pd.read_csv(url_or_path_to_csv_file)
        .rename(columns={"production_year": "year"})
        .merge(pd.read_csv("../data/raw/top_movies.csv"), on=['id'], how="left", suffixes=('', '_y'))
        .loc[:, ["director", "negative_format", "year", "budget", "genres", "film_type"]]
    )
    
    # Method Chain 2 (Create new columns, drop others, and do processing)
    df2 = (
        df1
        .dropna()
        .reset_index(drop=True)
        .assign(negative_format=df1.negative_format.str.split("|")).explode('negative_format')
        .assign(film_type=df1.film_type.str.split("|")).explode('film_type')
        .assign(genres=df1.genres.str.split("|")).explode('genres')
        .reset_index(drop=True)
        .sort_values("year", ascending=False)
    )
    
    # Make sure to return the latest dataframe
    return df2 

# Method Chain for Popular Formats
def get_popular_formats(df_clean):
    # Grab Initial Counts
    i = (
        df_clean
        .groupby('negative_format')
        .size()
        .reset_index(name='count')
    )
    # Filter out Data to prevent overplotting
    i = i[i['count']>80]
    # Sort and Return
    i = (
        i
        .sort_values(by=['count'], ascending=False)
        .reset_index(drop=True)
    )
    return i