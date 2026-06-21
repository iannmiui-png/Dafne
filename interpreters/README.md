# INTERPRETERS
direct/axiomatic interpreter (Zimbu)
```bash
imp/ort sys¿ĐAFNE
Đeffne = "SATOR AREPO TENET OPERA ROTAS".split()
Đict = dict(zip("ROTASPEN", "DAFNEBR0"))
D = ["".join(Đict[c] for c in Đeffne[4 - i]) for i in range(5)]
print("¿ĐAFNE?")
for line in sys.stdin:
     s = line.strip()
     if all(c in Đict for c in s) and "".join(Đictz[c] for c in s) == D[0]:
         print(*D, sep="\n")```
self-modifying
```bash
// CLASS D

  CONST A="ROTASPEN",B="DAFNEBR0";

  FUNC M(c CHAR) CHAR { VAR i=A.indexOf(c); RETURN i<0?c:B[(3*i+5)%8]; }

  FUNC T(s STRING) STRING
    VAR o=""; FOR i IN 0..s.len()-1 o+=M(s[i]); OD RETURN o;
  END

  FUNC E() LIST<STRING>
    VAR W="SATOR AREPO TENET OPERA ROTAS".split(" "),D LIST<STRING>=[];
    FOR i IN 0..4 D.append(T(W[4-i])); OD
    RETURN D;
  END

  FUNC main()
    VAR D=E();
    Out.println("¿ĐAFNE?");
    WHILE TRUE
      VAR s=In.readLine().trim();
      IF s.len()>0
        IF T(s)==D[0]
          FOR r IN D Out.println(r); OD
        FI
      FI
    OD
  END

END

```
# WIKI
= The DAFNE square =
Axiomatic DAFNE "doorway" (Zimbu)
<pre>
CLASS D

  CONST A="ROTASPEN"; CONST B="DAFNEBR0";

  FUNC m(c CHAR) CHAR
    VAR i=A.indexOf(c);
    RETURN i>=0?B[(3*i+5)%8]:c;
  END

  FUNC main()
    VAR W="SATOR AREPO TENET OPERA ROTAS".split(" ");
    VAR D LIST<STRING>=[];
    FOR i IN 0..4
      VAR s=W[4-i],o="";
      FOR j IN 0..s.len()-1 o+=m(s[j]); OD
      D.append(o);
    OD

    Out.println("¿ĐAFNE?");
    WHILE TRUE
      VAR s=In.readLine().trim();
      VAR ok=TRUE;
      FOR i IN 0..s.len()-1 IF A.indexOf(s[i])<0 ok=FALSE; FI OD
      IF ok
        VAR t="";
        FOR i IN 0..s.len()-1 t+=m(s[i]); OD
        IF t==D[0]
          FOR r IN D Out.println(r); OD
        FI
      FI
    OD
  END

END</pre>
{|
| 
|-
| DAFNE
|-
| ABRDN
|-
| FR0RF
|-
| NDRBA
|-
| ENFAD
|}

0D theta conversion operator
<pre>
SATOR
    O
    T
    A
    S
</pre>
=== Triadic expansion ===
(python)
<pre>#!SELF-MODIFYING
import re,sys

# ===============
# AXIOM
# ROTAS
# OPERA
# TENET
# AREPO
# SATOR
# ===============

A="ROTASPEN";B="DAFNEBR0"
f=lambda c:B[(3*A.index(c)+5)%8]if c in A else c
g=lambda t:"\n".join("".join(f(c)for c in l)for l in t.split("\n"))

def r():
 s=open(__file__,encoding="utf-8").read()
 m=re.search(r"AXIOM\n((?:# [A-Z0-9]{5}\n){5})",s)
 b=[ln[2:] for ln in m.group(1).splitlines()]
 return "\n".join(b),s

def w(b,s):
 x="\n".join("# "+l for l in b.split("\n"))+"\n"
 s=re.sub(r"(AXIOM\n)(?:# [A-Z0-9]{5}\n){5}",r"\1"+x,s)
 open(__file__,"w",encoding="utf-8").write(s)

b,s=r()

if b=="DAFNE\nABRDN\nFR0RF\nNDRBA\nENFAD":
 print(b)
else:
 nb=g(b)
 w(nb,s)
 print(nb)
</pre>
{|
|+ Dafne L-system
|-
! # Axioms !! expansion rule
|-
| <pre># ROTAS
# OPERA
# TENET
# AREPO
# SATOR</pre> || <pre>
DAFNE
ABRDN
FR0RF
NDRBA
ENFAD
BDFBR
D00BB
F0F0F
BB00D
RBFDB
BDNRA
DE0BR
N0F0N
RB0ED
ARNDB
</pre>
|}
=== 1D expansion ===
ROTASPEN DAFNEBR0
<pre>
DAFNE
ABRDN
FR0RF
NDRBA
ENFAD
expansion rules
[4,4,4,4,4,4,4,5,6]
[4,2,6,8,4,7,4,2,3]
[4,6,4,4,2,8,7,2,4]
[4,8,7,4,8,7,4,8,7]
[4,4,3,8,2,6,4,2,7]
[4,7,2,6,2,8,3,4,7]
[4,4,4,4,4,4,4,4,4]
[5,2,7,8,2,3,4,4,6]
[6,3,2,4,7,4,8,6,2]
[1,4,4,4,4,4,4,4,4]
NNNNABNBNN0RNNF
NNN0NRNAONOROAB
NEBNAFRANN0RNAR
NABNRANNNNNNN0R
0NRBAONNNNNNNOR
NAFFNRNNNNEBN0R
NBNNNNBFANNNNBN
NAONNNNRNNNNNAO
RANNNN0BANNNRAN
N0RNNNNNNNRANAB
NORNNNNNNBAO0NR
N0RNEBNNNFNRNAF
NNFN0RNBNNABNNN
OABNORNAO0NRNNN
NARN0RRANNAFNEB
</pre>
''i.e''
<pre>
s=[list("DAFNE"),list("ABRDN"),list("FR0RF"),list("NDRBA"),list("ENFAD")]
r=[[4,4,4,4,4,4,4,5,6],[4,2,6,8,4,7,4,2,3],[4,6,4,4,2,8,7,2,4],[4,8,7,4,8,7,4,8,7],
   [4,4,3,8,2,6,4,2,7],[4,7,2,6,2,8,3,4,7],[4,4,4,4,4,4,4,4,4],[5,2,7,8,2,3,4,4,6],
   [6,3,2,4,7,4,8,6,2],[1,4,4,4,4,4,4,4,4]]
</pre>
expansion rule
<pre>
u=[]
for row in s:
    for c in row:
        if c not in u:u.append(c)
while len(u)<9:u.append(u[-1])
m={i+1:u[i] for i in range(9)}
sr={u[i]:i for i in range(len(u))}
</pre>
alternating 0/O
<pre>
C=[0]
def z(x):
    if x!=8:return m[x]
    C[0]^=1
    return "0" if C[0] else "O"
</pre>
'''Linear (X)'''
<pre>
def X(g):
    o=[]
    for row in g:
        a=[[],[],[]]
        for c in row:
            t=r[sr[c]] if c in sr else [4]*9
            b=[z(x) for x in t]
            a[0]+=b[:3];a[1]+=b[3:6];a[2]+=b[6:]
        o+=a
    return o

for L in X(s):print("".join(L))
</pre>
The ROTASPEN dictionary creates a "Dafne square" which is a condensed [https://en.wikipedia.org/wiki/Vedic_square Vedic square].
The vedic square can be observed via Vedic_square.pgm

