# What is the largest prime factor of the number 600851475143?

def largest_prime_factor(n):
    # Initialize the divisor
    divisor = 2

    while divisor * divisor <= n:
        # Check if the divisor divides the number without a reminder
        if n % divisor == 0:
            # If yes, divide the number and continue checking with the same divisor
            n //= divisor
        else:
            # If no, increment the divisor
            divisor += 1

    # The remaining number is the largest prime factor
    return n

# Call the function for 600851475143 and print the result
result = largest_prime_factor(600851475143)
print(result)
