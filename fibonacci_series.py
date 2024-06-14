def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Number of terms in the Fibonacci sequence
num_terms = int(input("Enter the number of terms for Fibonacci sequence: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    print(fibonacci(num_terms))




'''
question 11. 1,2,3,4,5
             4,3,2,1,0

'''