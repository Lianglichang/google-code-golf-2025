def p(g,E=enumerate):
 P=[[r,c,C]for r,R in E(g)for c,C in E(R)if C and C-8]
 for r,c,_ in P:g[r][c]=0
 z=P[0]
 for r,R in E(g):
  for c,C in E(R):
   if C==8:
    g[r][c]=z[2]
    for x in P:g[r+x[0]-z[0]][c+x[1]-z[1]]=x[2]
 return g