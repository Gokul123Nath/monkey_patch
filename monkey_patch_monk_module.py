class A:

    def func(self):
        print("Func () is called")

def monkey_function(self):
    print("Monkey func is called")

# Assign monkey function to be executed instead of func of the class
# Technically replacing the address of the func with monkey_function 

A.func = monkey_function

# Create object

obj = A()

# Calling the func whose address got replaced with monkey_function
obj.func()

