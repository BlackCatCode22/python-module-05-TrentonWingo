import re
count = 0

fh = open('mbox-short.txt')

user = input("Enter a regular expression: ")

for line in fh:
    line = line.rstrip()
    if re.search(user, line):  #This line can be translated as "Examine the user's input, and search for it in each line of mbox-short.txt."
        count = count + 1 #This line can be translated as "If there is a string/line that matches the user's input, add 1 to count.
print(count)