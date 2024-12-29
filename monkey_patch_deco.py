# Add_fun is a funtion that accepts a class and adds a method to it while runtime and returns the class

def add_func(cls):

    cls.speak = lambda self, message : print(message)
    return cls

@add_func
class Dog:

    def __init__ (self, name):
        self.name = name
    

obj = Dog("Andreson")
obj.speak("Hi i am andreson")