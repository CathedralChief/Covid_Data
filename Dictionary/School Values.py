#%%
import csv
import ntpath
import os
import pandas as pd 
# %%

safety_dict = {}
active_dict = {}

with open('words.csv', 'r') as values:
    reader = csv.reader(values)
    for row in reader:
        word = row[0]
        ax1 = row[1]
        ax2 = row[2]
        safety_dict[word] = ax1
        active_dict[word] = ax2
values.close()

ntpath.basename('../College_Responses/')

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


school_safe_values = {}
school_act_values = {}
school_safe_count = {}
school_act_count = {}
responses = '../College_Responses/'

state_files = []
words = []
word_list = []
for subdir, dirs, state in os.walk(responses):
    for filename in state:
        subdir = subdir.replace('\\', '/')
        file_path = subdir + '/' + filename
        state_files.append(file_path)

for college in state_files:
    f = open(college, 'r', encoding='utf-8', errors='replace')
    college_contents = f.read()
    school = path_leaf(college)
    school = school.strip('.txt')
    school_safe_count[school] = 0
    school_act_count[school] = 0
    for word in college_contents.split():
        word = word.lower()
        word = word.translate({ord(ch): '' for ch in '();,.?!0*""/:-'})

        

        # Find the values for the word
        if word not in safety_dict:
            safe_value = 0
        else:
            safe_value = int(safety_dict[word])
        if word not in active_dict:
            active_value = 0
        else:
            active_value = int(active_dict[word])

        # Keep track of running value for each school
        if school not in school_act_values:
            school_act_values[school] = active_value
        else:
            school_act_values[school] += active_value
        if school not in school_safe_values:
            school_safe_values[school] = safe_value
        else:
            school_safe_values[school] += safe_value

        # Keep track of how many words are counted for each school

        if safe_value != 0:
            school_safe_count[school] += 1
        if active_value != 0:
            school_act_count[school] += 1

school_norm_act_dict = {}
for school in school_act_values:
    value = school_act_values[school]
    count = school_act_count[school]
    norm_value = round(value/count, 4)
    school_norm_act_dict[school] = norm_value

school_norm_safe_dict = {}
for school in school_safe_values:
    value = school_safe_values[school]
    count = school_safe_count[school]
    norm_value = round(value/count, 4)
    school_norm_safe_dict[school] = norm_value
# %%
print(school_norm_act_dict)
print(school_norm_safe_dict)
# %%
for i in school_norm_act_dict:
    print(i, ': ', school_norm_act_dict[i])
# %%
act_df = pd.DataFrame.from_dict(list(school_norm_act_dict.items()))
act_df.columns = ['School', 'Activity Values']
safe_df = pd.DataFrame.from_dict(list(school_norm_safe_dict.items()))
safe_df.columns = ['School', 'Safety Value']

df = act_df.merge(safe_df, left_on='School', right_on='School')

df.to_csv('../School_Values.csv')
# %%
