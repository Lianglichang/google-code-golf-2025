def p(g):
 r=range;a=min(len(g),len(g[0]))if g and g[0]else 0
 def d(i):
  if a<3:return tuple(tuple(x-9and x for x in y)for y in i)
  b=[[x-9and x for x in y]for y in i];c=[[max(b[y][k],b[k][y])for k in r(a)]for y in r(a)]
  for h,j in enumerate(c[1:],1):
   for k,e in enumerate(j[:1:-1],2):
    if e:c[h][k]=e
  return(*map(tuple,c),)
 b=(*map(tuple,g),)
 for _ in r(256):
  c=d(b)
  if c==b:break
  b=c
 return list(map(list,b))