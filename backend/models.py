from datetime import datetime

ALLOWED_CATEGORIES = ["Food", "Transport", "Bills", "Shopping", "Entertainment", "Other"]

class Expense:
    def __init__(self, id, item, date, amount, category, recurring=False, note=""):
        self.id = id
        self.item = item
        self.date = date
        self.amount = amount
        self.category = category
        self.recurring = recurring
        self.note = note.strip() if note else ""

        now = datetime.utcnow().isoformat()
        self.created_at = now
        self.updated_at = now
        
    def to_dict(self):
        return{
            "id": self.id,
            "item": self.item,
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "recurring": self.recurring,
            "note": self.note,
            "created_at": self.created_at
            "updated_at": self.updated_at
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id = data["id"],
            item = data["item"],
            date = data["date"],
            amount = data["amount"],
            category = data["category"],
            recurring = data.get("recurring", False),
            note = data.get("note", "")   
        )

