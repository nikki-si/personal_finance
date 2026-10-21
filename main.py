# main.py
from finance_manager import load_transactions, save_transactions, get_total_expenses
from models.transaction import Transaction

def main():
    transactions = load_transactions()
    
    if not transactions:
        # Создание объектов 
        t1 = Transaction(1, 1500.0, "Продукты", "Пятёрочка")
        t2 = Transaction(2, 500.0, "Транспорт", "Метро")
        transactions.append(t1)
        transactions.append(t2)
        save_transactions(transactions)
    
    print("Список транзакций:")
    for t in transactions:
        print(t) 
        
    total = get_total_expenses(transactions)
    print(f"\nОбщая сумма расходов: {total} руб.")

if __name__ == "__main__":
    main()