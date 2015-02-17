def choose(n, k):
	return factorial(n)/factorial(n-k)/factorial(k)

factorial = lambda k: 1 if k <= 1 else k*factorial(k-1)
