def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers"
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

# Test the function with a number
test_number = 5  # Change this to test a different number

# Calculate the factorial of the number
fact_result = factorial(test_number)

# Print the factorial of the number
print(f"The factorial of {test_number} is: {fact_result}")
