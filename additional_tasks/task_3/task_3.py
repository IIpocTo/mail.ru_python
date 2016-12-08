def fibonacci_generator(n=None):

    if n <= 0:
        raise ValueError("parameter 'n' must be positive")

    first = 0
    second = 1

    if n == 1:
        yield first

    yield first
    yield second
    if n is not None:
        counter = 3
        while counter <= n:
            result = first + second
            first = second
            second = result
            counter += 1
            yield result
    else:
        while True:
            result = first + second
            first = second
            second = result
            yield result


for number in fibonacci_generator(54):
    print(number)
