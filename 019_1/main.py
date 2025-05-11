def add(n1,n2):
    return n1 + n2
print(add(1,2))



def calc(a1, a2, func):
    return func(a1, a2)

print(calc(1,2, add))