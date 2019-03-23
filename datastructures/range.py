#  The range type represents an immutable sequence of numbers and is commonly used for looping
#  a specific number of times in for loops.
x = range(1, 10)
print("Range x is: ", x)

for n in x:
    print("Value is: ", n)

y = range(1, 10)

print("is x == y : ", (x == y))

z = range(0, -10, -1)
print("Negative tuple: ", list(z))
