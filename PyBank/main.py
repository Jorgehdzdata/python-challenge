# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



import pandas as pd
import numpy as np

df = pd.read_csv('Resources/budget_data.csv')

#print(df)

#df

TM = len(df.index)

print(f"Total Months:" + " " + str(TM), file=open("analysis/Financial_Analysis.txt", "a"))

#Total_Months

Total_amount = df["Profit/Losses"].sum()

print(f"Total:" + " $" + str(Total_amount), file=open("analysis/Financial_Analysis.txt", "a"))

dfd = df["Profit/Losses"].diff()

AC = dfd.mean()
AC = round(AC, 2)
print(f"Average Change:" + " $" + str(AC), file=open("analysis/Financial_Analysis.txt", "a"))

#df['Date'] = pd.to_datetime(df['Date'])  

df['Profit/Losses'].diff().idxmax()

GM = df["Date"].iloc[25]

GI = df['Profit/Losses'].diff().max()
print(f"Greatest Increase in Profits: " + GM + " (" + "$" + str(GI) + ")", file=open("analysis/Financial_Analysis.txt", "a"))

df['Profit/Losses'].diff().idxmin()

DM = df["Date"].iloc[44]

GD = df['Profit/Losses'].diff().min()
print(f"Greatest Decrease in Profits: " + DM + " (" + "$" + str(GD) + ")", file=open("analysis/Financial_Analysis.txt", "a"))

