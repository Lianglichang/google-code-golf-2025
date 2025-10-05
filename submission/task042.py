def p(g):
 o=[r[:]for r in g];R=range;h,w=len(g),len(g[0]);G={(y,x)for y in R(h)for x in R(w)if g[y][x]==3};U=set()
 for m in 3,2,1:
  for y in R(h-2*m):
   for x in R(w-2*m):
    for c1,c2,c0,c3 in((x+m,x,x-m,x+2*m),(x,x+m,x+2*m,x-m)):
     E={(y+d,c1+e)for d in R(m)for e in R(m)}|{(y+d+m,c2+e)for d in R(m)for e in R(m)}
     if E<=G and not E&U:
      U|=E
      for d in R(m):
       for e in R(m):
        Y=y+d-m;X=c0+e
        if 0<=Y<h and 0<=X<w:o[Y][X]=8
        Y=y+d+2*m;X=c3+e
        if 0<=Y<h and 0<=X<w:o[Y][X]=8
 return o