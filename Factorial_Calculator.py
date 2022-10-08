# A program to calculate the factorial of first ten numbers (1-10)


def factorial(x):                   #function definition
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)
    
x = 1
while x < 11:
    print("Factorial of ", x, " is: ", factorial(x))            #function call
    x += 1
