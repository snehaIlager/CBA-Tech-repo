#method overriding (Runtime polymorphism)
class Animal: #this is super class
    def eatFood(self):
        print('Animals eat food')

class Elephant(Animal):
    def eatFood(self):
        print('Elephants eat grass')

E1=Elephant()
E1.eatFood() #method overriden in elephant class ie.runtime polymorphism

#





