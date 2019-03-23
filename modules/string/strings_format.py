# string.format usage. format string should contains {} , and literal positional based formatting.
print("Hello, Mr. {}, welcome to {}".format("Lova", "Python"))
# index based formatting.
print("Hello, Mr. {1} welcome to {0}".format("Python", "Lova"))

name = "Lova"
print("Hello, Mr.  {} welcome".format(name))

# named arguments.
print("Hello, Mr. {name} ".format(name='Lova'))

nameTuple = ("Lova", len("Lova"))  # tupple in python.
print("Hello, Mr. {0[0]} and your name contains {0[1]} letters".format(nameTuple))

print('{:,}'.format(1234567890))

print('{:+f}; {:+f}'.format(3.14, -3.14))

print('{:<30}'.format('left aligned'))   # aligned by 30 empty chars to left.
print('{:>30}'.format('right aligned'))  # aligned by 30 empty chars to right.
print('{:^30}'.format('center aligned'))  # aligned by 30 empty chars on both the sides.
print('{:*^30}'.format('center aligned'))  # aligned by 30 * chars on both the sides.

print('{:0=10}'.format(12))  # prepended 10 0's.

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))

c = 3-5j
print('The complex number {0} is formed from the real part {0.real} and the imaginary part {0.imag}.'.format(c))
