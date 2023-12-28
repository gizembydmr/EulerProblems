# There exists exactly one Pythagorean triplet for which a+b+c=1000
# Find the product abc.

def find_pythagorean_triplet(target_sum):
    # Iterate through possible values of 'a'
    for a in range(1, target_sum):
        # Iterate through possible values of 'b'
        for b in range(a, target_sum - a):
            # Calculate 'c' based on the Pythagorean theorem
            c = target_sum - a - b
            # Check if it's a Pythagorean triplet
            if a**2 + b**2 == c**2:
                # Return the product 'abc'
                return a * b * c

# Set the target sum as specified in the problem
target_sum = 1000

# Call the function and print the result
result = find_pythagorean_triplet(target_sum)
print(result)
