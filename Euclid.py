def NOD():
    a = int(input('Введите число: '))
    b = int(input('Введите число: '))
    print(list((a,b)))
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else: 
            b = b % a
    print('НОД этих чисел равен', a + b)
    return NOD()
NOD()
