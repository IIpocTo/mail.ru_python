import sys
from decimal import Decimal


def round_decorator(inner_func):
    def wrapper(self):
        return round(inner_func(self), 2)

    return wrapper


class Charge:
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self.get_value)

    @property
    @round_decorator
    def get_value(self):
        return self._value


class Account:
    def __init__(self, total=Decimal(0)):
        if isinstance(total, (int, float, Decimal)):
            if total < 0:
                raise AttributeError("Constructor 'Account' parameter 'total'")
            else:
                self._total = Decimal(total)
                self._charges = []
                self._current = 0
        else:
            raise ValueError("Account(" + str(total) + ")")

    def __iter__(self):
        return iter(self._charges)

    def __next__(self):
        if self._current > len(self._charges):
            self._current = 0
            raise StopIteration
        else:
            self._current += 1
            return self._current - 1

    @property
    @round_decorator
    def get_total(self):
        return self._total

    def income(self, amount):
        if isinstance(amount, (int, float, Decimal)):
            if amount < 0:
                raise AttributeError("Function 'income' parameter 'amount'")
            else:
                decimal_amount = Decimal(amount)
                self._charges.append(Charge(decimal_amount))
                self._total += decimal_amount
        else:
            raise ValueError("income(" + str(amount) + ")")

    def outcome(self, amount):
        if isinstance(amount, (int, float, Decimal)):
            if amount < 0:
                raise AttributeError("Function 'outcome' parameter 'amount'")

            decimal_amount = Decimal(amount)
            if decimal_amount - self._total > 0:
                print("There is no requested amount of money: " + str(amount))
            else:
                self._charges.append(Charge(-decimal_amount))
                self._total -= decimal_amount
        else:
            raise ValueError("outcome(" + str(amount) + ")")


if __name__ == "__main__":

    try:

        account = Account(2.342)
        account.outcome(32)
        account.income(3.3232876)
        account.income(2.3272)
        account.outcome(3.785335)
        account.outcome(0.001)
        account.income(1.323)
        account.outcome(12.323)

        print("\nOperation history:")
        for elem in account:
            print(elem)

        print("\nTotal: " + str(account.get_total))

    except ValueError:
        print("Given parameter must be an instance of int, float or Decimal -", sys.exc_info()[1])
    except AttributeError:
        print(sys.exc_info()[1], "must be non-negative")
