

categories = [
    "Dzīvokļa maksājumi"
    "Ēdiens"
    "Izklaide"
    "Veselība"
    "Transports"
    "Mājai"
    "Cits"
]

def sum_total(expenses):
    """"
    aprēķina visu izdevumu kopsummu
    Args:
        expenses (list): izdevumu saraksts
    returns:
        float: kopējā summa
    """
    return round(sum(expense.get("amount", 0)for expense in expenses), 2)