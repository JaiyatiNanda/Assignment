number=int(input("enter number"))
def prime(number):
    if(number<=1):
        return False
    for i in range(2,number):
        if(number %i==0):
            return False
        return True


if(number==2):
    print("least even prime number")
elif(number%2==0):
    print("the number is even")
elif(prime(number)):
    print("prime number")
else:
    print("odd number")
