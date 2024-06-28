
class Category:
    def __init__(self, name):
        self.name = name
        self.transactions = []

    def add_transaction(self, transaction):
        self.transaction.append(transaction)

    def get_total_amount(self):
        return sum(transaction.amount for transaction in self.transactions)

    def __repr__(self):
        return f"Category(name='{self.name}', total_amount={self.get_total_amount()})"
