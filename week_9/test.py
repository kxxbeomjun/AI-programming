# from lab9_p4 import Fraction
# f1 = Fraction(2, 12)
# f2 = Fraction(1, 6)
# f2.num = 2
# print('f1:', f1) # f1:˽1/6
# print('f2:', f2) # f2:˽2/6
# f2.reduce()
# print('f2:', f2) # f2:˽1/3
# f2.adjust(3)
# print('f2:', f2) # f2:˽3/9

from lab9_p5 import Fraction

f1 = Fraction(1, 2) * Fraction(2, 3)
print('f1:', f1) # f1:˽2/6
f2 = f1 * (-2)
print('f2:', f2) # f2:˽-4/6
f3 = f2 + 3
print('f3:', f3) # f3:˽14/6

try:
    f4 = f3 + 3.0
    print('f4:', f4)
except ValueError:
    print('f4: value error') # f4:˽value error