import sqlite3

from django.shortcuts import render

DB_PATH = "data/finance.sqlite"


def transactions_list(request):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        SELECT t.id, t.amount, c.name AS category, t.description
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
        ORDER BY t.id
        """
    ).fetchall()
    conn.close()
    context = {"transactions": rows}
    return render(request, "transactions/transaction_list.html", context)


def transaction_detail(request, transaction_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    row = conn.execute(
        """
        SELECT t.id, t.amount, c.name AS category, t.description
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
        WHERE t.id = ?
        """,
        [transaction_id],
    ).fetchone()
    conn.close()

    context = {"transaction": row}
    return render(
        request,
        "transactions/transaction_detail.html",
        context,
        status=404 if row is None else 200,
    )


def transactions_by_category(request):
    category = request.GET.get("category")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    if category:
        rows = conn.execute(
            """
            SELECT t.id, t.amount, c.name AS category, t.description
            FROM transactions t
            JOIN categories c ON t.category_id = c.id
            WHERE c.name = ?
            ORDER BY t.amount DESC
            """,
            [category],
        ).fetchall()
    else:
        rows = []
    conn.close()

    context = {"transactions": rows, "category": category}
    return render(
        request, "transactions/transaction_by_category.html", context
    )


def transactions_over(request):
    amount = request.GET.get("amount")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    if amount:
        try:
            amount_value = float(amount)
        except ValueError:
            amount_value = 0
        rows = conn.execute(
            """
            SELECT id, amount, description
            FROM transactions
            WHERE amount > ?
            ORDER BY amount DESC
            """,
            [amount_value],
        ).fetchall()
    else:
        rows = []
    conn.close()

    context = {"transactions": rows, "amount": amount}
    return render(request, "transactions/transaction_over.html", context)


def transactions_top(request):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        SELECT t.id, t.amount, c.name AS category, t.description
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
        ORDER BY t.amount DESC
        LIMIT 5
        """
    ).fetchall()
    conn.close()

    context = {"transactions": rows}
    return render(request, "transactions/transaction_top.html", context)
