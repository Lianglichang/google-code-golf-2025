def p(g,R=enumerate):
 S,T=({(i,j)for i,r in R(g)for j,x in R(r)if x==k}for k in(2,8))
 if not S or not T:return g
 E=lambda s:(min(s)[0],max(s)[0],min(t[1]for t in s),max(t[1]for t in s));a,b,c,d,e,f,h,i=E(S)+E(T)
 q=(d<h)*(h-d-1)or(i<c)*(i-c+1);p=not q and((b<e)*(e-b-1)or(f<a)*(f-a+1))
 return[[((x,y)in T)*8+((x-p,y-q)in S)*2 for y,_ in R(g[0])]for x,_ in R(g)]