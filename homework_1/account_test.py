import sys
import unittest
from decimal import Decimal
from io import StringIO

from homework_1.lec3_homework import Account


class AccountTest(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.__stdout__, StringIO()
        self.account = Account()
        self.any_positive_constructor_param = 2.343216
        self.any_negative_constructor_param = -1.45435
        self.any_wrong_type_param = []
        self.any_income = 4.4324525
        self.any_outcome = 2.34234
        self.any_negative_amount = -5.9023

    def test_account_should_have_zero_total_balance_with_empty_constructor(self):
        self.assertEqual(0, self.account.get_total)

    def test_account_should_set_total_balance_to_constructor_param_value(self):
        self.account = Account(self.any_positive_constructor_param)
        self.assertAlmostEqual(Decimal(2.34), self.account.get_total)

    def test_account_constructor_should_throw_ae_with_negative_param(self):
        with self.assertRaises(AttributeError):
            self.account = Account(self.any_negative_constructor_param)

    def test_account_constructor_should_throw_ve_with_wrong_type_param(self):
        with self.assertRaises(ValueError):
            self.account = Account(self.any_wrong_type_param)

    def test_income_must_add_value_to_total_balance(self):
        self.account.income(self.any_income)
        self.assertAlmostEqual(Decimal(4.43), self.account.get_total, delta=0.001)

    def test_income_must_throw_ae_while_get_negative_amount(self):
        with self.assertRaises(AttributeError):
            self.account.income(self.any_negative_amount)

    def test_income_must_throw_ve_while_get_wrong_type_param(self):
        with self.assertRaises(ValueError):
            self.account.income(self.any_wrong_type_param)

    def test_outcome_must_subtract_value_from_total_balance_if_that_amount_exists(self):
        self.account.income(self.any_income)
        self.account.outcome(self.any_outcome)
        self.assertAlmostEqual(Decimal(2.09), self.account.get_total, delta=0.001)

    def test_outcome_must_print_error_message_if_requested_amount_greater_than_total_balance(self):
        self.account.outcome(self.any_outcome)
        self.assertEqual("There is no requested amount of money: " + str(self.any_outcome),
                         sys.stdout.getvalue().strip())

    def test_outcome_must_throw_ae_while_get_negative_amount(self):
        with self.assertRaises(AttributeError):
            self.account.outcome(self.any_negative_amount)

    def test_outcome_must_throw_ve_while_get_wrong_type_param(self):
        with self.assertRaises(ValueError):
            self.account.outcome(self.any_wrong_type_param)


if __name__ == "__main__":
    unittest.main()
