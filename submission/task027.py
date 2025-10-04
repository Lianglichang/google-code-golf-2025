def p(g):
 r=[*map(list,g)];h=len(g);w=len(g[0]);b=lambda x,y:-1<x<h and-1<y<w
 k={(x,a)for x in range(h)for a in range(w)if g[x][a]==1}
 if k:
  for o in 0,1:
   p=[t for t in {(x,a)for X,A in k for x,a in((5-X+o,A-5),(5-A+o,4-X+o),(X-5,A-4))if x*x<26>a*a} if((u:=4-t[1]+o,v:=5-t[0]+o)in k or b(u,v)<1)and((u:=5+t[1],v:=4+t[0])in k or b(u,v)<1)and((u:=5-t[0]+o,v:=5+t[1])in k or b(u,v)<1)and(u,v)in k]
   if {(x,y)for t in p for x,y in((5-t[0]+o,5+t[1]),(4-t[1]+o,5-t[0]+o),(5+t[1],4+t[0]))if b(x,y)}==k:
    for x,a in p:
     if b(4+x,4-a+o)and not r[4+x][4-a+o]:r[4+x][4-a+o]=2
    break
 return r