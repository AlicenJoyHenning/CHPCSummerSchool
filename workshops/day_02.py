# -*- coding: utf-8 -*-
"""
PYTHON : Extract, Transform, and Load 
"""

""" SECTION 1 : REVIEW """
# File directories 
# (look on RHS) But making a project in spyder is different only because it is connected to Sypder 

import pandas as pd # first thing we do (we can call it whatever we want, 'pd' is shorter so its helpful)

# Load data with absolute path to the file 
country_data = pd.read_csv("C:/Users/alice/CHPC\\day_02\\data_02\\country_data_index.csv")

# Relative path : from where we are, not in full "look relative to where i am"
country_data = pd.read_csv("day_02\\data_02\\country_data_index.csv")
#### NOTE (cool): easy way click on file & you can get absolute or relative path 

# Read in df with no header info
column_names =  ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'] # list 
iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)
# Same as before reading from a different location online 
url = "https://raw.githubusercontent.com/kode2go/nithecs/main/lecture_01/iris.csv"
file = pd.read_csv(url, header=None, names= column_names)

# Read in text files with semi colon separator 
geospatial_data = pd.read_csv("day_02/data_02/Geospatial Data.txt",sep=";")

# Read in excel spreadsheet 
resident_doctors = pd.read_excel("day_02/data_02/residentdoctors.xlsx")

file = pd.read_json("day_02/data_02/student_data.json")
# categorical filtering would be helpful

# webscraping : beautiful soup 


url = "https://raw.githubusercontent.com/Asabele240701/css4_day02/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"
df = pd.read_csv(url)
# NOTE COOL : ctrl 1 to comment out! 

df = pd.read_csv("day_02/data_02/Accelerometer_data.csv", names = ["date_time", "x", "y", "z"])



""" SECTION 2 : TRANSFORM """

# Parameters of the readcsv function 
# https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-read-csv-table

# Index column 
country_data = pd.read_csv("day_02/data_02/country_data_index.csv", index_col=0)
# Skip rows
insurance = pd.read_csv("day_01/insurance_data.csv", skiprows = 5)
# Column headings 
column_names = ["duration", "pulse", "max_pulse", "calories"]
patient_data = pd.read_csv("day_02\\data_02\\patient_data.csv",header = None,names = column_names)
# Unique delimiter 
df = pd.read_csv("day_02\\data_02\\Geospatial Data.txt", sep=";")

""" Inconsistent data types & names """
# .extract() and .astype() methods that can be applies to a pandas series object 

df = pd.read_excel("day_02\\data_02\\residentdoctors.xlsx")
""" 
Problems : 
1. snake case vs lower case 
2. age groups '30-34yrs'
3. mixing text with numbers 

Change way info is stored into two cols, lower & upper 30-34 yrs > 30 , 34 
1 Extract the lower end of the age range 
df['LOWER_AGE'] = df['AGEDIST'].str.extract('(\d+)-')
2 Convert the new column to float 
df['LOWER_AGE'] = df['LOWER_AGE'].astype(int)

"""

df.info()
"""
RangeIndex: 161 entries, 0 to 160
Data columns (total 10 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   AGE                  161 non-null    int64  
 1   ghqscore_sum         161 non-null    float64
 2   jobsatisfaction_sum  161 non-null    float64
 3   workload_sum         161 non-null    float64
 4   AGEDIST              161 non-null    object 
 5   MARITALSTATUS        161 non-null    object # defines entire column as text because of 1 'other'
 6   CHILDREN             158 non-null    float64
 7   female               161 non-null    int64  
 8   HOURSWORKED          161 non-null    float64
 9   LOWER_AGE            161 non-null    int32  
dtypes: float64(5), int32(1), int64(2), object(2)
memory usage: 12.1+ KB
"""
# Just copies the column 
# df['LOWER_AGE'] = df["AGEDIST"]

# Extract the lowest using regular expressions
# (\d+)- first digit
df['LOWER_AGE'] = df["AGEDIST"].str.extract('(\d+)-')
# above applies the string operation (.str) AND other operations 

print(df.info())
df['LOWER_AGE'] = df["LOWER_AGE"].astype(int)
# now the column entries are numerical 

# same for upper age 
df['UPPER_AGE'] = df["AGEDIST"].str.extract('-(\d+)')
df['UPPER_AGE'] = df["UPPER_AGE"].astype(int)

 
"""
BUT
lower_age is still an object! because we extracted it as a string 

RangeIndex: 161 entries, 0 to 160
Data columns (total 10 columns):
 #   Column               Non-Null Count  Dtype  
---  ------               --------------  -----  
 0   AGE                  161 non-null    int64  
 1   ghqscore_sum         161 non-null    float64
 2   jobsatisfaction_sum  161 non-null    float64
 3   workload_sum         161 non-null    float64
 4   AGEDIST              161 non-null    object 
 5   MARITALSTATUS        161 non-null    object 
 6   CHILDREN             158 non-null    float64
 7   female               161 non-null    int64  
 8   HOURSWORKED          161 non-null    float64
 9   LOWER_AGE            161 non-null    object 
dtypes: float64(5), int64(2), object(3)
memory usage: 12.7+ KB
None
"""


"""
Day 2 : ETL continued

CLEANING OUT DATA   

Working with dates 
General problem with dates in Excel is that formatting can be completely different 
& ideally you want to work with a date format that is consistent and clear

Most cases dates are read in as a string, even if digits with dashes 

30-01-2024 ~ british standard 
01-30-2024 ~ american assholes 

methods allows filtering of data
.str
.extract
.astype
.dt (operation)

"""

""" SECTION 1 """

import pandas as pd

df = pd.read_csv("day_02/data_02/time_series_data.csv", index_col=0)

# convert date column to date time format using pandas built in features, specifies format coming in 
df['Date'] = pd.to_datetime(df['Date'])
print(df.info)

# this is helpful because it allows more powerful features to be used with the date/time format 
df['Year'] = df['Date'].dt.year # extract year to put in new column 
df['Month'] = df['Date'].dt.month # extract month to put in new column 
df['Day'] = df['Date'].dt.day # extracts the day to put in new column 


""" SECTION 2 """
df = pd.read_csv("day_02/data_02/patient_data_dates.csv", index_col=0, )

# If not adjusted since we already have column for index we can drop the automatically generated one as it is redundant 
# df.drop(["Index"], inplace=True, axis=1)

"""
Problems 
0. redundant index column 
1. na value in date and calories columns 
2. date format 
"""
# convert to date 
df["Date"] = pd.to_datetime(df["Date"], format="mixed")
# ignore problem row in date

# still wrong : 
df.drop(index=26, inplace=True)
df.drop(index=22, inplace=True)

df["Date"] = pd.to_datetime(df["Date"])

# FILLNA : replacing empty values
# Either get the average of a column and fill the empty values 

avg_cal = df["Calories"].mean()
df["Calories"].fillna(avg_cal, inplace = True) # inplace = True 

""" EDITING DATA """

pd.set_option('display.max_rows', None)

# 1 Removing empty cells 
df.dropna(inplace = True)

# ALSO need to redo the index after removing rows 
df = df.reset_index(drop = True)


# 2 Removing duplicates DROP_DUPLICATES()
# df.drop(7, inplace = True) # possible for smaller datasets, not so much larger ones 
df.drop_duplicates(inplace = True)
df = df.reset_index(drop = True)

# 3 Outlier likely typo, changes specific value 
df.loc[7, "Duration"] = 45
 # OR explicitly for one @ a time 
# df["Duration"] = df["Duration"].replace([450], [45])
 
print(df)
# to show all columns 
# pd.set_option('display.max_rows', None)

"""
ETL : Applying data transformations 

Using pandas to do things like merging files (append and merge) 

"""

""" SECTION 1 """

import pandas as pd 

df = pd.read_csv("day_02/data_02/iris.csv")

# How to extract headers from a dataframe (so you don'ts have to open and look at it)
col_names = df.columns
col_names = df.columns.tolist()
print(col_names)

"""
['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
"""

# Create another column with square value of a current column 
df["sepal_length_sq"] = df["sepal_length"]**2
# more complex methods this will be easier / custom function to each entry of a column 
df["sepal_length_sq"] = df["sepal_length"].apply(lambda x: x**2)

# Grouping by categories 
grouped = df.groupby("class")
# to calculate mean based on groups 
mean_sq = grouped["sepal_length_sq"].mean()

"""
OUTPUT : works out mean on groups in a column 

class
Iris-setosa        25.1818
Iris-versicolor    35.4972
Iris-virginica     43.7980
Name: sepal_length_sq, dtype: float64

"""

# Working with multiple files 

df1 = pd.read_csv("day_02/data_02/person_split1.csv")
df2 = pd.read_csv("day_02/data_02/person_split2.csv")

# add them, make a list with one df after the other in one 
df = pd.concat([df1, df2], ignore_index=True)

# files with different column names (relationship btw df )

df_1 = pd.read_csv("day_02/data_02/person_education.csv")
df_2 = pd.read_csv("day_02/data_02/person_work.csv")

# inner join to merge together the above, here is an inner join, 
df_merge_inner = pd.merge(df_1, df_2, on="id") # specifies the relationship is the "id" column

# different parameters of merge (default is inner)

# outer join : if no match 'nas' everywhere else   
df_merge_outer = pd.merge(df_1, df_2, )



""" SECTION 2 """

df = pd.read_csv("day_02/data_02/country_data_index.csv")

# Filtering data 
# example based on 'age' column 
print(df[df['Age'] > 30])

"""
OUTPUT: 
    
   Unnamed: 0  Age Gender       Country
0           0   39      M  South Africa
3           3   46      M  South Africa
5           5   35      F    Mozambique
7           7   49      M         Kenya
9           9   40      F         Egypt

"""

# using the iris dataset 
df = pd.read_csv("day_02/data_02/iris.csv")

# CLEANING Here the class column can be adjusted, they all have 'Iris_' 
# df['class'] = df['class'].str.extract('-(\.)')
df["class"] = df["class"].str.replace("Iris-", "")

# Now for FILTERING 
# Give rows where sepal length > 5 
df = df[df["sepal_length"] > 5]

# only see data for virginica 
df = df[df["class"] == "virginica"]


""" SECTION 3 """
# LOAD : exporting the data, or sending the data somewhere 

# to export to separate folder : note pandas doesn't create a directory 
df.to_csv("day_02/output/virginica_filtered.csv")

url = "https://raw.githubusercontent.com/alexandrehsd/Predicting-Pulsar-Stars/master/pulsar_stars.csv"

df = pd.read_csv(url)

