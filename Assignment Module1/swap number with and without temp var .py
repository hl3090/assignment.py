"""
Using Temp Variable

n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))

temp = n1
n1 = n2
n2 = temp

print ("After swapping ", n1,n2)

"""

"""
Without temp Variable
"""

n1 = 5
n2 = 10

print ("Before Swapping: ",n1,n2)

n1,n2 = n2,n1

print ("After Swapping: n1 ",n1,"n2",n2)