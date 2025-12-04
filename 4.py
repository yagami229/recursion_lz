import random
def addition():
    a = random.randint(10**9, 10**10)
    b = random.randint(10**9, 10**10)
    print(list((str(a), str(b))))
    print('Сумма =', str(a+b))
    return addition()
if __name__== '__main__':
    addition()