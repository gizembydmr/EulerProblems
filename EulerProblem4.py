# Find the largest palindrome made from the product of two 3-digit numbers.
def largest_palindrome_product():
    max_palindrome = 0

    # Iterate through all possible products of two 3-digit numbers
    for a in range(100, 1000):
        for b in range(a, 1000):  # To avoid duplicate products
            product = a * b

            # Check if the product is a palindrome (forward and reverse strings
            # should be equal) and larger than the current max_palindrome
            if str(product) == str(product)[::-1] and product > max_palindrome:
                max_palindrome = product

    return max_palindrome

# Call the function and print the result
result = largest_palindrome_product()
print(result)
