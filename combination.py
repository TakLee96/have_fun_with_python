def e(x):
    if x in (1,2):
        return x-1
    else:
        return (x-1)*e(x-1)+e(x-2)

def p(x):
    if x == 2:
        return 1/2
    else:
        total = 0
        for i in range(2,x):
            total += p(x-i+1)
        return (total+1)/x
