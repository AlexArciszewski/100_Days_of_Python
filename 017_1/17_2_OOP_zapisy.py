#zapisy oop


class Car:
    def __init__(self,seats: int, wheels: int):
        self.seats = seats
        self.wheels = wheels

def main():
    my_car= Car(4,4)
    print(my_car)

if __name__ == "__main__":
    main()

class AwdCar:
    def __init__(self,wheels: int, seats: int):
        self.seats = seats
        self.wheels = wheels
my_jeep = AwdCar(5,4)
print(my_jeep.seats)

class FwdCar:
    def __init__(self,seats):
       self.seats = seats

my_opel = FwdCar(5)
my_opel.seats = 5
print(my_opel.seats)
