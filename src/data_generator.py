import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2023-01-01", end="2023-12-31")
products = [f"P{i}" for i in range(1, 11)]  # 10 products

data = []

for product in products:
    base_demand = np.random.randint(20, 50)

    for date in dates:
        # Weekly seasonality (weekends high)
        if date.weekday() >= 5:
            demand = base_demand + np.random.randint(10, 20)
        else:
            demand = base_demand + np.random.randint(-5, 5)

        # Random noise
        demand += np.random.randint(-3, 3)

        # Ensure non-negative
        demand = max(0, demand)

        data.append([date, product, demand])

df = pd.DataFrame(data, columns=["date", "product_id", "qty_sold"])

df.to_csv("data/data.csv", index=False)

print("Dataset created successfully!")