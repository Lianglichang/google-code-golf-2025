def p(g,R=range):
 g=[r*2 for r in g]+[r*2 for r in g];h=len(g);w=len(g[0])
 for r in R(h):
  for c in R(w):
   if 0<g[r][c]!=8:
    for i in-1,1:
     for j in-1,1:
      u=r+i;v=c+j
      if-1<u<h and-1<v<w and(g[u][v]or g[u].__setitem__(v,8)):0
 return g