def p(j):
 c=len(j)-1
 for a in j[1:]:
  if a[-1]==5:
   for l in range(c):
    if j[0][l]==5:a[l]=2
 return j