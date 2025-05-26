#args daja tuple UNLIMITED POSITIONAL ARGUMENTS
def add(*args:int) -> int:
    return sum(args)



print(add(2,3))
#5

def add2(*args: int) -> int:
    if not all(isinstance(arg, int) for arg in args):
        raise TypeError("Wszystkie argumenty muszą być typu int")
    return sum(args)

print(add2(1,2,3))
#6
#print(add2(1,2,"3"))
#TypeError: Wszystkie argumenty muszą być typu int

#KEY WORD ARGUMENTS
def calculate(**kwargs:int) -> dict:
    print(kwargs)


calculate(add=3, multiply=5)
calculate(kot=1,pies=2)


def my_func(**kwargs):
    print(kwargs)

d = {'a': 1, 'b': 2}
my_func(**d)


def calculate(n, **kwargs):
    print(kwargs)
    n+=kwargs["add"]
    n*=kwargs['multiply']
    print(n)

calculate(2,add=3, multiply=5)

class Car:

    def __init__(self,**kw):
        self.make = kw['make']
        self.model =kw['model']

my_car = Car(make="Nissan", model="GTR")
print(my_car)
print(my_car.make)
print(my_car.model) #jak to usuniemy będzie blad bo zabraknie klucza

# <__main__.Car object at 0x0000023BBB167A00>
# Nissan
# GTR

#jak użyjemy w konstruktorze metod get zamaist kwadtratowych nawiasów to da nam none zamiast błędu jak nie znajdzie arguentu


class Car:

    def __init__(self,**kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.colour =kw.get("colour")

my_car = Car(make="Nissan")
print(my_car)
print(my_car.make)
print(my_car.model)
print(my_car.colour)


# <__main__.Car object at 0x0000023BBB167970>
# Nissan
# None

def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)

bar(1, 2)
#1 2 yes please! 0


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)
#4 (7, 3, 0) {'x': 10, 'y': 64}