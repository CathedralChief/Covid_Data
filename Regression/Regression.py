#%%
import numpy as np
from sklearn.linear_model import LinearRegression
import csv
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
# %%

# Generate Cases DF based off of the csv
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

case_df = pd.DataFrame(combined_list).transpose()
case_df.columns = ['School', 'Cases']

# Generate the values DF. Because everything is already formatted in the csv, can just import 
# with pandas

values_df = pd.read_csv('../School_Values.csv')

df = case_df.merge(values_df, left_on = 'School', right_on='School')
df = df.filter(['School', 'Cases', 'Activity Values', 'Safety Value'])

# %%

# Create the variables
school = df['School']
cases = df['Cases']
activity = df['Activity Values']
safety = df['Safety Value']

slope, intercept, r_value, p_value, std_err = stats.linregress(cases.astype('int'), activity)

# %%
