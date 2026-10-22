import sqlite3

from django.shortcuts import render

DB_PATH = "data/finance.sqlite"


def statistics_view(request):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    total_row = conn.execute(
        "SELECT SUM(amount) AS total FROM transactions"
    ).fetchone()
    total = total_row["total"] if total_row["total"] is not None else 0

    rows = conn.execute(
        """
        SELECT c.name AS category, SUM(t.amount) AS total
        FROM categories c
        LEFT JOIN transactions t ON t.category_id = c.id
        GROUP BY c.id, c.name
        ORDER BY total DESC
        """
    ).fetchall()
    conn.close()

    context = {"total": total, "rows": rows}
    return render(request, "stats/statistics.html", context)
