from roman import *

arabic = [str(x) for x in input('Введите римское чилсло что преобразовать в арабское: ').split()]
for i in arabic:
    print(i, '->' ,roman_to_int(i))


number = [int(x) for x in input('Введите арабское чилсло что преобразовать в римское: ').split()]
# a=[4, 58, 1994, 26, 99, 69, 80]
for i in number:
    print(i, '->',int_to_roman(i))
