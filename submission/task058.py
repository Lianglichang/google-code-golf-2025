def p(j):
 A=range;c=len(j);E=[[0]*c for _ in A(c)];E[0]=[3]*c;W=a=c-1;k=0;l=((0,1),(1,0),(0,-1),(-1,0));C=1
 while a>0:
  for _ in A(2):
   for J in A(a):k+=l[C][0];W+=l[C][1];E[k][W]=3
   C=(C+1)%4
  a-=2
 return E