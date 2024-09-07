import unittest
from BankingSystemImpl import BankingSystemImpl


class TestBankingSystemImpl(unittest.TestCase):

    def setUp(self):
        self.banking_system = BankingSystemImpl()

    def test_create_account_various_balances(self):
        # Create account with 0 opening balance
        result = self.banking_system.create_account(1, "account_1", 0)
        self.assertTrue(result)

        # Create account with 1000 opening balance
        result = self.banking_system.create_account(2, "account_2", 1000)
        self.assertTrue(result)

        # Try to create an already existing account
        result = self.banking_system.create_account(3, "account_1", 500)
        self.assertFalse(result)

    def test_validate_balance_after_transfer(self):
        self.banking_system.create_account(1, "account_1", 500)
        self.banking_system.create_account(2, "account_2", 300)
        self.banking_system.create_account(3, "account_3", 200)

        # Transfer between accounts
        self.banking_system.transfer(4, "account_1", "account_2", 200)
        self.banking_system.transfer(5, "account_2", "account_3", 100)
        self.banking_system.transfer(6, "account_3", "account_1", 50)

        # Validate balances
        account_1 = next(acc for acc in self.banking_system.accounts if acc.account_id == "account_1")
        account_2 = next(acc for acc in self.banking_system.accounts if acc.account_id == "account_2")
        account_3 = next(acc for acc in self.banking_system.accounts if acc.account_id == "account_3")

        self.assertEqual(account_1.balance, 350)
        self.assertEqual(account_2.balance, 400)
        self.assertEqual(account_3.balance, 250)

    def test_find_top_n_spending_accounts(self):
        self.banking_system.create_account(1, "account_1", 1000)
        self.banking_system.create_account(2, "account_2", 1000)
        self.banking_system.create_account(3, "account_3", 1000)
        self.banking_system.create_account(4, "dummy_account", 0)
        # Transfer amounts to simulate spending
        self.banking_system.transfer(2, "account_1", "dummy_account", 300)
        self.banking_system.transfer(3, "account_2", "dummy_account", 500)
        self.banking_system.transfer(4, "account_3", "dummy_account", 200)

        top_spenders = self.banking_system.get_n_top_spenders()
        self.assertEqual(top_spenders, {"account_2": 500, "account_1": 300, "account_3": 200})

    def test_create_account_with_negative_balance(self):
        # Attempt to create an account with a negative balance
        result = self.banking_system.create_account(1, "account_1", -100)
        self.assertFalse(result)

    def test_transfer_to_same_account(self):
        self.banking_system.create_account(1, "account_1", 500)

        # Attempt to transfer to the same account
        balance = self.banking_system.transfer(2, "account_1", "account_1", 100)
        self.assertIsNone(balance)

    def test_transfer_with_insufficient_balance(self):
        self.banking_system.create_account(1, "account_1", 100)
        self.banking_system.create_account(2, "account_2", 200)

        # Attempt to transfer more than the available balance
        balance = self.banking_system.transfer(2, "account_1", "account_2", 150)
        self.assertIsNone(balance)

    def test_get_n_top_spenders_with_no_spending(self):
        self.banking_system.create_account(1, "account_1", 1000)
        self.banking_system.create_account(2, "account_2", 1000)

        # No spending has occurred
        top_spenders = self.banking_system.get_n_top_spenders()
        self.assertEqual(top_spenders, {})

    def test_get_n_top_spenders_with_equal_spending(self):
        self.banking_system.create_account(1, "account_1", 1000)
        self.banking_system.create_account(2, "account_2", 1000)
        self.banking_system.create_account(3, "dummy_account", 0)

        # Equal spending from both accounts
        self.banking_system.transfer(2, "account_1", "dummy_account", 300)
        self.banking_system.transfer(3, "account_2", "dummy_account", 300)

        top_spenders = self.banking_system.get_n_top_spenders()
        self.assertEqual(top_spenders, {"account_1": 300, "account_2": 300})

    def test_get_n_top_spenders_with_n_explicit(self):
        self.banking_system.create_account(1, "account_1", 1000)
        self.banking_system.create_account(2, "account_2", 1000)
        self.banking_system.create_account(3, "account_3", 1000)
        self.banking_system.create_account(4, "dummy_account", 0)

        # Transfer amounts to simulate spending
        self.banking_system.transfer(2, "account_1", "dummy_account", 300)
        self.banking_system.transfer(3, "account_2", "dummy_account", 500)
        self.banking_system.transfer(4, "account_3", "dummy_account", 200)

        # Test with n = 1
        top_spenders = self.banking_system.get_n_top_spenders(1)
        self.assertEqual(top_spenders, {"account_2": 500})

        # Test with n = 2
        top_spenders = self.banking_system.get_n_top_spenders(2)
        self.assertEqual(top_spenders, {"account_2": 500, "account_1": 300})

        # Test with n = 3
        top_spenders = self.banking_system.get_n_top_spenders(3)
        self.assertEqual(top_spenders, {"account_2": 500, "account_1": 300, "account_3": 200})

        # Test with n greater than the number of accounts
        top_spenders = self.banking_system.get_n_top_spenders(5)
        self.assertEqual(top_spenders, {"account_2": 500, "account_1": 300, "account_3": 200})


if __name__ == '__main__':
    unittest.main()
