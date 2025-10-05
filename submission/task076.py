_A=0
import collections as C
def m(g):
 if not(g and g[0]):return 0
 c=C.Counter(sum(g,[]));t=max(c.values());b=[k for k in c if c[k]==t];return min(b)if 0 not in b else 0
def o(g,u=_A,d=_A,w=1):
 if not(g and g[0]):return[]
 H,I=len(g),len(g[0]);J=m(g)if w else None;D=[[0]*I for _ in range(H)];N=[];P=[(1,0),(-1,0),(0,1),(0,-1)]+[(1,1),(1,-1),(-1,1),(-1,-1)]*d
 for E in range(H):
  for F in range(I):
   C=g[E][F]
   if D[E][F]or w and C==J:continue
   O=C if u else None;G=[(E,F)];D[E][F]=1;K=[]
   while G:
    L,M=G.pop();C=g[L][M]
    if u and C!=O or not u and w and C==J:continue
    K.append((C,(L,M)))
    for Q,R in P:
     A,B=L+Q,M+R
     if 0<=A<H and 0<=B<I and not D[A][B]:
      if u:
       if g[A][B]==O:D[A][B]=1;G.append((A,B))
      elif not(w and g[A][B]==J):D[A][B]=1;G.append((A,B))
   if K:N.append(K)
 return N
def b(o):
 E=iter(o);H,(F,G)=next(E);A=B=F;C=D=G;[((A:=min(A,E)),(B:=max(B,E)),(C:=min(C,F)),(D:=max(D,F)))for(G,(E,F))in E];return A,C,B,D
n=lambda o:o if not o else(lambda mi,mj,ma,mj2:[(A,(B-mi,C-mj))for(A,(B,C))in o])(*b(o))
s=lambda o,d:[(C,(D+d[0],E+d[1]))for(C,(D,E))in o]
v=lambda o:o if not o else(lambda mi,mj,ma,mj2:[(A,(B,mj+mj2-C))for(A,(B,C))in o])(*b(o))
h=lambda o:o if not o else(lambda mi,mj,mi2,mj2:[(A,(mi+mi2-B,C))for(A,(B,C))in o])(*b(o))
dm=lambda o:o if not o else(lambda mi,mj,ma,mj2:[(A,(C-mj+mi,B-mi+mj))for(A,(B,C))in o])(*b(o))
c=lambda o:v(dm(v(o)))
def f(g,o):
 if not(g and g[0]):return g
 D,E=len(g),len(g[0]);A=[*map(list,g)]
 for F,(B,C)in o:
  if 0<=B<D and 0<=C<E:A[B][C]=F
 return A
def y(g,o):
 if not(g and g[0]):return set()
 B,D=len(g),len(g[0]);A=n(o)
 if not A:return set()
 C,E,F,G=b(A);H,I=F-C+1,G-E+1;return{(B,C)for B in range(B-H+1)for C in range(D-I+1)if all(g[B][C]==A for(A,(B,C))in s(A,(B,C)))}
def p(I):
 if not(I and I[0]):return I
 C=o(I,d=1)
 if not C:return I
 F=max(C,key=lambda o:len({a for a,_ in o}));T=[c,dm,h,v];D=set()
 for H in T+[lambda x,a=A,b=B:a(b(x))for A in T for B in T]:
  E=n(H(F));A=[q for q in E if q[0]in(2,4)]
  if not A:continue
  K,L=min(p[1][0]for p in A),min(p[1][1]for p in A)
  for M,N in y(I,A):D|=set(s(E,(M-K,N-L)))
 return f(I,D)