import pandas as pd
import matplotlib.pyplot as plt
def factorize(Column):
    replace_map = {"Bronze": 0, "Silver": 1, "Gold": 2, "Platinum": 3, "Diamond": 4, "Apex": 5}
    return Column.replace(replace_map)
def cross_tab(df, col_name, other_col_name):
    return pd.crosstab(df[col_name], df[other_col_name], normalize="index")
with open(r"D:\uni stuff\Data-Science-Project\CleanData.csv", "r") as file:
    df = pd.read_csv(file)
def get_means(df):
    return [df["WinRate"].mean(), df["Games"].mean(), df["Kills"].mean(), df["Deaths"].mean(), df["Assists"].mean(), df["CS"].mean(), df["MultiKills"].mean()]
# plot WinRate
bronze_df = df[df.Rank == "Bronze"]
bronze_plot = pd.DataFrame({"Data": ["WinRate", "Games", "Kills", "Deaths", "Assists", "CS", "MultiKills"], "Means": get_means(bronze_df)})
bronze_color_list = ["#CD7F32"]*7

silver_df = df[df.Rank == "Silver"]
silver_plot = pd.DataFrame({"Data": ["WinRate", "Games", "Kills", "Deaths", "Assists", "CS", "MultiKills"], "Means": get_means(silver_df)})
silver_color_list = ["#C0C0C0"]*7

gold_df = df[df.Rank == "Gold"]
gold_plot = pd.DataFrame({"Data": ["WinRate", "Games", "Kills", "Deaths", "Assists", "CS", "MultiKills"], "Means": get_means(gold_df)})
gold_color_list = ["#d4af37"]*7

platinum_df = df[df.Rank == "Platinum"]
platinum_plot = pd.DataFrame({"Data": ["WinRate", "Games", "Kills", "Deaths", "Assists", "CS", "MultiKills"], "Means": get_means(platinum_df)})
platinum_color_list = ["#E5E4E2"]*7

diamond_df = df[df.Rank == "Diamond"]
diamond_plot = pd.DataFrame({"Data": ["WinRate", "Games", "Kills", "Deaths", "Assists", "CS", "MultiKills"], "Means": get_means(diamond_df)})
diamond_color_list = ["#A0e1f5"]*7

apex_df = df[df.Rank == "Apex"]
apex_plot = pd.DataFrame({"Data": ["WinRate", "Games", "Kills", "Deaths", "Assists", "CS", "MultiKills"], "Means": get_means(apex_df)})
apex_color_list = ["#860111"]*7

plt.bar(x=bronze_plot["Data"], height=bronze_plot["Means"], color=bronze_color_list)
plt.title("Bronze")
plt.ylabel("Stats")
#plt.show()

plt.bar(x=silver_plot["Data"], height=bronze_plot["Means"], color=silver_color_list)
plt.title("Silver")
plt.ylabel("Stats")
#plt.show()

plt.bar(x=gold_plot["Data"], height=bronze_plot["Means"], color=gold_color_list)
plt.title("Gold")
plt.ylabel("Stats")
#plt.show()

plt.bar(x=platinum_plot["Data"], height=bronze_plot["Means"], color=platinum_color_list)
plt.title("Platinum")
plt.ylabel("Stats")
#plt.show()

plt.bar(x=diamond_plot["Data"], height=bronze_plot["Means"], color=diamond_color_list)
plt.title("Diamond")
plt.ylabel("Stats")
#plt.show()

plt.bar(x=apex_plot["Data"], height=bronze_plot["Means"], color=apex_color_list)
plt.title("Apex")
plt.ylabel("Stats")
#plt.show()
