from django.shortcuts import render

from finance_manager import load_transactions, get_total_expenses


def statistics_view(request):
    transactions = load_transactions()
    total = get_total_expenses(transactions)

    categories = {}
    for t in transactions:
        categories[t.category] = categories.get(t.category, 0) + t.amount

    rows = [
        {"category": cat, "amount": amount}
        for cat, amount in categories.items()
    ]

    context = {"total": total, "rows": rows}
    return render(request, "stats/statistics.html", context)
