"""
ID: nayem.c2
LANG: PYTHON3
PROG: friday
"""

fin = open('friday.in')
fout = open('friday.out', "w")

n = int(fin.readline())

s = 1900
e = 1900 + n - 1

w = 1
dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
for y in range(s, e+1):
    leap =  y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
    
    for m in range(1, 13):
        if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
            d = 31
        elif m==2:
            if not leap:
                d = 28
            else:
                d = 29
        else:
            d = 30
        
        #for i in range(1, d+1):
        #    w = (w+1)%7
        #    if i==13:
        #        dict[w] += 1
        dict[(w+13)%7] += 1
        w = (w+d)%7

fout.write(" ".join([str(dict[k]) for k in dict.keys()])+'\n')

fin.close()
fout.close()