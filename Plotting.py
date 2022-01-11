import pandas as pd
import matplotlib.pyplot as plt
import PlotUtility as util

df = util.read_csv()
DataFrames = { #hold dictionary of data frames we use to plot with later
              "Bronze": {"Plot_DF": util.get_plot_df(util.get_df(df, "Bronze"), type="Normal"), "Color_List": ["#CD7F32"]*7},
              "Silver": {"Plot_DF": util.get_plot_df(util.get_df(df, "Silver"), type="Normal"), "Color_List": ["#C0C0C0"]*7},
              "Gold": {"Plot_DF": util.get_plot_df(util.get_df(df, "Gold"), type="Normal"), "Color_List": ["#d4af37"]*7},
              "Platinum": {"Plot_DF": util.get_plot_df(util.get_df(df, "Platinum"), type="Normal"), "Color_List": ["#E5E4E2"]*7},
              "Diamond": {"Plot_DF": util.get_plot_df(util.get_df(df, "Diamond"), type="Normal"), "Color_List": ["#A0e1f5"]*7},
              "Apex": {"Plot_DF": util.get_plot_df(util.get_df(df, "Apex"), type="Normal"), "Color_List": ["#860111"]*7}
              }

DataFrames_Damage_Gold = {
    "Bronze": {"Plot_DF": util.get_plot_df(util.get_df(df, "Bronze")), "Color_List": ["#CD7F32"]*7},
    "Silver": {"Plot_DF": util.get_plot_df(util.get_df(df, "Silver")), "Color_List": ["#C0C0C0"]*7},
    "Gold": {"Plot_DF": util.get_plot_df(util.get_df(df, "Gold")), "Color_List": ["#d4af37"]*7},
    "Platinum": {"Plot_DF": util.get_plot_df(util.get_df(df, "Platinum")), "Color_List": ["#E5E4E2"]*7},
    "Diamond": {"Plot_DF": util.get_plot_df(util.get_df(df, "Diamond")), "Color_List": ["#A0e1f5"]*7},
    "Apex": {"Plot_DF": util.get_plot_df(util.get_df(df, "Apex")), "Color_List": ["#860111"]*7}
}
##BRONZE PLOT
#plt.bar(x=DataFrames["Bronze"]["Plot_DF"]["Data"], height=DataFrames["Bronze"]["Plot_DF"]["Means"], color=DataFrames["Bronze"]["Color_List"]) #MEANS
plt.bar(x=DataFrames_Damage_Gold["Bronze"]["Plot_DF"]["Data"], height=DataFrames_Damage_Gold["Bronze"]["Plot_DF"]["Means"], color=DataFrames_Damage_Gold["Bronze"]["Color_List"]) #DAMAGE GOLD
plt.title("Bronze")
plt.ylabel("Stats")
plt.show()
##BRONZE PLOT

##SILVER PLOT
#plt.bar(x=DataFrames["Silver"]["Plot_DF"]["Data"], height=DataFrames["Silver"]["Plot_DF"]["Means"], color=DataFrames["Silver"]["Color_List"]) #MEANS
plt.bar(x=DataFrames_Damage_Gold["Silver"]["Plot_DF"]["Data"], height=DataFrames_Damage_Gold["Silver"]["Plot_DF"]["Means"], color=DataFrames_Damage_Gold["Silver"]["Color_List"]) #DAMAGE GOLD
plt.title("Silver")
plt.ylabel("Stats")
plt.show()
##SILVER PLOT

##GOLD PLOT
#plt.bar(x=DataFrames["Gold"]["Plot_DF"]["Data"], height=DataFrames["Gold"]["Plot_DF"]["Means"], color=DataFrames["Gold"]["Color_List"]) #MEANS
plt.bar(x=DataFrames_Damage_Gold["Gold"]["Plot_DF"]["Data"], height=DataFrames_Damage_Gold["Gold"]["Plot_DF"]["Means"], color=DataFrames_Damage_Gold["Gold"]["Color_List"]) #DAMAGE GOLD
plt.title("Gold")
plt.ylabel("Stats")
plt.show()
##GOLD PLOT

#PLATINUM PLOT
#plt.bar(x=DataFrames["Platinum"]["Plot_DF"]["Data"], height=DataFrames["Platinum"]["Plot_DF"]["Means"], color=DataFrames["Platinum"]["Color_List"]) #MEANS
plt.bar(x=DataFrames_Damage_Gold["Platinum"]["Plot_DF"]["Data"], height=DataFrames_Damage_Gold["Platinum"]["Plot_DF"]["Means"], color=DataFrames_Damage_Gold["Platinum"]["Color_List"]) #DAMAGE GOLD
plt.title("Platinum")
plt.ylabel("Stats")
plt.show()
##PLATINUM PLOT

##DIAMOND PLOT
#plt.bar(x=DataFrames["Diamond"]["Plot_DF"]["Data"], height=DataFrames["Diamond"]["Plot_DF"]["Means"], color=DataFrames["Diamond"]["Color_List"]) #MEANS
plt.bar(x=DataFrames_Damage_Gold["Diamond"]["Plot_DF"]["Data"], height=DataFrames_Damage_Gold["Diamond"]["Plot_DF"]["Means"], color=DataFrames_Damage_Gold["Diamond"]["Color_List"]) #DAMAGE GOLD
plt.title("Diamond")
plt.ylabel("Stats")
plt.show()
##DIAMOND PLOT

##APEX PLOT
#plt.bar(x=DataFrames["Apex"]["Plot_DF"]["Data"], height=DataFrames["Apex"]["Plot_DF"]["Means"], color=DataFrames["Apex"]["Color_List"]) #MEANS
plt.bar(x=DataFrames_Damage_Gold["Apex"]["Plot_DF"]["Data"], height=DataFrames_Damage_Gold["Apex"]["Plot_DF"]["Means"], color=DataFrames_Damage_Gold["Apex"]["Color_List"]) #DAMAGE GOLD
plt.title("Apex")
plt.ylabel("Stats")
plt.show()
##APEX PLOT
