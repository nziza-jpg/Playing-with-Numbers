import math
# Enter 2 numbers
numberLargest = int(input("Enter Largest Number: "))
numberSmallest = int(input("Enter Smallest Number: "))

def find_lcm(a,b):
    return (a * b)//math.gcd(a,b)

lcm = find_lcm(numberLargest, numberSmallest)
print("LCM is: ", lcm)

