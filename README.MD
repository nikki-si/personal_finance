# Система управления личными финансами

## Назначение
Приложение для учёта личных расходов и контроля бюджета. Консольная версия (ПР3) → веб-интерфейс на Django (ПР5) → шаблоны (ПР6) → база данных SQLite (ПР7).

## Используемые технологии
- Python 3
- Django 5.2
- Django Template Language (DTL)
- HTML5, CSS3, JavaScript
- Bootstrap 5.3
- SQLite (база данных)
- `sqlite3` (стандартная библиотека Python)
- pytest, flake8

## Предметная область
Учёт финансовых операций (расходов). Каждая транзакция имеет сумму, категорию и описание. Категории хранятся в отдельной таблице.

## Основные сущности
- **Category** — категория расхода (`id`, `name`).
- **Transaction** — операция (`id`, `amount`, `category_id`, `description`).

## База данных (ПР7)

### Структура
- `categories` — категории: `id INTEGER PRIMARY KEY`, `name TEXT NOT NULL`.
- `transactions` — транзакции: `id INTEGER PRIMARY KEY`, `amount REAL NOT NULL`, `category_id INTEGER NOT NULL`, `description TEXT`, внешний ключ `category_id → categories.id`.

### Файлы
- `sql/schema.sql` — создание таблиц.
- `sql/queries.sql` — 12 SQL-запросов проекта (SELECT, WHERE, JOIN, COUNT, SUM, AVG, GROUP BY, HAVING, MAX).
- `db/database.py` — подключение к SQLite, `PRAGMA foreign_keys = ON`.
- `db/import_json.py` — импорт данных из `data/transactions.json` в SQLite.
- `data/finance.sqlite` — файл базы данных.

### Импорт данных
```bash
python -m db.import_json