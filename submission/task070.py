def p(j):
 R=range;c=[r[:]for r in j];e=[(i,k)for i in R(len(j))for k in R(len(j[0]))if j[i][k]==8]
 if e:
  a,b=min(e)[0],max(e)[0];l=min(k for _,k in e);m=max(k for _,k in e)
  for i in R(a,b+1):
   for k in R(l,m+1):
    if j[i][k]==1:c[i][k]=3
 return c