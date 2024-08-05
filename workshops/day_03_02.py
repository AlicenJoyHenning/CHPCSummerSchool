# -*- coding: utf-8 -*-
"""
PLOT PRACTICE 

"""

import pandas as pd
import matplotlib.pyplot as plt
# import webbrowser

iris = pd.read_csv("day_02/data_02/iris.csv")

# CLEAN 
iris["class"] = iris["class"].str.replace("Iris-", "")

# PLOT 
