# finance_manager.py
import json
import os
from models.transaction import Transaction

DATA_FILE = "data/transactions.json"


def load_transactions() -> list[Transaction]:
    """Загружает транзакции и превращает их в объекты."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
        return [Transaction.from_dict(item) for item in data]


def save_transactions(transactions: list[Transaction]) -> None:
    """Сохраняет объекты в файл."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        #  каждый объект в словарь перед сохранением
        data = [t.to_dict() for t in transactions]
        json.dump(data, file, ensure_ascii=False, indent=4)


def get_total_expenses(transactions: list[Transaction]) -> float:
    """Считает общую сумму расходов."""
    total = 0.0
    for t in transactions:
        total += t.amount  # обращение к атрибуту объекта, а не к ключу словаря
    return total
