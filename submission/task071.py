def p(g):
 R=range;H,W=len(g),len(g[0]);C={}
 def q(v):
  if not v:return 0
  a,b=zip(*v);return len(v)==(max(a)-min(a)+1)*(max(b)-min(b)+1)
 for r in R(H):
  for c in R(W):
   v=g[r][c]
   if v:C.setdefault(v,[]).append((r,c))
 if not C:return[[0]*W for _ in R(H)]
 b=max((k for k in C if q(C[k])),key=lambda k:len(C[k]),default=None)
 x=[k for k in C if k!=b and not q(C[k])]or[k for k in C if k!=b]
 r=max(x,key=lambda k:len(C[k]));s=C[r];S=set(s);B=set(C[b])if b else set()
 t=max(R(2*W-1),key=lambda t:sum(1 for i,j in s if 0<=(m:=t-j)<W and((i,m)in S or(i,m)in B)),default=min(j for i,j in s)+max(j for i,j in s))
 o=[[0]*W for _ in R(H)]
 for i,j in s:o[i][j]=r
 if b:
  for i,j in C[b]:
   if 0<=(m:=t-j)<W and(i,m)in S:o[i][j]=r
 return o