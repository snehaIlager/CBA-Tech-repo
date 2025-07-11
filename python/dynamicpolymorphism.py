#dynamic typing (duck typing)

class Cat:
    def sound(self):
        print('cat meow')

class Dog:
    def sound(self):
        print('dog bark')

def do_sound(animal):
    animal.sound()

do_sound(Cat())
do_sound(Dog())