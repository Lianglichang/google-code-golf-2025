def p(g,E=enumerate):
 w=[(i,j)for i,r in E(g)for j,v in E(r)if v>0];R,C=zip(*w);a,b,c,d=min(C),max(C),min(R),max(R);b-= (b-a)//2;d-= (d-c)//2;return[r[a:b]for r in g[c:d]]