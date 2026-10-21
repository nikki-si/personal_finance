# models/transaction.py


class Transaction:
    """Класс, описывающий одну финансовую операцию (расход)."""

    def __init__(
        self,
        transaction_id: int,
        amount: float,
        category: str,
        description: str,
    ):
        self.id = transaction_id
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self) -> str:
        return f"[{self.id}] {self.category}: {self.amount} руб."

    @classmethod
    def from_dict(cls, data: dict) -> 'Transaction':
        """Создает объект из словаря (для загрузки из JSON)."""
        return cls(
            transaction_id=data["id"],
            amount=data["amount"],
            category=data["category"],
            description=data["description"],
        )

    def to_dict(self) -> dict:
        """Превращает объект в словарь (для сохранения в JSON)."""
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
        }
