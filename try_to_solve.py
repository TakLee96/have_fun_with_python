from math import e, log

def s(m):
	left = m*log(m/0.9)+(1-m)*log((1-m)/0.1)
	right = log(10/9)/100
	return left - right
