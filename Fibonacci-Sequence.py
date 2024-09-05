def fibonacci(n):

    # Initialize first two numbers of the sequence
    
    x, y = 0, 1
    
    # Loop to print the Fibonacci sequence
    for i in range(n):
        print(x, end=' ')
        x, y = y, x + y

# Input: number of terms
terms = int(input("Enter the number of terms: "))

# Output: Fibonacci sequence
if terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci sequence up to {terms} terms:")
    fibonacci(terms)
