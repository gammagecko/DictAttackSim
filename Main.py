# Download pandas

import pandas as pd
import re

def has_no_letters(s):
    return not re.search("[a-zA-Z]", s)

def has_numbers(s):
    if type(s) != str:
        return True
    if re.search("[0-9]", s):
        return True
    return False

passList = []
engWordList = []
numAndWordList = []
# Open password list and assign to list passList
with open("xato-net-10-million-passwords-1000000.txt") as file:
    i = 0
    for line in file:
        passList.append(line.strip())
        i += 1
        if i > 40000:
            break
# Open common words and assign to sortedWordList
with open("30k.txt") as file:
    count = 0
    for line in file:
        count += 1
        sLine = line.strip()
        if count % 1000 == 0:
            print(count)
        if "null" in sLine:
            continue
        elif type(sLine) != str or re.search(r"[0-9]", sLine):
            numAndWordList.append(sLine)
        else:
            sLine = sLine.lower()
            engWordList.append(sLine)

for word in engWordList:
    print(word)

#Sort word list by pw size so we don't encounter miniwords
sortedWordList = sorted(engWordList, key=len, reverse=True)

df = pd.DataFrame(columns=["word", "count"])
df["word"] = sortedWordList
df["count"] = 0

ndf = pd.DataFrame(columns=["word", "count"])
ndf["word"] = numAndWordList
ndf["count"] = 1

num = 0
fileNum = 0
# scans through the passwords in passList
for pw in passList:
    pw2 = pw
    num += 1
    if num % 100 == 0:
        print(num)
    groupOfWords = []
    # scans through the 10000 top google hits
    for word in sortedWordList:
        # if there is a match between a top google hit and a pw
        if word in pw and len(word) > 2:
            groupOfWords.append(word)
            pw = pw.replace(word, "")
        elif word[0].upper() + word[1:].lower() in pw and len(word) > 2:
            groupOfWords.append(word.lower())
            pw = pw.replace(word, "")
    for word in groupOfWords:
        index = df.index[df["word"] == word]
        df.iloc[index, 1] += 1

fileNum += 1
# Drop words not used
i = len(df) - 1
while i >= 0:
    if df.iloc[i, 1] == 0:
        df.drop(i, inplace=True)
    i -= 1
# Put DF to file
sorted_df = df.sort_values(by=['count'], ascending=False)
sorted_df.to_csv("Name And Word Count " + str(fileNum) + ".csv")