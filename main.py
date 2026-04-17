from src.preprocess import load_data, basic_checks, clean_data, add_time_features
from src.features import create_features
from src.model import train_model
from src.inventory import calculate_inventory
from src.visualize import plot_sales, plot_predictions
from src.export import export_results

# -----------------------------
# 1. Load Data
# -----------------------------
df = load_data("data/data.csv")

# -----------------------------
# 2. Basic Checks
# -----------------------------
basic_checks(df)

# -----------------------------
# 3. Data Cleaning
# -----------------------------
df = clean_data(df)

# -----------------------------
# 4. Time Features
# -----------------------------
df = add_time_features(df)

# -----------------------------
# 5. Feature Engineering
# -----------------------------
df = create_features(df)

# -----------------------------
# 6. Model Training
# -----------------------------
model, preds, y_test = train_model(df)

# -----------------------------
# 7. Inventory Optimization
# -----------------------------
inventory = calculate_inventory(preds)

print("\nInventory Decision:")
for k, v in inventory.items():
    print(f"{k}: {v}")

# -----------------------------
# 8. Visualization
# -----------------------------
plot_sales(df)
plot_predictions(y_test, preds)

# -----------------------------
# 9. Export Results
# -----------------------------
export_results(df, preds, y_test, inventory)

print("\nAll outputs saved in outputs/")