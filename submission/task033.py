def p(g):
 r=range;c=[a[:]for a in g];e=g[5][0]
 for Y,X in(0,6),(0,12),(6,0),(6,6),(6,12),(12,0),(12,6),(12,12):
  for y in r(3):
   for x in r(3):
    a=Y+y+1;b=X+x+1;t=g[y+1][x+1];v=g[a][b];c[a][b]=t and(v if t==v else e)
 return c