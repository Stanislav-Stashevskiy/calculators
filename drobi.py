def nod(drob, drob2):
    while drob != 0 and drob2 != 0:
        if drob > drob2:
            drob = drob % drob2
        else:
            drob2 = drob2 % drob

    nd = drob + drob2
    return nd


def nok(b, d):
    x = max(b, d)
    y = min(b, d)

    n = x
    while True:
        n += x
        if n % y == 0:
            return n


def znamenatel(a, b, c, d):
    n = nok(b, d)

    return int(a * (n / b)), n, int(c * (n / d)), n


def plus(a, b, c, d):                               # функция plus() складывает обыкновенные дроби

    if b == d:                                      # если знаменатели равны
        drob = a + c                                # складываем числители

        drob2 = b                                   # присваеваем drob2 значение b
        nd = nod(drob, drob2)                       # nd присваеваем НОД drob и drob2
        b = drob2                                   # b присваеваем значение drob2

        if nd == 1:                                 # если НОД ответа равен 1, то...
            print(drob)                             # выводим полученный числитель
            print('--')
            print(b)                                # и прежний знаменвтель

        elif nd != 1:                               # если
            print(drob / nd)                        # делим его на НОД
            print('--')
            print(d / nd)                           # делим его на НОД

    elif b != d:                                    # но если знаменатели не равны
        a, b, c, d = znamenatel(a, b, c, d)         # запускаем функцию znamenatel()
        drob = a + c                                # присваеваем drob сумму числителей

        drob2 = b                                   # присваеваем drob2 значение b
        nd = nod(drob, drob2)                       # nd присваеваем НОД drob и drob2
        b = drob2                                   # b присваеваем значение drob2

        if nd == 1:                                 # если НОД равен 1 то выводим drob и  drob2
            print(drob)
            print('--')
            print(drob2)

        elif nd != 1:                               # но если НОД не равен 1 то воводим drob и  drob2 и делим их на НОД
            print(drob / nd)
            print('--')
            print(drob2 / nd)

    return a, b, c, d                               # возвращаемся к началу


def minus(a, b, c, d):                              # функция minus вычитает обыкновенные дроби
    if b == d:                                      # если знаменатели равны
        drob = a - c                                # то задаём drob значение a-c

        drob2 = b                                   # присваеваем drob2 значение b
        nd = nod(drob, drob2)                       # nd присваеваем НОД drob и drob2
        b = drob2                                   # b присваеваем значение drob2

        if nd == 1:                                 # если НОД ответа равен 1, то просто выводим значение
            print(drob)                             # то-есть дробь не сократимая
            print('--')
            print(drob2)

        elif nd != 1:                               # но если НОД ответа не раевн 1
            print(drob / nd)                        # числитель и знаменать делим на НОД
            print('--')                             # тем самым соеращяем дробь
            print(drob2 / nd)

    elif b != d:                                    # но если знаменатели не равны
        a, b, c, d, = znamenatel(a, b, c, d)        # запускаем функцию znamenatel()
        drob = b - c                                # присваеваем drob разность числителей

        drob2 = b                                   # присваеваем drob2 значение b
        nd = nod(drob, drob2)                       # nd присваеваем НОД drob и drob2
        b = drob2                                   # b присваеваем значение drob2
        # вывод ответа
        if nd == 1:                                 # если НОД равен 1 то выводим значение
            print(drob)
            print('--')
            print(drob2)

        elif nd != 1:                               # но если НОД не равен 1 то делим drob и drob2 на НОД
            print(drob / nd)                        # и выводим
            print('--')
            print(drob2 / nd)

    return a, b, d, c                               # возвращаемся к началу


def mnoshity(a, b, c, d):                          # функция mnoshity перемножает десятичные дроби
    drob = a * c                                   # выполняем стандартное умножение обыкновенных дробей
    drob2 = b * d

    nd = nod(drob, drob2)                          # находим НОД числителя и знаменателя
    # начало сокращения ответа
    if drob2 % drob == 0 and drob != 1:            # если остаток от делния числителя и знаменателя = 0 и числитель не=1
        drob2 = drob2 / drob                       # выполняем простое сокращение
        drob = drob / drob                         # то-есть делим числитель и знаменатель на числитель

        print(drob)                                # выводим результататы
        print('--')
        print(drob2)

    elif drob2 % drob != 0 and drob != 1:   # но если остаток от деления числителя и знаменателя не =0 и числитель не =1
        print(drob / nd)                    # делим числитель и знаменатель на их НОД найденный ранее
        print('--')                         # и выводим результаты
        print(drob2 / nd)

    elif drob == 1:                         # если числитель ответа равен одному, просто выводим полученное значение
        print(drob)
        print('--')
        print(drob2)

    return a, b, d, c                       # возвращаемся к началу


def delit(a, b, c, d):                              # функция delit делит обыкновенные дроби
    drob = a * d                                    # умножаем первый числитель на второй знаменатель
    drob2 = b * c                                   # умножаем первый знаменатель на второй числитель

    if drob > drob2:                                # если числитель ответа больше знаменателя ответа то...
        nd = nod(drob, drob2)                       # для начала находим НОД числителя и знаменателя ответа

        if drob2 % drob == 0 and drob != 1:         # если остаток деления числителя и знаменателя = 0, то...
            drob2 = drob2 / drob                    # числитель будет равен частному...
            drob = drob / drob                      # не сокращенных числителя и знаменателя

            print(drob)                             # выводим ответ
            print('--')
            print(drob2)

        elif drob2 % drob != 0:                     # если остаток от деления числителя и знаменателя не = 0, то...
            print(drob / nd)                        # выводим числитель и знаменатель делённые на НОД
            print('--')
            print(drob2 / nd)

        elif drob == 1:                             # если остаток деления числителя и знаменателя не = 0, то...
            print(drob / nd)                        # делим числитель и знаменатель на НОД и выводим
            print('--')
            print(drob2 / nd)

    elif drob < drob2:                              # если числитель ответа меньше знаменателя ответа то...
        nd = nod(drob, drob2)

        if drob2 % drob == 0:                       # если остаток от деления чисоитеоя и знаменателя равен 0, то
            drob2 = drob2 / drob                    # то знаменатель ответа будет равен частному числителя и знаменателя
            drob = drob / drob                      # а числитель отвтета бужет равен частному двух числителей (0)

            print(drob)                             # выводим ответ
            print('--')
            print(drob2)

        elif drob2 % drob != 0:                     # если остаток от деления числителя и знаменателя не равен 0, то..ю
            print(drob / nd)                        # делим числитель и знаменатель на их НОД
            print('--')                             # и выводим
            print(drob2 / nd)

        elif drob == 1:                             # если числитель ответа равен 1, то...
            print(drob)                             # просто выводим
            print('--')
            print(drob2)

    elif drob / drob2 == 1:                         # если частное чтслителя и знаменателя равно 1, то...
        print(1)                                    # при их сокращении получится 1/1
        print('--')                                 # и выводим
        print(1)

    return a, b, c, d


def main():                                             # главная функция программы
    a = int(input('введите первый числитель:'))         # запрвшиваю первый числитель
    b = int(input('введите первый знаменатель:'))       # запрашиваю первый знаменатель
    c = int(input('введите второй числитель:'))         # запращиваю второй числитель
    d = int(input('введите второй знаменатель:'))       # запрвшиваю второй знаменатель

    what = input('что делаем(/,*,+,-)')                 # и наконец запрашиваю действие

    if what == '+':                         # проверяем равна ли what +
        plus(a, b, c, d)                    # запускаем функцию plus
    elif what == '-':                       # проверяем равна ли what -
        minus(a, b, c, d)                   # запускаем функцию minus
    elif what == '*':                       # проверяем равна ли what *
        mnoshity(a, b, c, d)                # запускаем функцию mnoshity
    elif what == '/':                       # проверяем равна ли what /
        delit(a, b, c, d)                   # запускаем функцию delit

    main()


if __name__ == '__main__':              # запуск программы
    main()
