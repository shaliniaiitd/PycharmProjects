# Python program to demonstrate
# Swapping of two variables

x = 17
y = 50

# Swapping using xor
x = x ^ y
y = x ^ y
x = x ^ y

print("Value of x:", x)
print("Value of y:", y)
