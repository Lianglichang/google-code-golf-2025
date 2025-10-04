def p(a):
 o,d=len(a),len(a[0]);E=(-4,0,4);t=range;T=t(3);q,r,j,b=[[d]*10,[o]*10,[-1]*10,[-1]*10]
 for s in t(o):
  for h in t(d):
   m=a[s][h];q[m]=min(q[m],h);r[m]=min(r[m],s);j[m]=max(j[m],h);b[m]=max(b[m],s)
 for m in t(1,10):
  if j[m]-q[m]==b[m]-r[m]==2:c,i=q[m],r[m];break
 r=[d*[0]for _ in a]
 for x in T:r[i+x][c:c+3]=a[i+x][c:c+3]
 for f,u in((x,y)for x in E for y in E if x|y):
  h=c+f;s=i+u
  m=next((t for k in T for y in T if 0<=h+y<d and 0<=s+k<o and(t:=a[s+k][h+y])),0)
  if m:
   h=c;s=i
   while 1:
    h+=f;s+=u
    if-3<h<d and-3<s<o:
     for k in T:
      for y in T:
       if a[i+k][c+y]:
        v,l=h+y,s+k
        if 0<=v<d and 0<=l<o:r[l][v]=m
    else:break
 return r