def p(d,P=((0,-1),(0,1),(1,0),(-1,0)),R=range,T=lambda V,R:(C:=[*zip(*V)],A:=(min(C[1])+max(C[1]))>>1,B:=(min(C[2])+max(C[2]))>>1,[*zip(*[((c,-e+B+A,d-A+B),(c,e-B+A,-d+A+B))if R else((c,2*A-d,e),(c,d,2*B-e))for c,d,e in V])])[-1]):
 F=[];K=[];G=len(d);H=len(d[0]);S=[]
 for A in R(G):
  for D in R(H):
   if (C:=d[A][D])and(C,A,D)not in F+K:
    B=[(C,A,D)];I=set()
    while B:
     J=B.pop()
     if J not in I:
      I.add(J);B+=[(C,s,u)for a,b in P if 0<=(s:=J[1]+a)<G if 0<=(u:=J[2]+b)<H if(C:=d[s][u])]
    k=(*I,)
    if len(I)>3:S.append(k);F+=k
    else:K+=k
 for B in S:
  for A in R(-G,G):
   for D in R(-H,H):
    N=[(B[0],B[1]+A,B[2]+D)for B in B];m,p=T(N,1),T(N,0)
    V=next((y for y in([N]+m+p+T(m[0],0)+T(m[1],0)+T(p[0],1)+T(p[1],1))if sum(z in K and z not in F for z in y)==3),())
    for a,(Z,y,x)in enumerate(V):d[y][x]=Z;d[B[a][1]][B[a][2]]=0
 return d