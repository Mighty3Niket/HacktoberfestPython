def fibonacci(n):
    # Check if n is less than 0
    if n < 0:
        print("Input should be a non-negative integer")
        return None

    # Initialize the first two terms of the sequence
    fibonacci_sequence = [0, 1]

    # Generate the Fibonacci sequence up to the nth term
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence

# Number of terms in the Fibonacci sequence to generate
num_terms = 10  # Change this to generate a different number of terms

# Generate the Fibonacci sequence
fib_sequence = fibonacci(num_terms)

# Print the generated Fibonacci sequence
print("Fibonacci sequence up to {} terms:".format(num_terms))
print(fib_sequence)
