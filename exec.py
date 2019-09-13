import math

palabra = "Electroencefalografista"
palabra2 = "esternocleidomastoideo"

resultado = palabra[::-1]


def saldos():
    pass


a = math.factorial(4)


def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b


def test_valor_kwargs(**kwargs):
    if kwargs is not None:
        for key,  value in kwargs.items():
            print('%s == %s' % (key, value))

    print(type(kwargs))


def imprime_Fibonacci():
    #fib1 = fibonacci(1000)
    #fib_nums = [num for num in fib1]
    # double_fib_nums = [num * 3 for num in fib1]
    double_fib_nums = [num * 5 for num in fibonacci(100)]

    print(double_fib_nums)


if __name__ == '__main__':
    test_valor_kwargs(caricatura='batman', sexo='masculino')
    imprime_Fibonacci()
