number=int(input("enter your number "))

def factorial(number):
    if(number==0):
        return 1
    else:
        return number*factorial(number-1)

print(f'factorial of {number} is',factorial(number))