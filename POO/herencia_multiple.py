

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating like an animal')

class Flyable:

    def fly(self):
        print(f'{self.name} is flying like a bird')

    def eat(self):
        print(f'{self.name} is eating like a a bird')

class Walkable:

    def walk(self):
        print(f'{self.name} is walking like an animal')

class Bird(Flyable, Walkable, Animal):
    def __init__(self, name):
        super().__init__(name)

bird = Bird('Sparrow')
bird.fly()
bird.walk()
bird.eat()

    







