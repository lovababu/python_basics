# list inbuilt class usage. list data structure is an array, can be created with [] and list class.
# Lists are mutable sequences, typically used to store collections of homogeneous items
# (where the precise degree of similarity will vary by application).

int_list = [1, 2, 3, 4, 3, 6, 7, 8]
print(type(int_list))

# no.of occurrences.
print("no.of times 3 presence: ", int_list.count(3))

for x in int_list:
    print("Element in int_list : ", x)

# index based access.
print("0th element in index: ", int_list[0])
print("1st element in index: ", int_list[1])

# sublist list[start:stop:step], start inclusive, stop exclusive and step number of skips.
print("sublist of 0 to 2nd index.: ", int_list[0:2])
print("No change in original list: ", int_list)

print("sublist from 0 to 5th index, with step 2: ", int_list[0:5:2])

# list(123) results error, since 123 int is not iterable.

list_obj = list("123")  # here "123" converted as list of ['1', '2', '3']

print("List object of 123 is : ", list_obj)

str_list = list("ABEC")  # ABEC converted as list, as strings are iterables.
print("ABEC converted as list : ", str_list)

str_list.sort()
print("Sorted list: ", str_list)

# in operator.
for x in str_list:
    print("Element : " + x)

if "A" in str_list:
    print("Yes")

if "X" not in str_list:
    print("x not in list.")

# concatenating lists. using + operator.
print("List concatinating: ", (str_list + list_obj))

sample_list = ["A", "B", 1]
print("s * 2: ", sample_list * 2)  # list * n OR n * list -> repeat the same list n time with same order.

print("Min of list: ", min(int_list))
print("Max of list: ", max(int_list))

# index of.
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 0, 3]
print("index of B", sample_list.index("B"))  # if element not present in the list it throws error.
print("Index of 2  from start: ", list_2.index(2))
print("Index of 2 after index 4 : ", list_2.index(2, 4))
print("Index of 3 after index 4 : ", list_2.index(3, 4))
print("Index of 3 from index between 4 and 10: ", list_2.index(3, 4, 10))

# delete and append.
list_1 = list("AVOLP")
print("*" * 40)
# mutable sequence operations.
list_3 = [1, 2, 3, 4, 5]
del list_3[0]  # del deletes element from specified index. del[x:y]
print("After del array: ", list_3)
del list_3[1:4]
print("After del 1to3 array: ", list_3)
del list_3[:]  # clears list.
print("After del [:] list is: ", list_3)

str_list1 = list("AVOL")
str_list1[0] = "E"
print("Replace 0th index element: ", str_list1)
str_list1[1:3] = "O"
print("Replace 1st index to 3rd index with 'O' is : ", str_list1)

str_list2 = list("ABCDEFGH")
del str_list2[0:8:2]
print("Delete [0:3:2] after list: ", str_list2)

str_list2.append("A")
print("After appending list is: ", str_list2)

str_list2.extend("CEG")
print("After extending list with CEG: ", str_list2)

str_list3 = str_list2.copy()
print("Copy of list is : ", str_list3)
d = str_list3.pop(1)  # remove the element from list and returns, default value is -1 last element will be returned.
print("Popped element from index 1 is: ", d)
print("After popping 1st index element: ", str_list3)

str_list3.remove("F")
print("After removing element from list: ", str_list3)
str_list3.reverse()
print("Reversed list: ", str_list3)

sample1 = [1, 2, 3, "AB"]  # works, but sort operation throws error.
print(sample1)

sample2 = [1, 2, 3, "B"]
print("Is sample1 and 2 equal: ",  (sample1 == sample2))








