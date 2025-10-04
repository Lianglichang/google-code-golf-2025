def p(g):
 a=b=e=d=0;c=()
 if n:=sum(g[0]+g[-1]):g=[*zip(*g[::-1])]
 w,L=len(g[0]),len(g)
 for i in range(L):
  if (t:=g[i][0]+g[i][-1])and b<2:g[i]=[t]*w;b+=1;c+=t,;d=i
  a+=b==1
 for i in range(d+a,L,a):g[i]=[c[e]]*w;e^=1
 return(n and[*map(list,zip(*g))][::-1])or g