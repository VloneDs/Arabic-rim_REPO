from roman import *
choise = str(input('1 - из римского числа в арабское число(III - 3).\n2 - из арабского число в римское число(3 - III).\n Ответ:  '))

if choise == '1':
    arabic = [str(x) for x in input('Введите римское число что-бы преобразовать в арабское: ').upper().split()]
    for i in arabic:
        print(i, '->' ,roman_to_int(i))

elif choise == '2':
    roman = [int(x) for x in input('Введите арабское число что-бы преобразовать в римское: ').split()]
    for i in roman:
      print(i, '->',int_to_roman(i))

else:
    print('Повторите еще раз проверив правильность ввода')