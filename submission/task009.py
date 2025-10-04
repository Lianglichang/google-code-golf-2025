def p(m):
 I=range(k:=len(m));h=m[2][2];r=eval(str(n:=[[v*(v!=h)for v in R]for R in m]));E=lambda t:(t.index(c),k-t[::-1].index(c))if c in t else(0,0)
 for c in I:
  for i in I:
   a,b=E(n[i]);r[i][a:b]=[c]*(b-a)
   for j in range(*E(t:=[r[i]for r in n])):r[j][i]=c
 return[[(h,r[i][j])[m[i][j]!=h]for j in I]for i in I]