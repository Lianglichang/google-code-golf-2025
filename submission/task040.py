def p(g):
 F=g[0][0];E=F==g[0][9];G=g[9][0]if E else g[0][9];I=next(x for r in g for x in r if x not in(F,G,0));r=range(10)
 for a in r:
  for b in r:
   if g[a][b]==I:g[a][b]=F if(a<5 if E else b<5)else G
 return g