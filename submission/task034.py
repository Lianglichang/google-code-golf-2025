def p(g,R=range,L=len):
 s=({*sum(g,[])}-{0,2}).pop();h,w=L(g),L(g[0])
 for r in R(h-1):
  for c in R(w-1):
   m=(g[r][c],g[r][c+1],g[r+1][c],g[r+1][c+1])
   if min(m)>0:
    for I in(i for i in R(4) if m[i]==2):
     for i in R(10):
      y=r-i if I<2 else r+i+1;x=c+i+1 if I%2 else c-i
      for Y,X in((0,0),(-1,0),(1,0),(0,-1),(0,1)):
       Y+=y;X+=x
       if 0<=Y<h and 0<=X<w:g[Y][X]=s
 return g