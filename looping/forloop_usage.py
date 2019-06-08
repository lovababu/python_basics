# for loop usage.

for x in (1, 2, 3):
    print("Elements in tupple : ", x)

# range(start, stop[, step], start inclusive and stop exclusive. step is start + step next value.

for x in range(0, 5):  # prints from 0 to 4.
    print("Range elements: ", x)

for x in range(10):  # prints from 0 to 9.
    print("Range upto 10: ", x)

for x in range(0, 10, 2):
    print("Range upto 10 with step 2: ", x)

# list comprehensions, in python it is possible to write inline logic while looping over elements..
even_numbers = [x for x in range(1, 100) if x % 2 == 0]
print("Event Numbers: ", even_numbers)







