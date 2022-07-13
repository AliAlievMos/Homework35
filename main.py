from datetime import datetime
import logging

# Задание 1

cache = dict()


def decorator1(function):
    def wrapper(x, y):
        intro = f'{x}, {y}'
        if intro not in cache:
            cache[intro] = function(x, y)
            sum = cache[intro]
            print(sum)

        else:
            sum = cache[intro]
            print(sum)

    return wrapper


@decorator1
def function(x, y):
    return x**y


decorator1(function(5, 5))
decorator1(function(25, 5))
decorator1(function(7, 5))

print(cache)



# Задание 2


def decorator2(function):
    def wrapper(x, y):
        logging.basicConfig(
            level=logging.DEBUG,
            filename="mylog.log",
            format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
            datefmt='%H:%M:%S',
        )
        logging.info(f'Входные значения x:{x}, y:{y}')
        start_time = datetime.now()
        sum = function(x, y)
        logging.info(f'Результат работы ф-ции:{sum}')
    return wrapper


@decorator2
def function(x, y):
    sum = x**y**y
    return sum


# decorator2(function(5, 5))

# Задание 3


def decorator3(function):
    def wrapper(x, y):
        start_time = datetime.now()
        sum = function(x, y)
        print(sum)
        print(f'Время выполнение функции: {datetime.now() - start_time}')
    return wrapper


@decorator3
def function(x, y):
    return x**y**y


# decorator3(function(5, 5))
