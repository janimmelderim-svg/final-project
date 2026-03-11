import json
import os

data_file=expenses.json

def load_expenses():
    """ielādē izdevumus no json faila"""
    if not os.path.exists(data_file):
        return []
    
    try:
        with open(data_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_expenses(expenses):
    """saglabā izdevumus json failā"""
    try:
        with open(data_file, "w", encoding="utf-8") as f:
            json.dump(expenses, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        return False
    


