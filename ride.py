"""
ID: nayem.c2
LANG: PYTHON3
PROG: ride
"""

fin = open("ride.in")
fout = open("ride.out", "w")

s1, s2 = fin.readlines()[:2]

l1 = [ord(c)-64 for c in s1.strip()]
l2 = [ord(c)-64 for c in s2.strip()]

r1 = 1
for e in l1:
    r1 *= e
r2 = 1
for e in l2:
    r2 *= e

out = "GO\n" if r1%47==r2%47 else "STAY\n"

fout.write(out)

fin.close()
fout.close()