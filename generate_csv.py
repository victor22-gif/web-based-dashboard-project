import pandas as pd
from random import choice, randint, uniform
from faker import Faker
import os

# Create fake data generator
fake = Faker()

# Sample product and prices
products = {
    'Coffee_mug': 10,
    'Notebook': 5,
    'T-shirt': 15,
    'Pen': 2,
    'USB Drive': 8,
    'Backpack': 25,
    'Water Bottle': 12,
    'Headphones': 30,
}
# Generate random sales data
data = []
for i in range(1000):
    product = choice(list(products.keys()))
    quantity = randint(1, 5)
    price = products[product]
    total = quantity * price
    address = fake.address().replace('\n', ',')
    order = {
        'order_id': 1000 + i,
        'order_date': fake.date_between(start_date='-120d', end_date='today'),
        'product': product,
        'quantity': quantity,
        'price': price,
        'total': total,
        'address': address
    }
    data.append(order)

# Convert to DataFrame
df = pd.DataFrame(data)
# Save to CSV
os.makedirs("web-based dashboard project/data", exist_ok=True)
csv_path = "web-based dashboard project/data/orders.csv"
df.to_csv(csv_path, index=False)

print(f"✅ orders.csv created at: {csv_path}")