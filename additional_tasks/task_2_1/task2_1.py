from time import sleep
from time import time
from random import randint


def f(param, *args, **kwargs):
    def decorator(*args, **kwargs):
        def wrapper(*args, **kwargs):
            start = time()
            delay = randint(1, 10)
            sleep(delay)
            res = f(*args, **kwargs)
            print("Function has been executed.")
            cont = time() - start
            if cont > param:
                print("The program has been executing for " + str(cont) + " seconds,")
            return res
        return wrapper
    return decorator


@f(8)
def simple_sum(a, b):
    return a + b


if __name__ == "__main__":
    for i in range(10):
        simple_sum(i, i+1)
