class BMW:
    def type(self):
        print("BMW is a luxury car")

    def speed(self):
        print("BMW speed is 250 km/h")

class Ferrari:
    def type(self):
        print("Ferrari is a sports car")

    def speed(self):
        print("Ferrari speed is 300 km/h")

obj1=BMW()
obj2=Ferrari()

for i in (obj1,obj2):
    i.type()
    i.speed()
    print()