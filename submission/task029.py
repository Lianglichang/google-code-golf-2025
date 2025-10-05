def p(g,L=len,E=enumerate):
	for B in {*sum(g,[])}:
		D,F=zip(*((d,a)for a,c in E(g)for d,f in E(c)if f==B));A=[r[min(D)+1:max(D)]for r in g[min(F):max(F)]]
		if {*A[0]}<={B}:return A[1:]
	return g