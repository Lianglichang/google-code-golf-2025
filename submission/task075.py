def p(j):
 r=range;c=[*map(list,j)];e=[y[:3]for y in j[:3]]
 for k in r(9):
  for w in r(4,13):
   if j[k][w]==1:
    for l in-1,0,1:
     for m in-1,0,1:
      if 0<=k+l<9and 4<=w+m<13:c[k+l][w+m]=e[l+1][m+1]
 return c