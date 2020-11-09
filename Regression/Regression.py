#%%
import numpy as np
from sklearn.linear_model import LinearRegression
import csv
# %%

school_list = []
covid_cases = []

with open('../Dictionary/Cases.csv', 'r') as cases:
    reader = csv.reader(cases)
    for row in reader:
        schools = row[0]
        count = row[1]
        school_list.append(schools)
        covid_cases.append(count)
cases.close()
# %%
