def scan(f, lst, start):
    accumulated = start
    def closure(item):
        nonlocal accumulated
        accumulated = f(accumulated, item)
        return accumulated
    return map(lst, closure)
