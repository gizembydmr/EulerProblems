# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

def sum_of_squares(n):
    # Calculate the sum of the squares of the first n natural numbers
    return sum(i**2 for i in range(1, n + 1))

def square_of_sum(n):
    # Calculate the square of the sum of the first n natural numbers
    return sum(range(1, n + 1))**2

def difference_of_squares(n):
    # Calculate the difference between the sum of squares and square of sum
    return square_of_sum(n) - sum_of_squares(n)

# Call the function
result = difference_of_squares(100)
# Print the result
print(result)
