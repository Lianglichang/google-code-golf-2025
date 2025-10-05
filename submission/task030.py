def p(g,E=enumerate):
	x,y,b=[],[],[];t=[x,y];s=[]
	for a in g:
		for c,v in E(a):
			if v in(2,4):t[v//2-1]+=c,;a[c]=0
			elif v==1:b+=c,;s+=[(a,c)]
	for a,c in s:a[c+min(y)-min(b)]=4;a[c+min(x)-min(b)]=2
	return g