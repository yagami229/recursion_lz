def perfection():
    num = int(input('Введите число: '))
    sum = 0
    for i in range(1, num):   
        if num % i == 0:
            sum += i
    print('Сумма делителей этого числа =', sum)
    if num == sum: print('Число совершенное')
    else: print('Число не совершенное')
    return perfection()
if __name__== '__main__':
    perfection()
