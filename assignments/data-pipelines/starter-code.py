import csv

INPUT_FILE = "sales_data.csv"
OUTPUT_FILE = "processed_sales.csv"


def load_data(filename):
    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]


def clean_data(rows):
    cleaned = []
    for row in rows:
        quantity = row.get("quantity", "").strip()
        price = row.get("price", "").strip()
        if not quantity or not price:
            continue
        try:
            row["quantity"] = int(quantity)
            row["price"] = float(price)
        except ValueError:
            continue
        row["total_sales"] = row["quantity"] * row["price"]
        cleaned.append(row)
    return cleaned


def save_data(filename, rows):
    if not rows:
        return
    fieldnames = list(rows[0].keys())
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def summarize(rows):
    print(f"Rows loaded: {len(rows)}")
    if not rows:
        print("No valid records to process.")
        return

    total_sales = sum(row["total_sales"] for row in rows)
    print(f"Total sales: ${total_sales:.2f}")

    best_product = max(rows, key=lambda r: r["total_sales"])
    print(f"Top product by sales: {best_product['product']} (${best_product['total_sales']:.2f})")


def main():
    rows = load_data(INPUT_FILE)
    print("Loaded data from", INPUT_FILE)
    print(f"Dataset rows: {len(rows)}")

    cleaned = clean_data(rows)
    summarize(cleaned)

    save_data(OUTPUT_FILE, cleaned)
    print(f"Saved cleaned data to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
