def p(j):
 r=range(9);c=[[0]*9 for _ in r];E=[(y,x,j[y][x])for y in r for x in r if j[y][x]]
 for y,x,l in E:
  for t in r:c[y][t]=c[t][x]=l
 c[E[0][0]][E[1][1]]=c[E[1][0]][E[0][1]]=2;return c