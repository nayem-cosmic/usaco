"""
ID: nayem.c2
LANG: PYTHON3
PROG: milk2
"""

fin = open('milk2.in')
fout = open('milk2.out', 'w')

n = int(fin.readline())
l = []
for i in range(n):
    l.append(list(map(int, fin.readline().split())))
l = sorted(l, key=lambda x: x[0])

mil = []
nomil = 0
lpos = 0

for i, sp in enumerate(l):
    if i == 0:
        mil.append(sp[1]-sp[0])
    else:
        if sp[0] <= lpos and sp[1] > lpos: 
            mil[-1] += sp[1]-lpos
        elif sp[0] > lpos:
            nomil = max(nomil, sp[0]-lpos)
            mil.append(sp[1]-sp[0])
            
    lpos = sp[1] if sp[1]>lpos else lpos

fout.write(f"{max(mil)} {nomil}\n")

fin.close()
fout.close()