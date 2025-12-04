def notation():
    num = int(input('Введите число: '))
    sistema = int(input('Введите систему счисления от 2 до 16: '))
    symbols = '0123456789ABCDEF'
    new = ''
    while num > 0:
        num, remainder = divmod(num, sistema)        
        new = symbols[remainder] + new
    print(new)
    return notation()
if __name__== '__main__':
    notation()

