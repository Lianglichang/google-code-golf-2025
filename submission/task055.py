def p(j,A=range):
 c,E=len(j),len(j[0]);k=[r[:]for r in j];W,l=[i for i in A(c)if min(j[i])>7];J,a=[i for i in A(E)if min(r[i]for r in j)>7]
 for C in A(c):
  for e in A(E):
   if not k[C][e]:k[C][e]=(W<C<l)*((e<J)*4+(e>a)*3+(J<e<a)*6)+(J<e<a)*((C<W)*2+(C>l)*1)
 return k