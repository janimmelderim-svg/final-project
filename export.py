import csv

def export_to_csv(expenses, filename="izdevumi.csv"):

    """Eksportē izdevumu sarakstu uz CSV failu."""

    if not expenses:
        return False, "Nav datu, ko eksportēt."
    
    if not filename.endswith(".csv"):
        filename += ".csv"

    try:
        with open(filename, mode="w", encoding="utf-8-sig", newline="") as f:
            fieldnames = ["datums", "kategorija", "summa", "apraksts"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(expenses)
            
        return True, filename
    except Exception as e:
        return False, str(e)