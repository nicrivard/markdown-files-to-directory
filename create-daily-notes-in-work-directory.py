import os, datetime, pandas as pd

path = '/Users/nrivard/Work Vault' # 'C:\\Users\\2020745.UK\\OneDrive - EY\Work Vault'
os.chdir(path)

listOfDates = pd.date_range(start="2025-01-01",end="2025-12-31").tolist()

for date in listOfDates:
    YYMMDD = date.strftime("%y%m%d")
    YYYYW = date.strftime("%Y W%W")
    dailyNoteText = '###### Priori-threes\n1. \n2. \n3. \n\n###### Notes\n- \n\n```query\nline: ("- [ ]" ' + YYMMDD + ' -"line:")\n```\n\n###### Review\n\n\n###### Completed\n\n```query\nline: ("- [x]" ' + YYMMDD + ' -"line:")\n```\n\n---\nTags: \nReferences: [[' + YYYYW + ']]'
    title = date.strftime("%y%m%d %A")
    with open(str(title) + ".md", 'w') as newFile:
        print(dailyNoteText, file=newFile)
