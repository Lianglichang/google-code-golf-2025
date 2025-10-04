d=len;r=range;z=lambda g:[*map(list,zip(*g[::-1]))]
def p(g):
 f={0}
 for i in r(8):
  g=z(g)
  for i in r(q:=d(g)):
   if min(g[i])==max(g[i])>0:
    f|={p:=g[i][0]};o=d(g[0])
    for e in r(i-1):
     n=0
     for t in r(o):
      if g[e][t]==p:g[e][t]=0;n-=1;g[i+n][t]=p
    for e in r(i+1,q):
     n=0
     for t in r(o):
      if g[e][t]==p:g[e][t]=0;n+=1;g[i+n][t]=p
 return[[t*(t in f)for t in i]for i in g]