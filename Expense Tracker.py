class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category not in self.expenses:
            self.expenses[category] = []
        self.expenses[category].append(amount)

    def view_summary(self):
        for category, expenses in self.expenses.items():
            total = sum(expenses)
            print(f"{category}: ${total}")

# Example usage:
tracker = ExpenseTracker()
tracker.add_expense("Food", 50)
tracker.add_expense("Transportation", 30)
tracker.add_expense("Food", 20)
tracker.view_summary()
