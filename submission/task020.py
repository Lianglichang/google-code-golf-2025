def p(g,E=enumerate,R=range):
 t=l=9**9;b=r=-1
 for y,a in E(g):
  for x,v in E(a):
   if v:t=min(t,y);b=y;l=min(l,x);r=max(r,x)
 for y in R(t,b+1):
  for x in R(l,r+1):
   U,V,Y,B=t+x-l,t+r-x,l+y-t,l+b-y;P=((y,x),(y,l+r-x),(t+b-y,x),(t+b-y,l+r-x),(U,Y),(V,Y),(U,B),(V,B));c=max(g[i][j]for i,j in P)
   for i,j in P:g[i][j]=c
 return g