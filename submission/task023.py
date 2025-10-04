def p(t):
 from itertools import combinations as b;u,w=len(t),len(t[0]);r=range;f=lambda p,s,i:[(p,s),(p,s+1),(p+1,s),(p+1,s+1)]if i<1 else[(p,s),(p+1,s),(p+2,s)]if i<2 else[(p,s),(p,s+1),(p,s+2)];a=[(p,s,i)for i in r(3)for p in r(u-(1,2,0)[i])for s in r(w-(1,0,2)[i])if all(t[x][y]==5 for x,y in f(p,s,i))];y={(p,s)for p in r(u)for s in r(w)if t[p][s]==5};g=lambda q:{*sum((f(*e)for e in q),[])};h=lambda q:(d:=g(q))==y and len(d)==sum(4-(i>0)for _,_,i in q)
 def z(s,t,a):
  for j,e in enumerate(a):
   q={*f(*e)}
   if q&s and not q&g(t)and(k:=z(s-q,t+[e],a[j+1:])):return k
  return[]if s else t
 i=next((c for s in r(1,10)for c in b(a,s)if h(c)),0)or z(y,[],a)or[]
 C,L=set(),[];[(L.append(P),C.update(q))for P in sorted(a,key=lambda r:r[2:]+r[:2])if not(q:={*f(*P)})&C];i=i or L
 [t[x].__setitem__(y,8-(P[2]>0)*6)for P in i for x,y in f(*P)];return t