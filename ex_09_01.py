fname = input("Enter file: ")
if len(fname) < 1 : fname = 'clown.txt'

fhand = open (fname)

many = dict()

for line in fhand :
        line = line.rstrip()
        words = line.split()

        for word in words :
            many [word] = many.get(word, 0) + 1

# Find the top 5 words by frequency

tmp = dict ()
newlist = list ()
for k,v in many.items() :
    tup = (v,k)
    newlist.append(tup)

cool = sorted (newlist, reverse = True)

for v,k in cool [:5] :
    print(k,v)