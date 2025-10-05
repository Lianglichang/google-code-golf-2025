L=len;R=range;S=sum
def p(g):
 C=S(g,[]).count(2)
 for _ in R(4):
  h=L(g);g=[*zip(*g[::-1])]
  for r in R(h):
   if g[r].count(2)==C and S(g[r])==2*C:
    for y in R(max(r,h-r)):
     if 0<=r+y<h and S(g[r+y])>0 and 2 not in g[r+y] and 0<=r-y+1<h:g[r-y+1]=g[r+y]
     elif 0<=r+y<h and 0<=r-y-1<h:g[r+y]=g[r-y-1]
 return[[c or 3 for c in r]for r in g]