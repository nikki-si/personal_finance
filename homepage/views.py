from django.http import HttpResponse


def index(request):
    return HttpResponse("Личные финансы — учёт расходов")