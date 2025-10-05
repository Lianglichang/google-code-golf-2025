def p(g,E=enumerate):
 H=len(g[0]);A=[-1]+[a for a,b in E(zip(*g))if not any(b)]+[H];B=[[c[x+1:y]for c in g]for x,y in zip(A,A[1:])if x+1<y];C=B[:1]
 for D in B[1:]:
  I=C[-1];J=next((i for i,a in E(I)if a and a[-1]==5),0);K=next((i for i,a in E(D)if a and a[0]==5),0);F=J-K;G=[[0]*len(D[0])]*3;C+=[(G+D+G)[3-F:6-F]]
 L=[next((a for b in a for a in b if a>0!=5!=a),0)for a in B];M=[[[a==5and b or a for a in a]for a in a]for a,b in zip(C,L)];return[sum(a,[])for a in zip(*M)]