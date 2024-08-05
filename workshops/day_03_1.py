""" 
EDA : Exploratory Data Analysis aka VISUALISATION

Excel is not reproducible (formatting). There are various libraries you can use in python to visualise things

> Matplotlib (static)
> Seaborn (nicer)
> Plotly (nicest) 

data-to-viz : website (code for python & R!!!)

"""

# Line Plots 
import matplotlib.pyplot as plt

# react_conv = [0.5, 0.6, 0.7, 0.7, 0.9]
# temp = [180, 200, 220, 240, 260]

# LINE

# plt.plot(temp, react_conv)
# plt.xlabel("Temperature")
# plt.ylabel("Reaction conversion")
# plt.title("Chemical experiment")

# plt.show()

# BAR

# day1_attendees = [70, 20, 64, 90, 80]
# day1_names = ["Blessing", "Mali", "Pangi", "Tafi", "Shini"]

# plt.bar(day1_names, day1_attendees)
# plt.show()

# SCATTER
# x_scatter = [1, 2, 3, 4, 5]
# y_scatter= [2, 4, 6, 8, 10]

# plt.scatter(x_scatter, y_scatter)
# plt.show()

# HISTOGRAM 

# x_histogram = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# plt.hist(x_histogram)
# plt.show()

import plotly.express as px 
import webbrowser

df = px.data.gapminder().query("continent=='Oceania'")
fig = px.line(df, x = 'year', y = 'lifeExp', color = 'country')
fig.write_html("plot.html")

# Used to automatically open the plot 
webbrowser.open("plot.html")



