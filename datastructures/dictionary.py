about = {"Name": "Avol", "Age": 32, "Address": "Bangalore"}  # called dictionary key value pairs.

print(type(about))

# access keys.

# returns all keys as dict_keys (Note: dict_keys is not a list, index access may result type error).
keys = about.keys()
print(type(keys))
print(keys)  # keys[0] result type error dict_keys does not support indexing.

# access values.

# returns all values as dict_values (Note: dict_values is not a list, index access may result type error.)
values = about.values()
print(values)  # values[0] result type error dict_values does not support indexing.

# access through keys.
print("Name is : ", about.get("Name"))  # if no key matches, it returns None object which is null in python.

# iterate over dict.
for key in about.keys():
    print(about.get(key))

# change value in dict.
about["Name"] = "Srilekha"

print(about)

# delete by key.
del about["Address"]

print(about)

items = about.items()  # returns list of tuples type of dict_items.
print(items) # converting mutable dict into immutable tuple.

a = dict(one=1, two=2, three=3)  # dict is a class.
print(a)


