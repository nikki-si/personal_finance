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
