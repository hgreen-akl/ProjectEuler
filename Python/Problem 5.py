# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import numpy as np

number = 2519
goal = np.ones(20)
y = np.zeros(20)
np.array_equal(goal,y)


while np.array_equal(goal,y) == False:
    for i in range(1,21):
        if number % i != 0:
            number +=1
            y = np.zeros(20)
            continue
        else:
            y[i-1] = 1

print(number)
