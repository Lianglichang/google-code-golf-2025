def p(g,E=enumerate,R=range):
 t=l=9**9;b=r=-1
 for y,a in E(g):
  for x,v in E(a):
   if v:t=min(t,y);b=max(b,y);l=min(l,x);r=max(r,x)
 s=t+b;S=l+r
 for y in R(t,b+1):
  for x in R(l,r+1):
   P=((y,x),(y,S-x),(s-y,x),(s-y,S-x),(t+x-l,l+y-t),(t+r-x,l+y-t),(t+x-l,l+b-y),(t+r-x,l+b-y));c=max(g[i][j]for i,j in P)
   for i,j in P:g[i][j]=c
 return g