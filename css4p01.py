#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 22:44:20 2024

@author: josedam
"""

import pandas as pd
df = pd.read_csv("movie_dataset.csv")
print(df.info())


print(df.columns)

avg_cal = df["Revenue (Millions)"].mean()

avg_cal2 = df["Metascore"].mean()


df["Revenue (Millions)"].fillna(avg_cal, inplace = True)

df["Metascore"].fillna(avg_cal2, inplace = True)
print(df.info())


#df = df[df["Year"] == "2017"]

#df = df[df['Year']>2015




#Qu 1- The highest rated movie is obtained by filtering all ratings greater than 8.9

# """ df = df[df['Rating']>8.9]
# print(df)"""

# #Qu 2- What is the average revenue of all movies in tha data set

# """ avg_rev = df["Revenue (Millions)"].mean()
# print(avg_rev) """

#Qu 3- The average revenue of movies  from 2015 to 2017



# Numerical analysis of specific colums
print(df.describe())
print(df.columns)


# Calculate the mean of a Rating column
mean_column_value = df['Rating'].mean()
print("Mean of 'Rating':", mean_column_value)

# Calculate the median of Rating column
median_column_value = df['Rating'].median()
print("Median of 'Rating':", median_column_value)

# Calculate the mode of Rating column
mode_column_value = df['Rating'].mode()
print("Mode of 'Rating':", mode_column_value)


# Calculate the mean of Vote column
mean_column_value = df['Votes'].mean()
print("Mean of 'Votes':", mean_column_value)

# Calculate the median of Vote column
median_column_value = df['Votes'].median()
print("Median of 'Votes':", median_column_value)

# Calculate the mode of Votes column
mode_column_value = df['Votes'].mode()
print("Mode of 'Votes':", mode_column_value)


# Calculate the mean of Revenue column
mean_column_value = df['Revenue (Millions)'].mean()
print("Mean of 'Revenue (Millions)':", mean_column_value)

# Calculate the median of  Revenue column
median_column_value = df['Revenue (Millions)'].median()
print("Median of 'Revenue (Millions):", median_column_value)

# Calculate the mode of Revenue column
mode_column_value = df['Revenue (Millions)'].mode()
print("Mode of 'Revenue (Millions)':", mode_column_value)


# Calculate the mean of Metascore column
mean_column_value = df['Metascore'].mean()
print("Mean of 'Metascore':", mean_column_value)

# Calculate the median of Metascore column
median_column_value = df['Metascore'].median()
print("Median of 'Metascore:", median_column_value)

# Calculate the mode of Metascore column
mode_column_value = df['Metascore'].mode()
print("Mode of 'Metascore':", mode_column_value)






