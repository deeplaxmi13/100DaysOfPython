'''
TODO 1: Create a function called greet()
        Write 3 print statements inside the function
        Call the greet() function and run your code
'''

#One parameter
def greet(name):
    print(f"Hello {name}")
    print(f"How do you do {name} ?")
    print("Isn't the weather nice today?")


def greet_twoParam(name, location):
    print(f"Hello {name}")
    print(f"Isn't the weather at {location} nice today?")

def number_function(a,b,c):
    d = a+b+c
    print(d)
 
name = input("Enter your name: ")
location = input("Enter your location: ")
greet(name)
print("\n\n")
greet_twoParam(name,location)
print("\n\n")
number_function(10,20,30)