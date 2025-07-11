# program to find HCF/GCD

# Enter 2 numbers
numberLargest = int(input("Enter Largest Number: "))
numberSmallest = int(input("Enter Smallest Number: "))

# Using Eucliden Algorithms
while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("HCF is: ", numberLargest)