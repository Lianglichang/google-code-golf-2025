def p(u):
 s=range;S=sum;r=(len(u)-1)//2
 if r==1:
  d=[u[0][0],u[0][2],u[2][0],u[2][2]]
  for m in d:
   if d.count(m)==1:return[[m]]
 for t,h in((0,0),(0,r+1),(r+1,0),(r+1,r+1)):
  l=[[u[t+i][h+j]for j in s(r)]for i in s(r)]
  if len({*S(l,[])})>1:return l