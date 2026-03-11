from storage import load_expenses, save_expenses
from logic import sum_total
from datetime import date

categories = [
    "Dzīvokļa maksājumi",
    "Ēdiens",
    "Izklaide",
    "Veselība",
    "Transports",
    "Mājai",
    "Cits",
]

def show_menu():
    """"parāda galveno izvēlni"""

    print("\n"+ "="*50)
    print("         IZDEVUMU IZSEKOTĀJS")
    print("="*50)
    print("1) Pievienot izdevumu")
    print("2) Parādīt izdevumus")
    print("7) Iziet")

    return input("\nIzvēlies darbību (1-7): ")

def add_expense(expenses):
    """"funkcija jauna izdevuma pievienošanai"""
    print("\n---  JAUNS IZDEVUMS ---")

    """Datums"""
    today = date.today().isoformat()
    datums = input(f"Datums (YYYY-MM-DD)[{today}]: ") or today

    """Kategorija"""
    print("\nKATEGORIJAS")
    for i, cat in enumerate(categories, 1):
        print(f"{i}) {cat}")

    try:
        cat_idx = int(input(f"Izvēlies (1-{len(categories)}): ")) - 1
        kategorija = categories[cat_idx]
    except (ValueError, IndexError):
        print(" Kļūda: Nepareiza izvēle, piešķirta kategorija 'Cits'.")
        kategorija = "Cits"

    """Summa ar pārbaudi"""

    try:
        summa = float(input("Summa (EUR): "))
        if summa <= 0:
            print("KĻŪDA. Summai jābūt pozitīvai.")
            return
    except ValueError:
        print("KĻŪDA. Summai jābūt skaitlim")
        return
    
    """Apraksts"""

    apraksts = input("Apraksts: ").strip()
    if not apraksts:
        apraksts = "Nav apraksts"
    
    """Pievienošana un saglabāšana"""

    jauns_ieraksts = {
        "datums": datums,
        "kategorija": kategorija,
        "summa": summa,
        "apraksts": apraksts
    }
    expenses.append(jauns_ieraksts)
    save_expenses(expenses)
    print(f"\n✓ Pievienots: {datums} | {kategorija} | {summa:.2f} EUR | {apraksts}")

def show_expenses(expenses):

    """"Parāda visus izdevumus"""
    if not expenses:
        print("\n Saraksts ir tukšs.")
        return

    print(f"\n{'Nr.':<3} | {'Datums':<10} | {'Kategorija':<15} | {'Summa':>10} | {'Apraksts'}")
    print("-" * 50)
    
    for i, exp in enumerate(expenses, 1):
        print(f"{i:<3} | {exp['datums']:<10} | {exp['kategorija']:<15} | {exp['summa']:>10.2f} | {exp['apraksts']}")
    
    print("-" * 50)
    print(f"{'KOPĀ:':>32} {sum_total(expenses):>10.2f} EUR")

def main():

    """galvenais programmas cikls"""

    expenses = load_expenses()
    while True:
        choice = show_menu()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "7":
            print("Uz redzēšanos!")
            break
        else:
            print("Nepareiza izvēle, mēģini vēlreiz.")

if __name__ == "__main__":
    main()


