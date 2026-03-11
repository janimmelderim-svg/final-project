from storage import load_expenses, save_expenses
from logic import sum_total, filter_by_month, sum_by_category, get_available_months, is_valid_date
from datetime import date
from export import export_to_csv

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
    print("3) Filtrēt pēc mēneša")
    print("4) Kopsavilkums pa kategorijām")
    print("5) Dzēst izdevumu")
    print("6) Eksportēt uz CSV")
    print("7) Iziet")

    return input("\nIzvēlies darbību (1-7): ")

def add_expense(expenses):
    """"funkcija jauna izdevuma pievienošanai"""
    print("\n---  JAUNS IZDEVUMS ---")

    """Datums"""

    while True:
        today = date.today().isoformat()
        datums = input(f"Datums (YYYY-MM-DD) [{today}]: ") or today
        
        if is_valid_date(datums):
            break # Datums ir pareizs, izejam no cikla
        else:
            print("Kļūda: Nepareizs datuma formāts vai neeksistējošs datums (jābūt GGGG-MM-DD).")

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

def show_monthly_filter(expenses):

    """parāda mēnešu filtru"""

    months = get_available_months(expenses)
    if not months:
        print("\nNav datu, ko filtrēt.")
        return

    print("\nPieejamie mēneši:")
    for i, m in enumerate(months, 1):
        print(f" {i}) {m}")
    
    try:
        izvele = int(input("Izvēlies mēnesi: ")) - 1
        izveletais_menesis = months[izvele]
        filtered = filter_by_month(expenses, izveletais_menesis)
        
        print(f"\n{izveletais_menesis} izdevumi:")
        for exp in filtered:
            print(f"{exp['datums']} | {exp['summa']:>8.2f} EUR | {exp['kategorija']:<15} | {exp['apraksts']}")
        print(f"Kopā: {sum_total(filtered):.2f} EUR ({len(filtered)} ieraksti)")
    except (ValueError, IndexError):
        print(" Atcelts vai nepareiza izvēle.")

def show_summary(expenses):

    """parāda kategoriju summu"""

    summary = sum_by_category(expenses)
    if not summary:
        print("\n📭 Nav datu kopsavilkumam.")
        return
    print("\n--- KOPSAVILKUMS PA KATEGORIJĀM ---")
    for kat, kopa in summary.items():
        print(f"{kat:<20}: {kopa:>10.2f} EUR")

def delete_expense(expenses):

    """Parāda dzēšanu pēc nr."""

    if not expenses:
        print("\nNav ierakstu, ko dzēst.")
        return

    print("\nIzdevumi:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}) {exp['datums']} | {exp['summa']:.2f} EUR | {exp['apraksts']}")

    try:
        izvele = int(input("\nKuru dzēst? (numurs vai 0 lai atceltu): ")) - 1
        if izvele == -1: return
        
        removed = expenses.pop(izvele)
        save_expenses(expenses) # Saglabājam izmaiņas failā!
        print(f"✓ Dzēsts: {removed['datums']} | {removed['summa']} EUR | {removed['apraksts']}")
    except (ValueError, IndexError):
        print(" Kļūda: Nepareizs numurs.")

def main():

    """galvenais programmas cikls"""

    expenses = load_expenses()
    while True:
        choice = show_menu()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            show_monthly_filter(expenses)
        elif choice == "4":
            show_summary(expenses)
        elif choice == "5":
            delete_expense(expenses)
        elif choice == "6":
            default_name = "izdevumi.csv"
            name = input(f"Faila nosaukums [{default_name}]: ").strip() or default_name
    
            success, result = export_to_csv(expenses, name)
            if success:
                print(f"✓ Eksportēts: {len(expenses)} ieraksti -> {result}")
            else:
                print(f"Kļūda: {result}")
        elif choice == "7":
            print("Uz redzēšanos!")
            break
        else:
            print("Nepareiza izvēle, mēģini vēlreiz.")

if __name__ == "__main__":
    main()


