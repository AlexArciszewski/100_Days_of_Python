import math

def is_prime(num:int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


print(is_prime(3))