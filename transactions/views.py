from django.core.paginator import Paginator
from django.db.models import Sum, Count, Avg, Max, Min, Q
from django.shortcuts import get_object_or_404, render

from .models import Category, Transaction


def transaction_list(request):
    transactions = Transaction.objects.select_related("category")

    # Поиск по описанию/категории
    q = request.GET.get("q", "").strip()
    if q:
        transactions = transactions.filter(
            Q(description__icontains=q) | Q(category__name__icontains=q)
        )

    # Фильтр по категории
    category_id = request.GET.get("category", "").strip()
    if category_id.isdigit():
        transactions = transactions.filter(category_id=int(category_id))

    # Сортировка
    sort_map = {
        "date": "-created_at",
        "amount": "-amount",
        "category": "category__name",
    }
    sort = request.GET.get("sort", "date")
    transactions = transactions.order_by(sort_map.get(sort, "-created_at"), "id")

    # Пагинация
    paginator = Paginator(transactions, 5)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = {
        "page_obj": page_obj,
        "categories": Category.objects.order_by("name"),
        "q": q,
        "selected_category": category_id,
        "sort": sort,
    }
    return render(request, "transactions/transaction_list.html", context)


def transaction_detail(request, pk):
    transaction = get_object_or_404(
        Transaction.objects.select_related("category"), pk=pk
    )
    return render(
        request,
        "transactions/transaction_detail.html",
        {"transaction": transaction},
    )


def transaction_by_category(request):
    category_name = request.GET.get("category", "").strip()
    transactions = Transaction.objects.none()
    if category_name:
        transactions = (
            Transaction.objects.select_related("category")
            .filter(category__name__iexact=category_name)
            .order_by("-amount")
        )
    return render(
        request,
        "transactions/transaction_by_category.html",
        {"transactions": transactions, "category": category_name},
    )


def transaction_over(request):
    amount = request.GET.get("amount", "").strip()
    transactions = Transaction.objects.none()
    error = None
    if amount:
        try:
            amount_value = float(amount)
        except ValueError:
            error = "Введите корректное число."
        else:
            transactions = (
                Transaction.objects.select_related("category")
                .filter(amount__gt=amount_value)
                .order_by("-amount")
            )
    return render(
        request,
        "transactions/transaction_over.html",
        {"transactions": transactions, "amount": amount, "error": error},
    )


def transaction_top(request):
    transactions = (
        Transaction.objects.select_related("category")
        .order_by("-amount")[:5]
    )
    return render(
        request, "transactions/transaction_top.html", {"transactions": transactions}
    )


def statistics_view(request):
    summary = Transaction.objects.aggregate(
        total_count=Count("id"),
        total_amount=Sum("amount"),
        avg_amount=Avg("amount"),
        min_amount=Min("amount"),
        max_amount=Max("amount"),
    )
    # Суммы по категориям через annotate
    categories = Category.objects.annotate(
        total=Sum("transactions__amount"),
        count=Count("transactions"),
    ).order_by("-total")

    return render(
        request,
        "stats/statistics.html",
        {"summary": summary, "categories": categories},
    )


def expensive_categories(request):
    categories = (
        Category.objects.annotate(total=Sum("transactions__amount"))
        .filter(total__gt=500)
        .order_by("-total")
    )
    return render(
        request,
        "stats/expensive_categories.html",
        {"categories": categories},
    )
