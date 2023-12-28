# Find the sum of all the primes below two million.

def is_prime(num):
    # Check if a number is prime
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(limit):
    total_sum = 0
    # Iterate through numbers below the limit
    for i in range(2, limit):
        if is_prime(i):
            # Add prime numbers to the sum
            total_sum += i
    return total_sum

# Call the function and print the result
result = sum_of_primes(2000000)
print(result)
