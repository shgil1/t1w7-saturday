import math_ops

num1 = 15
num2 = 6

result_add = math_ops.add(num1, num2, 1, 1, 1, 1, 1, 1)
print(result_add)

result_subtract = math_ops.subtract(num2, num1)
print(result_subtract)

result_multiply = math_ops.multiply(1, 5, 6, 7)
print(result_multiply)

result_divide = math_ops.divide(2, 3)
print(result_divide)

# Another way to import
print("------------")
from math_ops import add, subtract
result_add = add(num1, num2)
print(result_add)

result_subtract = subtract(num1, num2)
print(result_subtract)

print("**************")
# Python's pre-defined modules
import math, random

num1 = math.pow(4,3)
print(num1)

num2 = math.sqrt(64)
print(num2)

randValue = random.randrange(1, 10)
print(randValue)