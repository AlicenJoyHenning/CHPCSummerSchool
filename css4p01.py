# -*- coding: utf-8 -*-
"""
HOMEWORK 

As a researcher, you ar etasked to use ETL and EDA skills on a movie dataset to extract certain insights. 
Using pandas, analyse the "movie_dataset.csv "

Note, some column names have spaces (not ideal) and missing values (drop or fill to prevent bias). 
Load and clean the data, making reasonable assumptions. 

"""

import pandas as pd

IMDB = pd.read_csv("movie_dataset.csv")
print(IMDB.describe())

"""
              Rank         Year  ...  Revenue (Millions)   Metascore
count  1000.000000  1000.000000  ...          872.000000  936.000000
mean    500.500000  2012.783000  ...           82.956376   58.985043
std     288.819436     3.205962  ...          103.253540   17.194757
min       1.000000  2006.000000  ...            0.000000   11.000000
25%     250.750000  2010.000000  ...           13.270000   47.000000
50%     500.500000  2014.000000  ...           47.985000   59.500000
75%     750.250000  2016.000000  ...          113.715000   72.000000
max    1000.000000  2016.000000  ...          936.630000  100.000000

[8 rows x 7 columns]

"""

# Q1 : highest rated movie in the dataset 
# isolate column in df with rating and find max 
IMDB.info()
IMDB["Rating"] = IMDB["Rating"].astype(int)
print(IMDB['Rating'.max()]) # float64
print(IMDB[IMDB['Rating'] == 9])
"""
    Rank            Title  ... Revenue (Millions) Metascore
54    55  The Dark Knight  ...             533.32      82.0
"""


# Q2 : What is the average revenue of all movies in the dataset?
# From info : Revenue (Millions) mean = 82.95


# Q3 : What is the average revenue of movies from 2015 to 2017 in the dataset?
subset_IMDB = IMDB[ (IMDB['Year'] >= 2015) & (IMDB['Year'] < 2017) ]
print(subset_IMDB['Revenue (Millions)'].mean())
""" 
63.099905660377345
"""

# Q4 : How many movies were released in 2016?
subset_2016 = IMDB[IMDB['Year'] == 2016]
# size is 297


# Q5 : How many movies were directed by Christopher Nolan 
subset_Nolan = IMDB[IMDB['Director'] == "Christopher Nolan"]  
# size is 5 

# Q6 : How many movies in the dataset have a ranking of at least 8.0?
print(IMDB[IMDB['Rating'] >= 8])
subset_8 = IMDB[IMDB['Rating'] >= 8 ]
# 78 rows 

# Q7 : What is the median rating of movies directed by Christopher Nolan 
print(subset_Nolan['Rating'].median())
# 8.6

# Q8 : Find the year with the highest average rating 
# 1 : find the average rating of each year 
avg2006 = IMDB[IMDB['Year'] == 2006] 
avg = avg2006.describe() # 7.125 

avg2007 = IMDB[IMDB['Year'] == 2007] 
avg = avg2007.describe() # 7.133962264150944

avg2008 = IMDB[IMDB['Year'] == 2008] 
avg = avg2008.describe()	# 6.784615384615384

avg2009 = IMDB[IMDB['Year'] == 2009] 
avg = avg2009.describe() # 6.96078431372549

avg2010 = IMDB[IMDB['Year'] == 2010] 
avg = avg2010.describe() # 	6.826666666666666

avg2011 = IMDB[IMDB['Year'] == 2011] 
avg = avg2011.describe() # 6.8381

avg2012 = IMDB[IMDB['Year'] == 2012] 
avg = avg2012.describe() # 6.925

avg2013 = IMDB[IMDB['Year'] == 2013] 
avg = avg2013.describe() # 6.81209

avg2014 = IMDB[IMDB['Year'] == 2014] 
avg = avg2014.describe() # 6.8378

avg2015 = IMDB[IMDB['Year'] == 2015] 
avg = avg2015.describe() # 6.602

avg2016 = IMDB[IMDB['Year'] == 2016] 
avg = avg2016.describe() # 6.43

# Q9 : What is the percentage increase in number of movies made between 2006 and 2009? 
movies_2006 = IMDB[IMDB['Year'] == 2006] # 44 movies 
movies_2016 = IMDB[IMDB['Year'] == 2016] # 297 movies 
per_increase = ((297 - 44 )/ 44) * 100  # 575 


# Q10 : Find the most common actor in all the movies 
# NB the actors column has multiple names, you must find a way to search 


# Q11 : How many unique genres are there in the dataset


# Q12 : Do a correlation of the numerical features, what insights can you deduce? Mention at least 5 insights. What advice can you give directors to produce better movies


# Q13 : Create a github repository and upload a single python file called 'css4p01.py'. Share the url 
# The code must show all the steps used to load, analyse, and clean the data, as well as how you answered the Quiz questions. 
