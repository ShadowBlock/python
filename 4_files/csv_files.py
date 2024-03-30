import csv

rows = []

with open('inventory.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        rows.append(row)

    csv_file.close()

def save_product(id: int, name: str, category: str, price: float, quantity: int):
    """Save the product to a csv file."""
    if price < 0 or quantity < 0:
        return False
    with open('inventory.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        value = 0
        for list in rows:
            if str(id) == list[0]:
                csv_writer.writerow([id, name, category, price, quantity])
                value = 1
            else:
                csv_writer.writerow(list)

        if value == 1:
            return True
        else:
            csv_writer.writerow([id, name, category, price, quantity])
            return True


def remove_product(id: int):
    """Remove the product based on id."""
    with open('inventory.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        for list in rows:
            if str(id) == list[0]:
                continue
            else:
                csv_writer.writerow(list)


def get_product_quantity(id: int):
    """Get product quantity from id."""
    for list in rows:
        if str(id) == list[0]:
            return int(list[4])
    return 0


def get_products_of_category(category: str):
    """Get all products from category."""
    all_ids = set()
    for list in rows:
        if category == list[2]:
            all_ids.add(int(list[0]))
    return all_ids
