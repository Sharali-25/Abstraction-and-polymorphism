from abc import ABC,abstractmethod
class Animal(ABC):

    def move(self):
        pass

class human(Animal):
    def move(self):
        print("I can walk and run")

class snake(Animal):
    def move(self):
        print("I can crawl")

class dog(Animal):
    def move(self):
        print("I can bark")

class lion(Animal):
    def move(self):
        print("I can roar")

r=human()
r.move()

s=snake()
s.move()

k=dog()
k.move()

l=lion()
l.move()
