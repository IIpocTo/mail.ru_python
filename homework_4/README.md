# <img src="https://worldvectorlogo.com/logos/mail-ru.svg" width="18%" height="10%" alt="" />
## <img src="https://worldvectorlogo.com/logos/python-3.svg" width="18%" height="10%" alt="" />

<h1>Задание</h1>

  1. Необходимо разработать представление и форму для сущности **Charge** и реализовать необходимые проверки, при
     этом транзакции-списания (с отрицательным значением) не могут быть заведены на будущее (дата **date** в таких
     транзакциях должна быть меньше или равна сегодняшнему дню из **date.today**). В случае успеха или неудачи
     (определяемым по корректности заполнения формы) нужно выводить соответствующие сообщения.
     
  2. Задан генератор (источник данных), возвращающий случайное количество пар (**date**, **value**) для транзакций:
     ```python
     from datetime import date
     from decimal import Decimal
     from random import randint
     
     
     def random_transactions():
         today = date.today()
         start_date = today.replace(month=1, day=1).toordinal()
         end_date = today.toordinal()
         while True:
             start_date = randint(start_date, end_date)
             random_date = date.fromordinal(start_date)
             if random_date >= today:
                 break
             random_value = randint(-10000, 10000), randint(0, 99)
             random_value = Decimal('%d.%d' % random_value)
             yield random_date, random_value
     ```
     Необходимо разработать представление, которое будет получать от генератора список транзакций и выводить их на
     страницу (для этого следует использовать шаблоны). При этом транзакции-списания (с отрицательным занчением **value**) и
     транзакции-зачисления (с положительным значением **value**) должны выводиться в разные списки на странице (можно 
     использовать для верстки html-списки или таблицы).