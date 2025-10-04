def p(j,A=enumerate):
 F=sum(j,[]);d=len(j[0]);c=[[0]*d for _ in j]
 for E in{*F}-{0}:
  k=[(n//d,n%d)for n,x in A(F)if x==E];W,l=map(max,zip(*k))
  for J,a in k:c[J][a+(J<W)*(a<l)]=E
 return c