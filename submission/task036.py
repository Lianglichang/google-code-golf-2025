def p(d,e=enumerate):
 x={}
 for i,a in e(d):
  for j,v in e(a):
   if v>0:x[v]=x.get(v,[])+[(i,j)]
 s=min((len(v)*(max(b for _,b in v)-min(b for _,b in v)),k)for k,v in x.items())[1];d=[[s*(y==s)for y in a]for a in d];r,c=zip(*x[s]);return[a[min(c):max(c)+1]for a in d][min(r):max(r)+1]