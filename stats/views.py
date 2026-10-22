import sqlite3

from django.shortcuts import render

DB_PATH = "data/finance.sqlite"


def statistics_view(request):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    summary = conn.execute(
        """
        SELECT
            COUNT(*) AS total_count,
            SUM(amount) AS total_amount,
            AVG(amount) AS avg_amount,
            MIN(amount) AS min_amount,
            MAX(amount) AS max_amount
        FROM transactions
        """
    ).fetchone()

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

    context = {
        "total_count": summary["total_count"] or 0,
        "total_amount": summary["total_amount"] or 0,
        "avg_amount": summary["avg_amount"] or 0,
        "min_amount": summary["min_amount"] or 0,
        "max_amount": summary["max_amount"] or 0,
        "rows": rows,
    }
    return render(request, "stats/statistics.html", context)


def expensive_categories(request):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        SELECT c.name AS category, SUM(t.amount) AS total
        FROM categories c
        JOIN transactions t ON t.category_id = c.id
        GROUP BY c.id, c.name
        HAVING SUM(t.amount) > 500
        ORDER BY total DESC
        """
    ).fetchall()
    conn.close()

    context = {"rows": rows}
    return render(request, "stats/expensive_categories.html", context)
