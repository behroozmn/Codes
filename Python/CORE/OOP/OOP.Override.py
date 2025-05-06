class Animal:
    def makeSound(self): raise NotImplementedError # بدنه کلاس را در زیر کلاس باید تعریف کنیم وگرنه به ارور برخورد خواهیم کرد

class Dog(Animal):
    def makeSound(self):
        return "cat is making sound"

class Worm(Animal):
    def makeSound(self):
        return "worm does not make any sound"


dog = Dog()
worm = Worm()

print(dog.makeSound())
print(worm.makeSound())