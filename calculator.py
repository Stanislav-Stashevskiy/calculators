ALLOWED_OPERATIONS = ('+', '/', '-', '*')


def main():
    while True:
        what = input('что делаем? (+, -, *, /): ')
        if what not in ALLOWED_OPERATIONS:
            print('выбранна не правильная функция!')
            continue

        try:
            a = float(input('введи первое число:'))
            b = float(input('введи второе число:'))
        except ValueError:
            print('введите число!')
            continue

        if what == '+':
            c = a + b
        elif what == '-':
            c = a - b
        elif what == '*':
            c = a * b
        elif what == '/' and b == 0:
            print('Делить на 0 нельзя')
            main()
        else:
            c = a / b

        print(f'результат {c}')


if __name__ == '__main__':
    main()
