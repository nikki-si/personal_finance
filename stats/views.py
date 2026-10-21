from django.http import HttpResponse

from finance_manager import load_transactions, get_total_expenses
from homepage.views import page


def statistics_view(request):
    transactions = load_transactions()
    total = get_total_expenses(transactions)

    categories = {}
    for t in transactions:
        categories[t.category] = categories.get(t.category, 0) + t.amount

    rows = ""
    for cat, amount in categories.items():
        rows += f"<tr><td>{cat}</td><td>{amount} руб.</td></tr>"

    content = f"""
    <h1>Статистика расходов</h1>
    <p>Общая сумма расходов: <strong>{total} руб.</strong></p>
    <table class="table table-striped">
      <thead>
        <tr><th>Категория</th><th>Сумма</th></tr>
      </thead>
      <tbody>{rows}</tbody>
    </table>
    """
    return HttpResponse(page("Статистика", content))