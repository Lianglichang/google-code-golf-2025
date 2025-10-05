from collections import*
j=len;A=range
def p(c):
 k=[x for x in Counter(sum(c,[])).most_common() if x[0]][-1][0]
 J=[(a,b)for a in A(j(c))for b in A(j(c[0]))if c[a][b]==k];y,x=zip(*J);e=min(x);K=max(x);w=min(y);L=max(y);return[A[e:K+1]for A in c[w:L+1]]