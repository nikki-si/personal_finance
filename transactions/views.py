from django.http import HttpResponse


def transactions_list(request):
    return HttpResponse("Список транзакций")


def transaction_detail(request, transaction_id):
    return HttpResponse(f"Транзакция {transaction_id}")