import os, datetime, pandas as pd

path = '/Users/nrivard/Digital Vault' # 'C:\\Users\\2020745.UK\\Dropbox\\Nic\\Obsidian\\Personal Vault\\Journal'
os.chdir(path)

listOfDates = pd.date_range(start="2021-01-01",end="2021-12-31").tolist()

def suffixGenerator(day):
    if(str(day)[-1] == '1' and (day != '11')):
        return "st"
    elif (str(day)[-1] == '2' and (day != '12')):
        return "nd"
    elif (str(day)[-1] == '3' and (day != '13')):
        return "rd"
    else:
        return "th"

for date in listOfDates:
    day = date.strftime("%d")
    suffix = suffixGenerator(day)
    if(int(day) < 10):
        day = str(day).replace("0", "")
    dailyStoic = date.strftime("%B ") + str(day) + str(suffix)
    dailyNoteText = "---\ncalories_in: \ncalories_out: \nBMR: 1800\n---\n\n##### What are you grateful for today? \n\n- \n\n##### What did you learn today? \n\n- \n\n##### What will you improve tomorrow? \
\n\n- \n\n---\n![[" + dailyStoic + "]]\n\n---\nTags: #journal "
    title = date.strftime("%y%m%d %A")
    with open(str(title) + ".md", 'w') as newFile:
        print(dailyNoteText, file=newFile)
