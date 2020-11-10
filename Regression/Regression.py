#%%
import numpy as np
from sklearn.linear_model import LinearRegression
import csv
import pandas as pd
# %%

school_list = []
covid_cases = []

with open('../Cases.csv', 'r') as cases:
    reader = csv.reader(cases)
    for row in reader:
        schools = row[0]
        schools= schools.replace('.txt', '')
        count = row[1]
        school_list.append(schools)
        covid_cases.append(count)
cases.close()

combined_list = [school_list, covid_cases]

df = pd.DataFrame(combined_list).transpose()

# %%
