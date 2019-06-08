# class is the keyword in python to declare class template.
import time

class Account:
    number = 1234567
    name = "Avol"
    branch = "Channasandra"
    code = "ICICI12345"


acct = Account()  # instantiating/creating object for class Account.
print(acct.number)  # accessing class variables.
acct.branch = "Whitefield"  # changing object variable data.
print(acct.branch)


# class methods. constructors, destructors and methods.


class Account1:

    def __init__(self):
        # constructor method, invoked while object being instantiated.
        print("I am in constructor.")

    def greet(self):
        print("Hello, welcome to python.")

    def __del__(self):
        # destructor method, invoked before the object is going to be destroyed.
        print("I am in destructor.")


acct_1 = Account1()  # instantiating, constructor should be invoked.
acct_1.greet()

print("---- sleeping.")
time.sleep(30)

