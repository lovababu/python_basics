# var args, and default arguement values.


def about(name, age, address):
    print("Hello, this is {} and am {} years old, living in {}".format(name, age, address))


about("Avol", 32, "Bangalore")   # error missing 1 required positional argument if don't pass all arguments.

# invoke function by specifying argument values with name, order no matter.

about(name="Srilekha", address="Tatipaka", age=14)

print("*" * 10 + "Default parameter values " + "*" * 10)


def about_1(name, age, address="Bangalore"):   # default parameter must be the last parameter.
    print("Hello, this is {} and am {} years old, living in {}".format(name, age, address))


about_1("Avol", 32)  # still works, as we declared address parameter with default value.

print("*" * 10 + " Packing & unpacking" + "*" * 10)

numbers = [1, 2, 3, 4, 5]
print(numbers)   # prints [1, 2, 3, 4, 5], how to print 1 2 3 4 5
print(*numbers)  # prints 1 2 3 4 5, unpacking.
print("abc")   # prints abc, how to print a b c
print(*"abc")  # unpacking iterables.


def add(*nums):
    tot = 0
    for x in nums:
        tot = tot + x

    print("Total is : ", tot)


add(1, 2, 3, 4, 5)  # pack, and pass to function add.


def about_3(name, age, address):
    print("Hello, {} you are {} old and living in {}".format(name, age, address))


about_dict = {"name": "Avol", "age": 32, "address": "Karnataka"}
about_3(**about_dict)  # unpacking dictionary and passing as parameters.


def about_4(**kwargs):
    for key, value in kwargs.items():
        print("{} = {}".format(key, value))


about_4(lova="male", satya="female")  # packing.

#  * represents args, **kwargs represents keyword args.








