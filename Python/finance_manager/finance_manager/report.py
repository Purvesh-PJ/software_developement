
class Report:
    def __init__(self, categories):
        self.categories = categories

    def generate(self):
        report = "Finance Report:\n"
        for category in self.categories:
            report += f"Category: {category.name}\n"
            report += f"Total Amount: {category.get_total_amount()}\n"
            for transaction in category.transactions:
                report += f"  - {transaction}\n"
        return report