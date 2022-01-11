import pandas as pd
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
print("After Cleaning Size:", df.shape)
with open("CleanData.csv", "w") as file2:
    df.to_csv(file2, index=False)