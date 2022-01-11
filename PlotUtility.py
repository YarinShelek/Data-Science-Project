from Consts import Consts
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import pandas as pd
def read_csv():
    with open(Consts.Clean_Data_File, "r") as DataFile:
        return pd.read_csv(DataFile)

def get_means(df):
    return [df["WinRate"].mean(), df["Games"].mean(), df["Kills"].mean(), df["Deaths"].mean(), df["Assists"].mean(), df["CS"].mean(), df["MultiKills"].mean()]

def get_gold_damage_means(df):
    return [df["Damage"].mean(), df["Gold"].mean()]

def get_df(df, rank):
    return df[df.Rank == rank]

def get_plot_df(df, type=""):
    if type == "Normal":
        return pd.DataFrame({"Data": ["WinRate", "Games", "Kills", "Deaths", "Assists", "CS", "MultiKills"], "Means": get_means(df)})
    else:
        return pd.DataFrame({"Data": ["Damage", "Gold"], "Means": get_gold_damage_means(df)})
def get_highly_correlated_cols(df):
    correlations, tuple_arr = [], []
    cols = df.columns
    for i, col1 in enumerate(cols):
        for j, col2 in enumerate(cols):
            if i == j:
                continue
            else:
                corr, _ = pearsonr(df[col1], df[col2])
                if corr >= 0.5 and (i, j) not in tuple_arr and i < j:
                    correlations.append(corr)
                    tuple_arr.append((i, j))
    return correlations, tuple_arr
def plot_high_correlated_scatters(df):
    correlations, tuples = get_highly_correlated_cols(df)
    corr_len = len(correlations)
    fig, axes = plt.subplots(1, corr_len)
    for c in range(corr_len):
        i, j = tuples[c]
        x = df.columns[i]
        y = df.columns[j]
        title = ("corr('%s','%s')=%4.2f") %(x, y, correlations[c])
        df.plot(kind="scatter",x=x,y=y,ax=axes[c],title=title)
    plt.show()
