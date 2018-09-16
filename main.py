# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 00:03:57 2018

@author: parth
"""

# Importing required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Settings to produce nice plots in a Jupyter notebook
plt.style.use('fivethirtyeight')
# Reading in the data
stock_data = pd.read_csv("datasets/stock_data.csv")
benchmark_data =  pd.read_csv("datasets/benchmark_data.csv")
# Display summary for stock_data
print('Stocks\n')
# ... YOUR CODE FOR TASK 2 HERE ...
stock_data.info()
# Display summary for benchmark_data
print('\nBenchmarks\n')
# ... YOUR CODE FOR TASK 2 HERE ...
benchmark_data.info()