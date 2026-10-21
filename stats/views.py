from django.http import HttpResponse


def statistics_view(request):
    return HttpResponse("Статистика расходов")