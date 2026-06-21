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
