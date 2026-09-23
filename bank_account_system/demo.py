"""Demo of the BankAccountImpl."""

from bank_account import BankAccountImpl


def main():
    bank = BankAccountImpl()

    bank.create_account("12345", "savings")
    bank.create_account("67890", "checking")

    bank.deposit("12345", 1000)
    bank.deposit("67890", 2000)
    bank.withdraw("12345", 200)

    print(f"Баланс 12345: {bank.get_balance('12345')}")   # 800
    print(f"Баланс 67890: {bank.get_balance('67890')}")   # 2000
    print(f"История 12345: {bank.get_transaction_history('12345')}")

    bank.apply_interest()
    print(f"После процентов 12345: {bank.get_balance('12345')}")  # 840.0
    print(f"После процентов 67890: {bank.get_balance('67890')}")  # 2000


if __name__ == "__main__":
    main()