# Tuples are immutable sequences, typically used to store collections of heterogeneous data
# (such as the 2-tuples produced by the enumerate() built-in).
# class tuple([iterable])

# ways to create tuple
t1 = ()  # empty tuple.
t2 = (2,)  # single item tuple
t3 = (1, 2, 3)  # tuple with three values.
print("Tuple t3 is : ", t3)
t4 = tuple()  # using inbuilt class.
print("Tuple t4 is : ", t4)
t5 = tuple("abc")
print("Tuple t5 is : ", t5)
print("comparing tuples: ", (t1 == t4))

#  https://docs.python.org/3.3/library/stdtypes.html#typesseq-common

tuple_1 = (1, 2, "A")
print("Tuple with different data type elements: ", tuple_1)

for x in tuple_1:
    print("Tuple element: ", x)

if 2 in tuple_1:
    print("2 element present in tuple_1.")

if "B" not in tuple_1:
    print("B element not present in tuple_1.")

tuple_1 = tuple_1 + tuple("B")

print("After concatenations with B is: ", tuple_1)
print("Length of tuple: ", len(tuple_1))


def ret_tuple():
    return 12, 13


x, y = ret_tuple()

print("X, Y is : ", x, y)

