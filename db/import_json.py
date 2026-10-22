import json

from db.database import get_connection

TRANSACTIONS_FILE = "data/transactions.json"


def load_json(filename):
    with open(filename, encoding="utf-8") as f:
        return json.load(f)


def import_data(conn):
    transactions = load_json(TRANSACTIONS_FILE)

    # Сбор уникальных категорий
    category_names = set()
    for t in transactions:
        category_names.add(t["category"])

    # Вставка категорий
    categories = [
        {"id": i + 1, "name": name}
        for i, name in enumerate(sorted(category_names))
    ]
    conn.executemany(
        "INSERT INTO categories (id, name) VALUES (?, ?)",
        [(c["id"], c["name"]) for c in categories],
    )

    # Сопоставление "название категории -> id"
    name_to_id = {c["name"]: c["id"] for c in categories}

    # Вставка транзакции
    conn.executemany(
        """
        INSERT INTO transactions (id, amount, category_id, description)
        VALUES (?, ?, ?, ?)
        """,
        [
            (
                t["id"],
                t["amount"],
                name_to_id[t["category"]],
                t["description"],
            )
            for t in transactions
        ],
    )


def main():
    conn = get_connection()
    try:
        import_data(conn)
        conn.commit()
        print("OK: данные импортированы")
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == "__main__":
    main()
