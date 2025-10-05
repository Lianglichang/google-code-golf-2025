def f(j,A,c):
 global W;l.append((j,A))
 for E in C(j-1,j+2):
  for k in C(A-1,A+2):
   if(E,k)in l:continue
   l.append((E,k))
   if not(0<=E<J and 0<=k<a) or K<=E<=K+1 and L<=k<=L+1:continue
   v=c[E][k]
   if v==2:W=8
   if v==8:f(E,k,c)
def p(c):
 global W,l,K,L,J,a,C;W,l,J,a,C,e=0,[],len(c),len(c[0]),range,enumerate
 for K,w in e(c):
  for L,b in e(w):
   if b==2:
    for E in C(K-1,K+3):
     for k in C(L-1,L+3):
      if 0<=E<J and 0<=k<a and c[E][k]==8:f(E,k,c)
    return[[W]]