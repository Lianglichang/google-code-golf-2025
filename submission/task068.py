def p(j):
 from collections import Counter as C
 w=next(k for k,v in C(x for r in j for x in r if x).items()if v==1);R=range(10)
 l,m=next((i,k)for i in R for k in R if j[i][k]==w)
 return[[w if not(i-l or k-m)else 2 if abs(i-l)<2 and abs(k-m)<2 else 0 for k in R]for i in R]