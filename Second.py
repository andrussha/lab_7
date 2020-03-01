'''
Визначити комп'ютер, виготовлений фірмою AMD з мінімальною ціною і
вивести всі відомості про нього. Поля структури: Виробник, Обсяг оперативної пам’яті,
Дата виготовлення, Ціна.
Постолович А.С. 122-В
'''
while True:
    from random import randint
    d = {'Producer': 'AMD', 'RAM':'16 Gb','Date of manufacture':'20.02.2019', 'Price':randint(7000,15000)}
    c = {'Producer': 'AMD', 'RAM':'8 Gb','Date of manufacture':'02.10.2018', 'Price':randint(7000,15000)}
    e = {'Producer': 'AMD', 'RAM':'4 Gb','Date of manufacture':'16.09.2015', 'Price':randint(7000,15000)}
    if d['Price'] < c['Price'] and d['Price'] < e['Price']:
        for items in d:
            print(f'{items} = {d[items]}')
    elif c['Pr ice'] < d['Price'] and c['Price'] < e['Price']:
        for items in c:
            print(f'{items} = {c[items]}')
    else:
        for items in e:
            print(f'{items} = {e[items]}')
    key = input('Again? Yes - 1, no - 2: ')
    if key == '1':
        continue
    else:
        print('Bye')
        break