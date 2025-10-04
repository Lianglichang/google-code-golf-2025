def p(j):
 A=sum(j,[])
 c=[k for k in sorted(set(A),key=A.count,reverse=True)[:3]if k>0][-1]
 j=[k for k in j if c in k]
 E=[i for k in j for i,x in enumerate(k)if x==c]
 return[k[min(E):max(E)+1]for k in j]