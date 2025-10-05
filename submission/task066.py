import copy;d=copy.deepcopy;l=len;y=sorted
i=lambda g,r,c:0<=r<l(g)and 0<=c<l(g[0])
n=lambda r,c:((r+1,c),(r-1,c),(r,c+1),(r,c-1))
a=lambda x,y:(x[0]+y[0],x[1]+y[1])
m=lambda x:((x[0]>0)-(x[0]<0),(x[1]>0)-(x[1]<0))
h=lambda x,y:abs(x[0]-y[0])+abs(x[1]-y[1])
f=lambda g,v:[(A,C)for A,B in enumerate(g)for C,D in enumerate(B)if D==v]
def c(ps):
 A=set(ps);E=[]
 while A:
  F=A.pop();D=[F];G=[F]
  while D:
   H,I=D.pop()
   [A.remove((B,C))or D.append((B,C))or G.append((B,C))for B,C in n(H,I)if(B,C)in A]
  E.append(G)
 return E
e=lambda t,p:min(h(p,A)for A in t)if t else 1e9
t=lambda v:v%3<1
def w(g,s,v,r):
 C=d(g);G=set();K=L=0;A=s;D=v;O=H=e(r,A)
 while K<l(g)*l(g[0])*10:
  K+=1;F=a(A,D)
  if i(g,*F)and C[F[0]][F[1]]==2:break
  if i(g,*F)and t(C[F[0]][F[1]]):
   A=F;C[A[0]][A[1]]=C[A[0]][A[1]]or 3
   if(E:=A,D)in G or G.add(E):break
  else:
   P,W=(-D[1],D[0]),(D[1],-D[0]);I=[]
   for Q in(P,W):
    B=a(A,Q)
    if i(g,*B)and t(C[B[0]][B[1]]):I.append((e(r,B),Q!=P,Q,B))
   if I:
    _,_,X,B=min(I);D=X;A=B;C[A[0]][A[1]]=C[A[0]][A[1]]or 3
    if(E:=A,D)in G or G.add(E):break
    L+=1
   else:
    R=-D[0],-D[1];B=a(A,R)
    if i(g,*B)and t(C[B[0]][B[1]]):
     D=R;A=B;C[A[0]][A[1]]=C[A[0]][A[1]]or 3
     if(E:=A,D)in G or G.add(E):break
     L+=1
    else:break
  H=min(H,(O:=e(r,A)))
 return C,K,H,O,L,s,D
def s(g):
 D,G=f(g,2),f(g,3)
 if not(D and G):return d(g)
 E=min(c(G),key=lambda c_:((u:=l(c_)),e(D,(round(sum(a for a,_ in c_)/u),round(sum(b for _,b in c_)/u)))))
 Q=set(E)
 A=next((((H,I),(J,K))for H,I in E for J,K in n(H,I)if(J,K)in Q),None)
 if not A:A=max(((B,C)for B in E for C in E),key=lambda t_:h(*t_))
 B,C=A;F=m((C[0]-B[0],C[1]-B[1]))
 return min((w(g,C,F,D),w(g,B,(-F[0],-F[1]),D)),key=lambda r:(r[3],r[4],r[2],r[1]))[0]
def b(g):
 D=f(g,2);E=f(g,3)
 if l(D)!=2 or l(E)!=2:return
 def H(ps):(A,B),(C,D)=y(ps);return B==D and abs(A-C)==1
 if not(H(D)and H(E)):return
 (I,F),(J,P)=y(E);(K,G),(L,P)=y(D)
 if{I,J}!={K,L}:return
 M,N=y((F,G));C=None
 for A in range(min(I,K)+1):
  if all(g[A][B]in(0,3,2)for B in range(M,N+1)):C=A;break
 if not C:return
 B=d(g);Q=max(J,L)
 for A in range(C,Q+1):B[A][F]=B[A][F]or 3;B[A][G]=B[A][G]or 3
 for O in range(M,N+1):B[C][O]=B[C][O]or 3
 return B
p=lambda g:b(g)or s(g)