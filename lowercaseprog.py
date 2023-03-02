import numpy
import pandas as pd
import os

data = pd.read_csv('PCP till the end.csv')

column_name = 'test'  # Name of the column
column_data = data[column_name]
print(column_data)

sourceFile = open('PCP till the end.txt', 'w')

for elements in column_data:
    print(elements.lower(),file = sourceFile) 
