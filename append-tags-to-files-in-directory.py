import os
import pandas as pd
import numpy as np

#Insert complete path to the excel file and index of the worksheet
df = pd.read_excel("C:\\Users\\2020745.UK\\Downloads\\Trello-Json-Markdown\\Journal Board\\200922 Trello Life Stack Tags.xlsx", sheet_name='Trello - Cards')
# insert the name of the column as a string in brackets
list1 = list(df['File']) 
list2 = list(df['Tags'])

list1_length = len(list1)

for i in range(list1_length):
	with open('C:\\Users\\2020745.UK\\Dropbox\\Nic\\Obsidian\\Personal Vault\\' + list1[i] + '.md', 'a') as f:
		f.write(str(list2[i]))
