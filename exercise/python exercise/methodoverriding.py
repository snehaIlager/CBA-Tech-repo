class Animal:
    def speak(self):
      print("Animal Speaks")

class Dog(Animal):
   def speak(self):
      print("Dog Barks")

domesticanimal = Animal()
puppy = Dog()

domesticanimal.speak()  # Output: Animal Speaks
puppy.speak()  # Output: Dog Barks