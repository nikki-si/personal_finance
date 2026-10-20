# main.py ПР№1 
import datetime

# Данные (простые типы)
current_date = datetime.date.today()
monthly_limit = 50000.0
current_expenses = 45000.0

def check_budget(limit: float, expenses: float) -> str:
    """Проверяет, остался ли бюджет."""
    if expenses > limit:
        return "Внимание! Вы превысили месячный лимит расходов."
    elif expenses == limit:
        return "Вы израсходовали бюджет полностью."
    else:
        remaining = limit - expenses
        return f"Бюджет в норме. Осталось: {remaining:.2f} руб."

# Основной сценарий
print(f"Дата проверки: {current_date}")
print(f"Лимит: {monthly_limit} руб. | Потрачено: {current_expenses} руб.")
print(check_budget(monthly_limit, current_expenses))