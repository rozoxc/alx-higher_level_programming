#!/usr/bin/python3
import calculator_1
a = 10
b = 5
add1 = calculator_1.add(a, b)
su = calculator_1.sub(a, b)
dev = calculator_1.div(a, b)
mult = calculator_1.mul(a, b)
print("{:d} + {:d} = {:d} ".format(a, b, add1))
print("{:d} - {:d} = {:d} ".format(a, b, su))
print("{:d} * {:d} = {:d} ".format(a, b, mult))
print("{:d} / {:d} = {:d} ".format(a, b, dev))
