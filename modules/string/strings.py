import string

sample = "Hello, World.!"
print("Sample string is : ", sample)
print("count(world) is ", sample.count("world"))  # returns how many times string found.
print("count(o) is ", sample.count("o"))

print('find("e")', sample.find("e"))  # returns the index of search string.
print(string.ascii_letters)  # prints a-zA-Z
print(string.hexdigits)  # prints 0-9a-fA-F

# find string length.
print("Length of string is : ", len(sample))

# slicing.
print("0th index char: ", sample[0])
print("0th to 5th index slicing: ", sample[0:5])
print("0th to 5th index slicing by jumping 2chars: ", sample[0:5:2])
print("from index 7th to end: ", sample[7::])
print("from index 7th to end by jumping 2chars: ", sample[7::2])

# printf style formatting.
print("Hello, %s , welcome to %d miles marathon" % ("Lova", 5))
map_s= {"Name": "Lovababu", "age": 32}
print("Hello, %(Name)s your are %(age)03d years old" % map_s)
