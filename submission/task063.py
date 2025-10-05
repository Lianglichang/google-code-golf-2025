def p(j):
 A=range;c=len(j);E=[*map(list,j)];B=A(1,c-1)
 for k in A(c):
  if not(j[1][k]|j[c-2][k]|sum(j[i][k]for i in B)):
   for i in B:E[i][k]=3
 for i in A(c):
  if not(j[i][1]|j[i][c-2]|sum(j[i][k]for k in B)):
   for k in B:
    if E[i][k]==0:E[i][k]=3
 return E