import math

# Numbers.
print("****************** Numbers ********************")
# gives 2
floor = math.floor(2.4)
print("Floor (2.4) is ", floor)

# gives 3
ceil = math.ceil(2.4)
print("Ceil (2.4) is ", ceil)

# copysign(x, y) - return a float of x with sign y.
copy_sign = math.copysign(2, -3)
print("copysign(2, -3) is ", copy_sign)

# fabs(-2.434) returns 2.434, absolute float value. |-2.434|=2.434, |-3*6|=18
f_abs = math.fabs(2.434)
print("fabs(2.4) is ", f_abs)

# factorial(3) - 3*2*1=6
fact = math.factorial(3)
print("factorial(3) is ", fact)

#  fmod(5.2, 3.0) is 2.2
f_mod = math.fmod(5.2, 3.0)
print("fmoc(5.2, 3.0) is ", f_mod)

# frexp(x)
f_rexp = math.frexp(4)
print("frexp(4) is ", f_rexp)

# fsum(iterable)
f_sum = math.fsum([2, 3, 4])
print("fsum([2,3,4]) is ", f_sum)

# isfinite()
flag = math.isfinite(3)
print("isfinite(3) is ", flag)

# isfinite()
flag = math.isfinite(math.inf)
print("isfinite(math.inf) is ", flag)

# isinf(x)
flag = math.isinf(4)
print("isinf(4) is ", flag)

flag = math.isinf(math.inf)
print("isinf(math.inf) is ", flag)

# isnan()
flag = math.isnan(4)
print("isnan(4) is ", flag)

x = float('nan')
flag = math.isnan(x)
print("isnan('nan')", flag)

# ldexp(x, i) -> x * 2**i
l_dexp = math.ldexp(3, 2)
print("ldexp(3, 2) is ", l_dexp)

# modf(x) -> 0.0, 5.0
mod_f = math.modf(5)
print("modf(4) is ", mod_f)

# trunc(float) > 5
trunc = math.trunc(5.2)
print("trunc(5.2) is ", trunc)

print("*" * 15 + " Power and logarithmic " + "*" * 15)   # "*" * 15 results 15 star symbols.

# gives 9.0, 3 power of 2.
power = math.pow(3, 2)
print("Pow(3, 2) is ", power)

# exp(x) Return e**x
exp_x = math.exp(4)
print("exp(4) is ", exp_x)

# expm1(x) Returns e**x - 1
exp_x1 = math.expm1(4)
print("expm1(4) is ", exp_x1)

# log(x[, base]) > log of 5 with base e.
log_5 = math.log(5)
print("log(5) is ", log_5)

log_5b2 = math.log(5, 2)
print("log(5, 2) is ", log_5b2)
print("exp(log_5b2, 2) is ", math.pow(2, log_5b2))

# log1p(x) > 1+x base e.
log1p_x = math.log1p(5)
print("log1p(5) is ", log1p_x)

# log2(5) > log of 5 with base 2.
log2 = math.log2(5)
print("log2(5) is ", log2)


print("***************** Angular Conversions ********************** ")

#  ##############################################
# Angular conversion.
# Py(22/7) radians = 180 degrees.
radian = 57.2985  # 1 Radian = 57.2958 degrees.
deg = math.degrees(4)
print("degree(4) is ", deg)
print("4 * radian is ", (4 * radian))

# the angle made when we take the radius and wrap it round the circle.
# https://www.mathsisfun.com/geometry/radians.html

rad = math.radians(4)
print("radians(4) is ", rad)
print("radian/4 is ")

# radian to degree --> (N-radians * 180)/Py   (where Py is 22/7)
# degree to radian --> (N-radians * Py)/180   (where Py is 22/7)

print("*" * 15 + " Trigonometric " + "*" * 15)

# cos(5)
cos = math.cos(5)
print("cos(5) is ", cos)
