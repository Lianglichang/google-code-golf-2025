def p(t,z=enumerate):
 w=len(t[0]);r=range(1,w);Z=zip
 g=next((i for i in r if all((x*y<1)|(x==y)for R in t for x,y in Z(R,R[i:]))),w)
 a=next((i for i in r if all((x*y<1)|(x==y)for R,S in Z(t,t[i:])for x,y in Z(R,S))),w)
 C={(y%a,x%g):v for y,R in z(t)for x,v in z(R)if v}
 [v or R.__setitem__(x,C[y%a,x%g])for y,R in z(t)for x,v in z(R)]
 return t