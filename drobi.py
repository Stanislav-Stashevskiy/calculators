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


def plus(a, b, c, d):
    if b == d:
        drob = a + c

        if b % drob == 0 and drob != 1:
            b = b / drob
            drob = drob / drob

            print(drob)
            print('--')
            print(b)

        elif b % drob != 0 or drob == 1:
            print(drob)
            print('--')
            print(b)

    elif b != d:
        a, b, c, d = znamenatel(a, b, c, d)
        drob = a + c
        print(drob)
        print('--')
        print(b)
        return a, b, c, d


def minus(a, b, c, d):
    if b == d:
        drob = a - c
        if b % drob == 0 and drob != 1:
            b = b / drob
            drob = drob / drob

            print(drob)
            print('--')
            print(b)

        elif b % drob != 0 or drob == 1:
            print(drob)
            print('--')
            print(b)

    elif b != d:
        a, b, c, d, = znamenatel(a, b, c, d)
        drob = b - c

        if b % drob == 0 and drob != 1:
            b = b / drob
            drob = drob / drob

            print(drob)
            print('--')
            print(b)

        elif b % drob != 0 or drob == 1:
            print(drob)
            print('--')
            print(b)

    return a, b, d, c


def mnoshity(a, b, c, d):
    drob = a * c
    drob2 = b * d

    if drob > drob2:
        nd = nod(drob, drob2)

        if drob2 % drob == 0 and drob != 1:
            drob2 = drob2 / drob
            drob = drob / drob

            print(drob)
            print('--')
            print(drob2)

        elif b % drob != 0 or drob == 1:
            print(drob / nd)
            print('--')
            print(b / nd)

    elif drob < drob2:
        if drob2 % drob == 0 and drob != 1:
            drob2 = drob2 / drob
            drob = drob / drob

            print(drob)
            print('--')
            print(drob2)

        elif drob2 % drob != 0 or drob == 1:
            print(drob)
            print('--')
            print(drob2)

    return a, b, d, c


def delit(a, b, c, d):
    x = d
    y = c

    drob = a * x
    drob2 = b * y

    if drob > drob2:
        nd = nod(drob, drob2)

        if b % drob == 0 and drob != 1:
            drob2 = drob2 / drob
            drob = drob / drob

            print(drob / nd)
            print('--')
            print(drob2 / nd)

        elif b % drob != 0 or drob == 1:
            print(drob / nd)
            print('--')
            print(drob2 / nd)

    elif drob < drob2:
        if drob2 % drob == 0 and drob != 1:
            drob2 = drob2 / drob
            drob = drob / drob

            print(drob)
            print('--')
            print(drob2)

        elif drob2 % drob != 0 or drob == 1:
            print(drob)
            print('--')
            print(drob2)

    return a, b, c, d


def main():
    a = int(input('введите первый числитель:'))
    b = int(input('введите первый знаменатель:'))
    c = int(input('введите второй числитель:'))
    d = int(input('введите второй знаменатель:'))

    what = input('что делаем(/,*,+,-)')

    if what == '+':
        plus(a, b, c, d)
    elif what == '-':
        minus(a, b, c, d)
    elif what == '*':
        mnoshity(a, b, c, d)
    elif what == '/':
        delit(a, b, c, d)


if __name__ == '__main__':
    main()
