def p(g,L=len,R=range):
 h,w=L(g),L(g[0])
 for r in R(h):
  for c in R(w):
   if g[r][c]==8:
    for y,x in((0,1),(0,-1),(1,0),(-1,0)):
     if g[r+y][c+x]==0:
      for z in R(20):
       Y=r+y*z;X=c+x*z
       if 0<=Y<h and 0<=X<w and (v:=g[Y][X])>0:g[r][c]=v
 return g