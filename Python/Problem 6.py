# The sum of the squares of the first ten natural numbers is,

# 1^2+2^2+...+10^2=385
# The square of the sum of the first ten natural numbers is,

# (1+2+...+10)^2=55^2=3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the 


square_sum = 0
summed = 0

for i in range(1,101):
    square_sum += (i**2)

print(square_sum)

for j in range(1,101):
    summed += j

print(summed)
sum_square = (summed**2)
print(sum_square)
print("The answer is:",sum_square - square_sum)
