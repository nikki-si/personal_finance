import sqlite3
from pathlib import Path

from django.core.management.base import BaseCommand

from transactions.models import Category, Transaction

SOURCE_DB = Path("data/finance.sqlite")


class Command(BaseCommand):
    help = "Импорт данных из data/finance.sqlite в Django ORM"

    def handle(self, *args, **options):
        if not SOURCE_DB.exists():
            self.stdout.write(self.style.ERROR(f"Нет файла {SOURCE_DB}"))
            return

        conn = sqlite3.connect(SOURCE_DB)
        conn.row_factory = sqlite3.Row

        # 1. Категории
        categories = conn.execute("SELECT id, name FROM categories").fetchall()
        for row in categories:
            Category.objects.update_or_create(
                id=row["id"], defaults={"name": row["name"]}
            )
        self.stdout.write(f"Категорий: {len(categories)}")

        # 2. Транзакции
        rows = conn.execute(
            "SELECT id, amount, category_id, description FROM transactions"
        ).fetchall()
        for row in rows:
            Transaction.objects.update_or_create(
                id=row["id"],
                defaults={
                    "amount": row["amount"],
                    "category_id": row["category_id"],
                    "description": row["description"] or "",
                },
            )
        self.stdout.write(f"Транзакций: {len(rows)}")

        conn.close()
        self.stdout.write(self.style.SUCCESS("Импорт завершён"))
