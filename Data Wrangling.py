import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


import warnings
warnings.filterwarnings('ignore')

# Step 1. Aggregate the datasets
# Iterrate each file in the directory
files = [file for file in os.listdir('./Data')]
for file in files:
    print(file)

# Concatinate the file names in the dataframe
all_data = pd.DataFrame()
for file in files:
    df = pd.read_csv('./Data/' + file)
    all_data = pd.concat([all_data, df])

print(all_data.head())

# Make it into a new csv file
all_data.to_csv('all_data2.csv', index=False)

# Step 2 Clean the data
all_data = all_data.dropna(how='all')
print(all_data.head())


# Q1.What was the best month for sales. How much was earned ?
