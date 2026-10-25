import json
import os


def test_transactions_json_exists():
    assert os.path.exists("data/transactions.json")


def test_transactions_json_has_data():
    with open("data/transactions.json", encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data, list)
    assert len(data) >= 10
