import math

# Program: Distance Between Two Points Calculator
# Purpose: Calculate Euclidean distance using Python's math library and user input.

# 1. Input: Prompt user for coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# 2. Process: Calculate Euclidean distance using pow() and sqrt()
# Formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# 3. Output: Display the result formatted to 2 decimal places
print(f"\nThe distance between the two points is: {distance:.2f}")

'''
--- REFLECTION ---
Using a library is more practical because it provides pre-tested, highly optimized functions like 
math.sqrt() and math.pow(), saving time and preventing errors. Without the math library, calculating 
square roots would require implementing complex iterative algorithms from scratch, making the code 
much longer and harder to write. The library simplifies the program so I can focus on solving the 
problem rather than rewriting fundamental mathematical operations.
'''