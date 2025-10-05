def p(a):
 R=range;a=[*map(list,a)];g,f=len(a),len(a[0]);n={}
 for r in a:
  for v in r:
   if v:n[v]=n.get(v,0)+1
 x,y,t=next((i,j,a[i][j])for i in R(g)for j in R(f)if a[i][j]and n[a[i][j]]==1)
 for G,H in((0,1),(1,0),(0,-1),(-1,0)):
  d,k=x+G,y+H
  if(d<0)|(d>=g)|(k<0)|(k>=f)|(a[d][k]==0):
   i,j=x,y
   while(0<=i-G<g)&(0<=j-H<f):
    i-=G;j-=H
    if a[i][j]==0:a[i][j]=t
 return a