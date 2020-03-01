'''
Дана послідовність цілих чисел а1, ... a30. Нехай М - найбільше з цих чисел, а m -
найменше. Вивести на екран у порядку зростання всі цілі з інтервалу (m, M), які не
входять до послідовність а1, ... а30.
'''
from  random import randint
while True:
    a = [randint(1,50) for i in range(31)]
    M = max(a)
    m = min(a)
    z = []
    for i in range(m,M+1):
        z.append(i)
        for j in range(len(z)):
            if z[j] in a:
                z.remove(z[j])
    print(z)
    key = input('Again? Yes - 1, no - 2: ')
    if key == '1':
        continue
    else:
        print('Bye')
        break