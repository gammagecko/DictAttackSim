Welcome to my password cracking simulator.

Currently, the first script takes in two files.

The first is a list of the 10,000,000 most common passwords, which can be found at:
https://github.com/danielmiessler/SecLists/blob/master/Passwords/xato-net-10-million-passwords-1000000.txt

The second is a list of the 30,000 most common English words, which can be found at:
https://github.com/arstgit/high-frequency-vocabulary/blob/master/30k.txt

The first script to run is Main.py. 
It takes in the two above .txt files and puts their contents to two different lists of strings. 
If there are numbers in the 30,000 most common English word list, it does not add it to the list. 
If a word is < 3 characters, it does not add it to the list. 
We then check to see if there are words from our English word list within each password. 
If we find a hit, we add to the count of that word. 

*Substrings of larger words will not be added, because we sorted the word list by size (descending), then remove each word that gets a hit from that specific password.

We remove words from the list that do not occur in the first 40,000 passwords, then export the file to "Name and Word Count 1.csv". 
The script takes several minutes to run.

In our second script, we make a dataframe from the "Name and Word Count 1" csv file. 
We then output everyword, everyword[0-9], everyword[0-9][0-9/!-*], and everyword[0-9][0-9][0-9/!-*]. 
There are approximately 12,000,000 combinations. 
The script takes several minutes to run.
