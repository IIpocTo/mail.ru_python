from time import sleep
from time import time
from random import randint


def constrained(param):
    def decorator(f):
        def wrapper(*args, **kwargs):
            start = time()
            res = f(*args, **kwargs)
            cont = time() - start
            if cont > param:
                print("The program has been executing for " + str(cont) + " seconds,")
            return res
        return wrapper
    return decorator


@constrained(8)
def f(message):
    delay = randint(1, 10)
    sleep(delay)
    print(message)
    return


if __name__ == "__main__":
    for i in range(10):
        f("I have been executed! :)")
