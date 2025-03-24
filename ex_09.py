
fname = input('Enter file name: ')
if len(fname) < 1: fname = 'mbox-short.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    lin = lin.split()

if len(lin) > 2:
    if lin[0] == 'From':
        w = lin[2]
        di[w] = di.get(w,0) + 1
print (di)