# What is the 10001st prime number?

def is_prime(num):
    # Check if a number is prime
    if num < 2:
        return False
    # Check divisibility up to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            # If any divisor is found, the number is not prime
            return False
        # If no divisors are found, the number is prime
    return True

def find_nth_prime(n):
    # Find the nth prime number
    primes = []
    i = 2
    # Continue until the list of primes has n elements
    while len(primes) < n:
        if is_prime(i):
            # If the current number is prime, add it to the list
            primes.append(i)
        # Move to the next number
        i += 1
    # Return the nth prime number
    return primes[-1]

# Find 10001th prime with the function and print the result
result = find_nth_prime(10001)
print(result)
