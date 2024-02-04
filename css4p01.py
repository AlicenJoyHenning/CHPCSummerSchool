# -*- coding: utf-8 -*-
"""
HOMEWORK 

As a researcher, you are tasked to use ETL and EDA skills on a movie dataset to extract certain insights. 
Using pandas, analyse the "movie_dataset.csv "

Note, some column names have spaces (not ideal) and missing values (drop or fill to prevent bias). 
Load and clean the data, making reasonable assumptions. 
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from ydata_profiling import ProfileReport

# Read in the data set 
IMDB = pd.read_csv("C:/Users/alice/CHPC/project_01/movie_dataset.csv", index_col=0)

# Basic overviw 
profile = ProfileReport(IMDB, title = "Profiling")
profile.to_file("IMDB_report.html")

# Q1 : What is the highest rated movie in the dataset ? 
# Firstly, the data type of "Rating" is not integer : 
IMDB.info()
"""
OUTPUT : 
Rating              1000 non-null   float64
"""
# This can be fixed as follows : 
IMDB["Rating"] = IMDB["Rating"].astype(int)
# Now isolate the row (movie) that has the highest integer value in the "Rating" column 
print(IMDB[IMDB['Rating'] == IMDB["Rating"].max()]) # Associate the highest rating value with the associated movie
"""
OUTPUT : 
    Rank            Title  ... Revenue (Millions) Metascore
54    55  The Dark Knight  ...             533.32      82.0
"""


# Q2 : What is the average revenue of all movies in the dataset?
# Without considering 'NAs'
IMDB["Revenue (Millions)"].mean() # 82.95637614678898
# Only consider a subset of the movies where revenue was measured 
IMDB_rev = IMDB.dropna(subset = ["Revenue (Millions)"])
IMDB_rev["Revenue (Millions)"].mean() # 82.95637614678898 (the same )


# Q3 : What is the average revenue of movies from 2015 to 2017 in the dataset?
IMDB_2015_to_2017 = IMDB[(IMDB['Year'] >= 2015) & (IMDB['Year'] <= 2017)]
print(IMDB_2015_to_2017['Revenue (Millions)'].mean())
""" 
OUTPUT : 
63.099905660377345
"""

# Q4 : How many movies were released in 2016?
len(IMDB[IMDB['Year'] == 2016])
# OUTPUT : 297


# Q5 : How many movies were directed by Christopher Nolan 
len(IMDB[IMDB['Director'] == "Christopher Nolan"])  
# OUTPUT : 5 


# Q6 : How many movies in the dataset have a ranking of at least 8.0?
len(IMDB[IMDB['Rating'] >= 8])
# 78 rows 


# Q7 : What is the median rating of movies directed by Christopher Nolan 
subset_Nolan = IMDB[IMDB['Director'] == "Christopher Nolan"]
print(subset_Nolan['Rating'].median())
# OUTPUT : 8.6

# Q8 : Find the year with the highest average rating 
IMDB_year_group = IMDB.groupby("Year")
IMDB_year_group_mean = IMDB_year_group["Rating"].mean()
"""
OUTPUT : 
Year
2006    7.125000
2007    7.133962   HIGHEST 
2008    6.784615
2009    6.960784
2010    6.826667
2011    6.838095
2012    6.925000
2013    6.812088
2014    6.837755
2015    6.602362
2016    6.436700
Name: Rating, dtype: float64
    
"""

# Q9 : What is the percentage increase in number of movies made between 2006 and 2009? 
movies_2006 = IMDB[IMDB['Year'] == 2006] # 44 movies 
movies_2016 = IMDB[IMDB['Year'] == 2016] # 297 movies 
per_increase = ((len(movies_2016) - len(movies_2006))/len(movies_2006)) * 100
# OUTPUT : 575 


# Q10 : Find the most common actor in all the movies 
# SHORT CUT TO FIND ANSWER 
len(IMDB[IMDB['Actors'].str.contains('Mark Wahlberg')]) # OUTPUT = 15
len(IMDB[IMDB['Actors'].str.contains('Chris Pratt')]) # OUTPUT = 7
len(IMDB[IMDB['Actors'].str.contains('Matthew McConaughey')]) # OUTPUT = 10
len(IMDB[IMDB['Actors'].str.contains('Bradley Cooper')]) # OUTPUT = 11


# AUTOMATE PROCESS IF IT WASN'T MCQ
# Split the actors into create separate rows 
split_actors = IMDB['Actors'].str.split(', ').explode()
# Df for frequency of each actor
actor_counts = split_actors.value_counts()


# Q11 : How many unique genres are there in the dataset

split_genera = IMDB['Genre'].str.split(',').explode()
genera = split_genera.nunique() # OUTPUT = 20
# genera = split_genera.value_counts() (nice to see what the genre are)

# Q12 : Do a correlation of the numerical features, what insights can you deduce? Mention at least 5 insights. What advice can you give directors to produce better movies

# Rename for better plotting (purely aesthetic)
IMDB = IMDB.rename(columns = {'Runtime (Minutes)' : 'Runtime'})
IMDB = IMDB.rename(columns = {'Revenue (Millions)' : 'Revenue'})

# Adding a column to see if the number of genera is related to anything 
IMDB['Genres'] = IMDB['Genre'].str.count(',') + 1

# Create a figure and axes for subplots (combining plots in 1)
fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Pearson correlation test (continuous data)
pearson = sns.heatmap(IMDB.corr(), vmin=-1, vmax=1, annot=True, cmap="PiYG", ax=axs[0])
pearson.set_title('Pearson Correlation', fontsize=16, fontweight='bold', pad=20)  # Increase font size, make bold, and adjust position
pearson.set_xticklabels(pearson.get_xticklabels(), rotation=0)  # Set x-axis label rotation to 0 degrees

# Spearman correlation test (other)
correlation_matrix = IMDB.corr(method='spearman')
spearman = sns.heatmap(correlation_matrix, vmin=-1, vmax=1, annot=True, cmap="PiYG", ax=axs[1])
spearman.set_title('Spearman Correlation', fontsize=16, fontweight='bold', pad=20)  # Increase font size, make bold, and adjust position
spearman.set_xticklabels(spearman.get_xticklabels(), rotation=0)  # Set x-axis label rotation to 0 degrees

# Plots
plt.tight_layout()
plt.show()



