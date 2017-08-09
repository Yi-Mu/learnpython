#-*- coding: utf-8 -*-

def quadratic(a,b,c):
	import math
	if not (isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float))):
		raise TypeError('bad operand type')
	t=b**2-4*a*c;
	if t>0:
		s1=(-b+math.sqrt(t))/2/a
		s2=(-b-math.sqrt(t))/2/a
		return s1,s2
	elif t==0:
		return -b/2/a,-b/2/a
	else:
		r=-b/2/a
		v=math.sqrt(abs(t))
		return '%.2f+%.2fi'%(r,v),'%.2f-%.2fi'%(r,v)
