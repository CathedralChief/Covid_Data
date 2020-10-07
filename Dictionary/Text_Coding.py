#%%

import string
import csv

responses = 'C:/Users/Ben Walsh/Dropbox/Python Stuff/Covid Project/College_Responses'

state_files = []
words = []
word_list = []
for subdir, dirs, state in os.walk(responses):
    for filename in state:
        subdir = subdir.replace('\\', '/')
        file_path = subdir + '/' + filename
        state_files.append(file_path)
        

for college in state_files:
    f = open(college, 'r', encoding='utf-8')
    college_contents = f.read()
    for word in college_contents.split():
        word = word.lower()
        word = word.translate({ord(ch): '' for ch in '();,.?!0*""/:-'})
        if word not in words:
            words.append(word)
        else:
            continue

for word in words:
    lst = []
    lst.append(word)
    word_list.append(lst)

with open('words2.csv', 'w', newline= '') as f:
    write = csv.writer(f)
    write.writerows(word_list)
f.close()
