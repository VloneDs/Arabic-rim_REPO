def roman_to_int(number_1:str)->int:
    res=0
    roman_number = {'CM':900, 'CD':400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV':4,
        'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    for number in roman_number:
        res += roman_number[number] * number_1.count(number)
        number_1 = number_1.replace(number, '')
    return res

def int_to_roman(num:int)->str:
    info = ['I', 'X', 'C', 'M']
    #      0    1    2    3   
    weird_number = ''
    number = 0
    while num != 0:
        n = num % 10
        weird_number = info[number] * n + weird_number
        num //= 10
        number += 1
    res = weird_number
    res = res.replace('IIIIIIIII','IX')
    res = res.replace('IIIII', 'V')
    res = res.replace('IIII', 'IV')
    res = res.replace('XXXXXXXXX','XC')
    res = res.replace('XXXXX','L')
    res = res.replace('XXXX','XL')
    res = res.replace('CCCCCCCCC','CM')
    res = res.replace('CCCCC','D')
    res = res.replace('CCCC','CD')
    return res

