import math

def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	elif x > 0:
		return x
	else:
		return -x

def quadratic(a, b, c):
	if not (isinstance(a,(int)) and isinstance(b,(int)) and isinstance(c,(int))):
		raise TypeError('bad operand type')
	else:
		tmp = b**2-4*a*c
		if tmp < 0:
			return "no roots"
		else:
			delta = math.sqrt(tmp)
			return (((-b+delta)/(2*a)),((-b-delta)/(2*a)))