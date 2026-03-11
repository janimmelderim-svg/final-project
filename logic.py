from datetime import datetime

def sum_total(expenses):

    """"aprēķina visu izdevumu kopsummu"""

    return round(sum(expense.get("amount", 0)for expense in expenses), 2)

def filter_by_month(expenses, year_month):

    """Atgriež tikai tos izdevumus, kas sākas ar GGGG-MM."""

    return [exp for exp in expenses if exp['datums'].startswith(year_month)]

def sum_by_category(expenses):

    """Sagrupē summas pa kategorijām."""

    summary = {}
    for exp in expenses:
        kat = exp['kategorija']
        summary[kat] = summary.get(kat, 0) + exp['summa']
    return summary

def get_available_months(expenses):

    """Atrod unikālus mēnešus (GGGG-MM) un sakārto tos."""

    months = {exp['datums'][:7] for exp in expenses}
    return sorted(list(months), reverse=True)

def is_valid_date(date_string):

    """Pārbauda, vai datums atbilst formātam YYYY-MM-DD un ir eksistējošs."""
    
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False