"""
ID: nayem.c2
LANG: PYTHON3
PROG: beads
"""

def ncont(p, dir):
    if dir==1: k=p
    else: k=p-1
    
    c = 0
    color = 'w'
    for j in range(n):
        if color=='w' and neck[k] != 'w':
            color = neck[k]
        
        if color != 'w' and neck[k] != 'w' and color != neck[k]:
            break
        
        c += 1
        k += dir
        if k>=n:
            k -= n
    
    return c

fin = open('beads.in')
fout = open('beads.out', 'w')

n = int(fin.readline())
neck = fin.readline().strip()

m = 0
for i in range(n):
    mc = ncont(i, 1) + ncont(i, -1)
    if mc > m:
        m = mc

print('m', m)
fout.write(f'{min(n, m)}\n')

fin.close()
fout.close()
