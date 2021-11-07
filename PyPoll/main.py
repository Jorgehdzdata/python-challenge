# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 22:08:55 2021

@author: georg
"""

import pandas as pd

df = pd.read_csv("Resources/election_data.csv")

df.head()

df_total = len(df["Voter ID"])

print("Total Votes:" + " " + str(df))

df

df_grouped = df.groupby("Candidate")

dfd= df_grouped["Candidate"].tolist()

df_grouped

Candidate_list

