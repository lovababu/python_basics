sample_set = set()
sample_set.add("Abc")
sample_set.add("Xyz")
sample_set.add("Abc")
print(sample_set)

sample_set.remove("Xyz")  # if the element not found in set, throws type error.
print(sample_set)

pop = sample_set.pop()  # remove the arbitrary element and returns.
print(pop)
# pop = sample_set.pop()  # error as set is empty.

# sample_set.remove() removes all elements.


