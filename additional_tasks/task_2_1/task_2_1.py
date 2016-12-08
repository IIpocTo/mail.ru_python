from time import sleep
from time import time
from random import randint


def slow_log(param):
    def decorator(f):
        def wrapper(*args, **kwargs):
            start = time()
            res = f(*args, **kwargs)
            func_exec_time = time() - start
            if func_exec_time > param:
                print("The program has been executing for " + str(func_exec_time) + " seconds,")
            return res
        return wrapper
    return decorator


@slow_log(8)
def f(message):
    delay = randint(1, 10)
    sleep(delay)
    print(message)
    return


if __name__ == "__main__":
    for i in range(10):
        f("I have been executed! :)")
