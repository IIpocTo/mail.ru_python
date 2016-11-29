# <img src="https://worldvectorlogo.com/logos/mail-ru.svg" width="18%" height="10%" alt="" />
## <img src="https://worldvectorlogo.com/logos/python-3.svg" width="18%" height="10%" alt="" />

<h1>Задание</h1>

 1. Создать модели **Account** и **Charge** (аналогичные сущностям, используемым в предыдущих домашних заданиях), учесть что
    **Account** относится к **Charge** как один-ко-многим. Создать формы для этих моделей, используя **Django Model Forms**.
    
 2. **Реализовать представления**
    - Создание банковского счета
    - Просмотр банковского счета, содержащее:
        - кнопку "Добавить приход/расход"
        - списки транзакций по счету "Приход"/"Расход (запись и чтение в СУБД)
    - Создание транзакции с привязкой с счету (ссылок на счет не должно быть на форме)