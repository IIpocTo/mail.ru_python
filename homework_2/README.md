# <img src="https://worldvectorlogo.com/logos/mail-ru.svg" width="18%" height="10%" alt="" />
## <img src="https://worldvectorlogo.com/logos/python-3.svg" width="18%" height="10%" alt="" />

<h1>Задание</h1>

Определен следующий бесконечный генератор:
```python
from random import randint
from time import sleep

def events(max_delay, limit):
    while True:
        delay = randint(1, max_delay)
        if delay >= limit:
            sleep(limit)
            yield None
        else:
            sleep(delay)
            yield 'Event generated, awaiting %d s' % delay
```

Необходимо проинициализировать генератор (с произвольными параметрами) в глобальную переменную и определить класс WSGI-
приложения, возвращающий события генератора. При этом в случае успеха (генератор вернул не **None**) приложение должно
возвращать стутус **200 OK**, а в противном случае статус **204 No Content**.