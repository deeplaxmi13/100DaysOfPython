#Type Error

# num_char = len(input("what is your name?"))
# print("Your name has"+num_char+"characters")

# This will give error as a string cannot be concatenated with numbers

#to get the datatype of the var that we are trying to concatenate

#Type Checking

from typing import Type


num_char = len(input("what is your name?"))
print(type(num_char))
#or
print(type(input("what is your name?"))) #gives answer as string
print(type(len(input("what is your name?")))) #gives answer as int


#TypeConversion

number_char = len(input("what is your name?"))
new_number_char = str(number_char)
print("your name has "+new_number_char+" characters")

#or
print("your name has "+str(new_number_char)+" characters.") #one liner



a= 123
type(a)
print(str(a))
print(float(a))



