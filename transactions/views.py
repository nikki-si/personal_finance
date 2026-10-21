from django.shortcuts import render

from finance_manager import load_transactions, get_total_expenses


def transactions_list(request):
    transactions = load_transactions()

    total = get_total_expenses(transactions)
    context = {
        "transactions": transactions,
        "total": total,
    }
    return render(request, "transactions/transaction_list.html", context)


def transaction_detail(request, transaction_id):
    transactions = load_transactions()
    transaction = None
    for t in transactions:
        if t.id == transaction_id:
            transaction = t
            break

    context = {"transaction": transaction}
    return render(
        request,
        "transactions/transaction_detail.html",
        context,
        status=404 if transaction is None else 200,
    )
