"""
ID: nayem.c2
LANG: PYTHON3
PROG: gift1
"""

fin = open('gift1.in')
fout = open('gift1.out', "w")

lines = [w.strip() for w in fin.readlines()]

np = int(lines[0])
membs = lines[1:np+1]
d = {}
for m in membs:
    d[m] = 0
i = np + 1

while i < len(lines):
    name = lines[i]
    i += 1
    t, j = [int(v) for v in lines[i].split()]
    print(t)
    each = t//j if j!=0 else 0
    for k in range(j):
        i += 1
        d[lines[i]] += each
    d[name] += - each*j
    i += 1

for k in d.keys():
    fout.write(f"{k} {d[k]}\n")
    
fin.close()
fout.close()
