# typical python function, def is the keyword to declare function.
def say_hello():
    print("Hello, welcome to python.")


say_hello()  # invoking function.


def say_hello(name):   # method with parameters.
    print("Hello, {}! welcome to python world.".format(name))


say_hello("Srilekha")

print("*" * 50)

global_num = 10


def fun1():
    global_num = 50  # local scope, do not effect global scope variable.
    print("In Fun1, global_num is: ", global_num)


def fun2():
    global global_num   # way to refer global variable from function.
    global_num = global_num + 50
    print("In Fun2, global_num is : ", global_num)


fun1()
print("In main global_num is : ", global_num)
fun2()
print("In main global_num is : ", global_num)


arr = [1, 2, 3]


def fun_arr():
    arr[0] = 4  # collections and custom object can be directly referenced from function.


fun_arr()
print("Array : ", arr)
