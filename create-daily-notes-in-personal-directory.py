import os, datetime, pandas as pd

path = '/Users/nrivard/Digital Vault/Journal'
os.chdir(path)

listOfDates = pd.date_range(start="2026-01-01",end="2026-12-31").tolist()

def suffixGenerator(day):
    if(str(day)[-1] == '1' and (day != '11')):
        return "st"
    elif (str(day)[-1] == '2' and (day != '12')):
        return "nd"
    elif (str(day)[-1] == '3' and (day != '13')):
        return "rd"
    else:
        return "th"

def getFitnessBlockId(date):
    """Generate the block ID for the 365-Day Fitness Challenge embed."""
    # ISO week number (Jan 5, 2026 = Week 2)
    week_num = date.isocalendar()[1]
    # Day of week: Monday=1, Sunday=7
    day_of_week = date.isoweekday()
    return f"^d{week_num}a{day_of_week:03d}"

for date in listOfDates:
    day = date.strftime("%d")
    suffix = suffixGenerator(day)
    if(int(day) < 10):
        day = str(day).replace("0", "")
    dailyStoic = date.strftime("%B ") + str(day) + str(suffix)
    fitnessBlockId = getFitnessBlockId(date)
    fitnessEmbed = f"![[365-Day Fitness Challenge#{fitnessBlockId}]]"
    dailyNoteText = f"""---
calories_in:
calories_out:
bmr: 1700
intermittent_fasting: false
huel: false
learning_hour: false
push-ups: false
squats: false
---
{fitnessEmbed}

##### What are you grateful for today?

-

##### What did you learn today?

-

##### What will you improve tomorrow?

-

---
![[{dailyStoic}]]

---
Tags: #journal """
    title = date.strftime("%y%m%d %A")
    with open(str(title) + ".md", 'w') as newFile:
        print(dailyNoteText, file=newFile)
