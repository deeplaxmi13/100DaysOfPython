'''
You are going to write a program that automatically prints the solution to that FizzBuzz game.

Your program should print each number from 1 to 100 in turn.

When the number is divisible by 3 then it should print "Fizz" instead of the number

When the number is divisible by 5 then it should print "Buzz" instead of the number

When the number is divisible by 3 and 5 then it should print "FizzBuzz" instead of the number
'''


for number in range(1, 101):
    if number % 3 == 0 and number % 5 ==0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)