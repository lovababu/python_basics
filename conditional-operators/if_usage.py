print("using if else clauses in python.")

# if [condition]:
#   code

# in pthong boolean values True and False are case sensitive. true/false incorrect.
if True:
    print("If block")

if False:
    print("If block")
else:
    print("Else block")

# else if usage.
x = 11
if x % 2 == 0:
    print("X is divisible by 2.")
elif x % 3 == 0:
    print("X is divisible by 3.")
else:
    print("X is neither divisible by 2 nor 3.")

# multiple conditions.

y = 6
if y > 0 and y <= 10:
    print("Y is in between 0 and 10")

if 0 < y <= 10:
    print("Y is in between 0 and 10")

# and/or/nor

if not False:
    print("If block. not(False) = True")


# switch case implementation simulation in python, python doesn't have switch implementation inbuilt.

def week(i):
    switcher = {
        1: "S",
        2: "M",
        3: "T",
        4: "W",
        5: "T",
        6: "F",
        7: "S"
    }
    return switcher.get(i)

ret = week(2)

print("Return value is : ", ret)




