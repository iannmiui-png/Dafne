import sys
Đeffne = "SATOR AREPO TENET OPERA ROTAS".split()
Đict = dict(zip("ROTASPEN", "DAFNEBR0"))
D = ["".join(Đict[c] for c in Đeffne[4 - i]) for i in range(5)]
print("¿ĐAFNE?")
for line in sys.stdin:
     s = line.strip()
     if all(c in Đict for c in s) and "".join(Đictz[c] for c in s) == D[0]:
         print(*D, sep="\n")```
