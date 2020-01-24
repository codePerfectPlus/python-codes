#parent Class
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def speak(self):
        print(f"I am {self.name} and I am {self.age} Old.")
    
#child class
class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        self.type = "dog"

#call child class
t = Dog("tyson", 5)
t.speak()
    
    