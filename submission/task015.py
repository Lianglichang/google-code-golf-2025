def p(g,r=range(9),t=(-1,0,1)):
 s=[(i,j,v>1)for i in r for j in r if 0<(v:=g[i][j])<3]
 for i,j,q in s:
  for a in t:
   for b in t:
    if a|b and (a*b!=0)==q:g[i+a][j+b]=7-3*q
 return g