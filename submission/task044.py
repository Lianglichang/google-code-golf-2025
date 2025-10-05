def p(g):
 v=set();S=[]
 for i in range(100):
  y,x=i//10,i%10
  if(y,x)in v:continue
  t=g[y][x];q=[(y,x)];s={(y,x)};v|=s
  for Y,X in q:
   for dy,dx in((0,1),(0,-1),(1,0),(-1,0)):
    a,b=Y+dy,X+dx
    if 0<=a<10> b>=0 and(a,b)not in v and g[a][b]==t:v|={(a,b)};q+=[(a,b)];s|={(a,b)}
  S+=[(t,s)]
 H=[];P=[]
 b=lambda s,i:[min,max][i>1](t[i%2]for t in s)
 for t,s in S:
  if t==0 and any(all(b(s,i)>=b(f,i)if i<2 else b(s,i)<=b(f,i)for i in range(4))for f in(x for y,x in S if y==5)):H+=[s]
  elif t and t-5:P+=[(t,s)]
 n=lambda s:frozenset((y-(m:=min(s))[0],x-m[1])for y,x in s)
 h={};p={}
 for s in H:k=n(s);h[k]=h.get(k,[])+[s]
 for t,s in P:k=n(s);p[k]=p.get(k,[])+[(t,s)]
 c={t:sum(x==t for x,_ in P)for t,_ in P}
 for k,L in h.items():
  if k in p:
   q=p[k]
   if len(q)>1:q=[x for x in q if x[0]!=max(c,key=c.get)]or q
   for a,(t,b) in zip(L,q):
    for y,x in b:g[y][x]=0
    for y,x in a:g[y][x]=t
 return g