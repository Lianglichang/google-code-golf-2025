def p(g,E=enumerate):
 X=[[0]*3,[0]*3,[0]*3]
 for r,a in E(g):
  for c,x in E(a):
   if x==5:
    for i in-1,0,1:
     for j in-1,0,1:
      if -1<r+i and-1<c+j and(t:=g[r+i][c+j]):X[i+1][j+1]=t
 return X