class BadLen(Exception):
    err = 'Неверное количество переменных.'


class NegativeNum(Exception):
    err = 'Операции доступны только для положительных чисел.'


def main():
    procedure()


def procedure():
    try:
        operation = input('Введите операнд и два положительных числа, разделяя их пробелом: ').split()
        if len(operation) != 3:
            raise BadLen
        action, a, b = operation
        assert action in ['+', '-', '*', '/']
        a = int(a)
        b = int(b)
        if a < 0 or b < 0:
            raise NegativeNum
        if action == '+':
            print(a + b)
        elif action == '-':
            print(a - b)
        elif action == '*':
            print(a * b)
        else:
            print(a / b)
    except BadLen:
        print(BadLen.err)
    except NegativeNum:
        print(NegativeNum.err)
    except ZeroDivisionError:
        print('Попытка делить на ноль.')
    except AssertionError:
        print('Недопустимая операция.')
    except ValueError as value:
        print(f'{a} или {b} не является числом')
    except ZeroDivisionError:
        print('Попытка делить на ноль.')
    except Exception as unexpected:
        print('Случилось что-то неожиданное!', unexpected)
    finally:
        procedure()


main()
