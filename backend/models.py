from datetime import date

class Expense:
    def __init__(self, item, amount, category, recurring=False, day=None):
        self.item = item
        self.amount = amount
        self.category = category
        self.recurring = recurring
        self.date = day or str(date.today())

    def to_dict(self):
        return{
            "item": self.item,
            "amount": self.amount,
            "catagory": self.catagory,
            "recurring": self.recurring,
            "date": self.date
        }

