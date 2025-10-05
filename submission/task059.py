def p(j,a=enumerate,r=range(11)):
 E=0;k=[[0if(i+1)%4and(l+1)%4 else 5 for i in r]for l in r];w=[0]*9
 for l,R in a(j):
  for c,C in a(R):
   if 0<C!=5:E=int(C);w[l//4*3+c//4]+=1
 e=max(w)
 for l,R in a(k):
  for c,C in a(R):
   if not C and w[l//4*3+c//4]==e:R[c]=E
 return k