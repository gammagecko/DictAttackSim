import pandas as pd
import re
def has_no_letters(s):
    return not re.search("[a-zA-Z]", s)
df = pd.read_csv('Name And Word Count 1.csv')
df = df[df['count'] > 1]
df2 = df.reset_index()

digs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specs = ['!', '@', '#', '$', '%', '^', '&', '*']
digSpecs = digs + specs

listy = []
allPws = []

# prints all the entries
for i in range(len(df2)):
    print(df2.iloc[i, 2])
# scans through all rows in the data frame
for i in range(len(df2)):
    first = df2.iloc[i, 2]
    firstL = first[0].upper() + first[1:].lower()
    print(first)
    print(firstL)

    # scans through 10 numbers
    for j in range(10):
        pw = first + str(j)
        print(pw)
        pwL = firstL + str(j)
        print(pwL)
        for spec in specs:
            pw2 = pw + spec
            print(pw2)
            pw2L = pwL + spec
            print(pw2L)
        for k in range(10):
            pw2 = pw + str(k)
            print(pw2)
            pw2L = pwL + str(k)
            print(pw2L)
            for digSpec2 in digSpecs:
                print(pw2 + digSpec2)
                print(pw2L + digSpec2)