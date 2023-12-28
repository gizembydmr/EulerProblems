# Find the sum of all the multiples of 3 or 5 below 1000.

# initialize the sum
sum = 0

# if the number is a multiple of 3 or 5, add it to the sum
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:

        sum = sum + i

# Print the final sum
print(sum)
