import pandas as pd
from sklearn import linear_model
from sklearn import metrics
from sklearn.metrics import make_scorer
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
import numpy as np
from Consts import Consts

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
