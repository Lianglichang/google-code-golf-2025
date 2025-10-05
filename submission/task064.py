L=len;R=range;S=sum
def p(g):
 h,w=L(g),L(g[0]);f=S(g,[]);a,b,c=sorted([[f.count(k),k]for k in set(f)])
 for r in R(h):
  for d in R(w):
   if g[r][d]==b[1]:
    for y,x in((0,1),(0,-1),(1,0),(-1,0)):
     if 0<=r+y<h and 0<=d+x<w and g[r+y][d+x]==c[1]:
      for z in R(20):
       if 0<=r+y*z<h and 0<=d+x*z<w and g[r+y*z][d+x*z]==a[1]:g[r][d]=0
 for _ in R(4):
  g=[*map(list,zip(*g[::-1]))];h,w=L(g),L(g[0])
  for r in R(h):
   if g[r].count(0):
    x=0
    for d in R(w):
     if g[r][d]==a[1]and g[r].index(0)>d:x=1
     if x:
      if g[r][d]==c[1]:g[r][d]=a[1]
      elif g[r][d]==0:x=0
 return[[v or b[1]for v in r]for r in g]