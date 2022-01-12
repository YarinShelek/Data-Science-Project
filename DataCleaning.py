import pandas as pd
import numpy as np
def outlier_detection_iqr(df):
    numeric_columns = df.select_dtypes(include=['number']).columns
    for col in df[numeric_columns]:
        Q1 = np.percentile(df[col], 25)
        Q3 = np.percentile(df[col], 75)
        IQR = Q3-Q1
        IQR_range = 1.5 * IQR
        df[col][(df[col] < Q1-IQR_range) | (df[col] > Q3 + IQR_range)] = np.nan
    return df

def get_df(df, rank):
    return df[df.Rank == rank]
with open("AllData.csv", "r") as file:
    df = pd.read_csv(file)

print("Original Size:", df.shape)
replace_map = {"Iron": "Bronze", "Challenger": "Apex", "Grandmaster": "Apex", "Master": "Apex"}
df["Rank"].replace(replace_map, inplace=True)
df.drop(df[df.Rank == "Unranked"].index, inplace=True)
df.drop_duplicates(inplace=True)
df.dropna(inplace=True) #get rid of the empty rows we made while crawling
df.drop("KDA", axis=1, inplace=True)
df.drop(df[df.Games <= 100].index & df[df.WinRate >= 75].index, inplace=True)
df.drop(df[df.WinRate <= 30].index, inplace=True)
df.drop(df[df.Games >= 1500].index, inplace=True)
print("Before or fat", df.shape)
df_gold = pd.DataFrame(get_df(df, "Gold"))
df_plat = pd.DataFrame(get_df(df, "Platinum"))
df.drop(df[df.Rank == "Gold"].index, inplace=True)
df.drop(df[df.Rank == "Platinum"].index, inplace=True)
df_gold = outlier_detection_iqr(df_gold)
df_plat = outlier_detection_iqr(df_plat)
df = df.append(df_gold)
df = df.append(df_plat)
print("After Cleaning Size:", df.dropna().shape)
with open("CleanData.csv", "w") as file2:
   df.dropna().to_csv(file2, index=False)