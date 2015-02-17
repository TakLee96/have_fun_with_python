# total = 0

# for i in range(1, 14):
# 	num = 3*i*i/(52-i)
# 	print("adding", num)
# 	total += num

# print("total", total)

def a(i):
	return 3*i/(52-i)

def b(i):
	if i == 1:
		return a(1)
	else:	
		return (1-sb(i-1))*a(i)

def sb(i):
	total = 0
	for j in range(1, i+1):
		total += b(j)
	return total

total = 0
for i in range(1, 14):
	total += b(i) * i
print(total)



lst = [[1, 2], [3, 4]]

doubled = [[col*2 for col in row] for row in lst]