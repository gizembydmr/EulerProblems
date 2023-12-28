# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued terms.

# Initialize the first two Fibonacci numbers
a, b = 1, 2

# Initialize the sum of even Fibonacci numbers
even_fibonacci_sum = 0

# while last Fibonacci number (a) do not exceed 4 million
while a <= 4000000:
    # if the current Fibonacci number is even, add it to the sum
    if a % 2 == 0:
       even_fibonacci_sum += a

    # Update Fibonacci numbers for the next iteration
    a, b = b, a + b

# Print the final sum of even Fibonacci numbers
print(even_fibonacci_sum)
