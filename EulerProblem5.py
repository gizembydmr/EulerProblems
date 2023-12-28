def gcd(a, b):
    # Find the greatest common divisor using Euclid's algorithm
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # Calculate the least common multiple using the formula: LCM(a, b) = |a * b| / GCD(a, b)
    return abs(a * b) // gcd(a, b)

def smallest_multiple(limit):
    result = 1

    # Calculate the least common multiple for numbers from 1 to the specified limit
    for i in range(1, limit + 1):
        result = lcm(result, i)

    return result

# Set the limit as 20, call the function and print the result
result = smallest_multiple(20)
print(result)
