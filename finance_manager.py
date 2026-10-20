# finance_manager.py
import json
import os

DATA_FILE = "data/transactions.json"

def load_transactions() -> list:
    """Загружает транзакции из файла."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_transactions(transactions: list) -> None:
    """Сохраняет транзакции в файл."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(transactions, file, ensure_ascii=False, indent=4)

def add_transaction(transactions: list, amount: float, category: str, description: str) -> None:
    """Добавляет новую транзакцию (расход)."""
    transaction = {
        "id": len(transactions) + 1,
        "amount": amount,
        "category": category,
        "description": description
    }
    transactions.append(transaction)
    print(f"Добавлен расход: {amount} руб. на {category}")

def get_total_expenses(transactions: list) -> float:
    """Считает общую сумму расходов."""
    total = 0.0
    for t in transactions:
        total += t["amount"]
    return total