from django.http import HttpResponse

from finance_manager import load_transactions, get_total_expenses
from homepage.views import page


def transactions_list(request):
    transactions = load_transactions()

    items = ""
    for t in transactions:
        items += (
            f'<li class="list-group-item">'
            f'<a href="/transactions/{t.id}/">{t}</a>'
            f'</li>'
        )

    total = get_total_expenses(transactions)
    content = f"""
    <h1>Транзакции</h1>
    <p>Всего транзакций: <strong>{len(transactions)}</strong></p>
    <p>Общая сумма расходов: <strong>{total} руб.</strong></p>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("Транзакции", content))


def transaction_detail(request, transaction_id):
    transactions = load_transactions()
    transaction = None
    for t in transactions:
        if t.id == transaction_id:
            transaction = t
            break

    if transaction is None:
        content = """
        <h1 class="text-danger">Транзакция не найдена</h1>
        <a href="/transactions/" class="btn btn-outline-secondary">
        ← к списку транзакций
        </a>
        """
        return HttpResponse(
            page("Транзакция не найдена", content),
            status=404,
        )

    content = f"""
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">Транзакция №{transaction.id}</h5>
        <p class="card-text"><strong>Сумма:</strong> {transaction.amount} руб.</p>
        <p class="card-text"><strong>Категория:</strong> {transaction.category}</p>
        <p class="card-text"><strong>Описание:</strong> {transaction.description}</p>
        <a href="/transactions/" class="btn btn-outline-secondary">
        ← к списку транзакций
        </a>
      </div>
    </div>
    """
    return HttpResponse(page(f"Транзакция №{transaction.id}", content))
