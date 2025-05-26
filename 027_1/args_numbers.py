


def add(n1:int, n2:int):
    return n1 + n2

print(add(1,2))

def add2(*args):
    return sum(args)


print(add2(1,2,3))

print(add2(1,2,3,4,5))