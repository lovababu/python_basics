# int() float() complex()
# complex() type is having real and imaginary part.

x = int(10)
print("Type of x is : ", type(x))
print("Bit length of x is : ", x.bit_length())
print("Byte array of x is : ", x.to_bytes(2, byteorder='big'))   # byte orders little or big.
print("From bytes to integer: ", int.from_bytes(b'\x00\n', byteorder='big')) # from byte array to int.

y = float(5.90)
print("Type of y is : ", type(y))
z = complex(5j)
print("Type of z is : ", type(z))
print("Real part of z is : ", z.real)
print("Imaginary part of z is: ", z.imag)
c = complex(z.imag + 5j)  # remove see and observe output.
print("C value is : ", c)
print("C real part : ", c.real)
print("C imaginary part: ", c.imag)
print("C conjugate : ", c.conjugate())

print("Floored quotient: ", (8 // 3))

print("Divmod of 7, 2 is: ", divmod(7, 2))
print("0 to the power of 0 is: ", pow(0, 0))
