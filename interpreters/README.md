= INTERPRETERS
direct/axiomatic interpreter
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
// dafne.HC

U8 *A = "ROTASPEN";
U8 *B = "DAFNEBR0";

U8 MapChar(U8 c)
{
  I64 i;
  for (i = 0; A[i]; i++)
    if (A[i] == c)
      return B[(3*i + 5) % 8];
  return c;
}

U8 *MapBlock(U8 *t)
{
  U8 *out = "";
  U8 **lines = StrSplit(t, "\n");
  I64 i, j;

  for (i = 0; lines[i]; i++) {
    U8 *row = "";
    for (j = 0; lines[i][j]; j++)
      row = Cat(row, Chr(MapChar(lines[i][j])));
    out = Cat(out, row);
    out = Cat(out, "\n");
  }
  return out;
}

U0 ReadState(I64 *step, U8 **block, U8 **src)
{
  *src = FileRead("dafne.HC");
  U8 *s = *src;

  // Extract STEP
  U8 *p = StrFind(s, "#STEP:");
  *step = Atoi(p+6);

  // Extract 5‑letter blocks after the first one
  U8 *q = s;
  I64 count = 0;
  U8 *acc = "";

  while (q = StrFind(q, "#")) {
    if (q[1] && q[2] && q[3] && q[4] && q[5] &&
        q[1] >= 'A' && q[1] <= 'Z') {

      if (count > 0) {
        U8 tmp[6];
        MemCpy(tmp, q+1, 5);
        tmp[5] = 0;
        acc = Cat(acc, tmp);
        acc = Cat(acc, "\n");
      }
      count++;
    }
    q++;
  }

  *block = acc;
}

U0 WriteState(I64 step, U8 *block, U8 *src)
{
  U8 *out = src;

  // Replace STEP
  {
    U8 buf[64];
    Sprint(buf, "#STEP:%d", step);
    out = StrReplace(out, "#STEP:", buf);
  }

  // Replace block region starting at #ROTAS
  {
    U8 *blk = "";
    U8 **lines = StrSplit(block, "\n");
    I64 i;
    for (i = 0; lines[i]; i++) {
      blk = Cat(blk, "#");
      blk = Cat(blk, lines[i]);
      blk = Cat(blk, "\n");
    }
    out = StrReplaceRegex(out, "#ROTAS(.|\n)*", blk);
  }

  FileWrite("dafne.HC", out);
}

U0 Main()
{
  I64 k;
  U8 *b, *s;

  ReadState(&k, &b, &s);

  if (k < 15) {
    WriteState(k+1, MapBlock(b), s);
  } else {
    Print("¿ĐAFNE?\n");
    Print("DAFNE\nABRDN\nFR0RF\nNDRBA\nENFAD\n");
  }

  while (TRUE) {
    U8 *L = GetStr();
    if (!StrCmp(StrTrim(L), "DAFNE"))
      Print("DAFNE\n");
  }
}
```
