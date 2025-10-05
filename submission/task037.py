def p(j,e=enumerate,r=range):
 w=[a[:]for a in j];k={}
 for y,a in e(j):
  for x,v in e(a):
   if v:k[v]=k.get(v,[])+[(y,x)]
 for a in k:
  (y,x),(Y,X)=k[a]
  for d in r(abs(Y-y)+1):w[y+d*(1-2*(Y<y))][x+d*(1-2*(X<x))]=a
 return w