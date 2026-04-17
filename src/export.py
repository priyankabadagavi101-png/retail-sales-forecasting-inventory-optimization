import pandas as pd

def export_results(df, preds, y_test, inventory):
    # Prediction vs actual
    results = pd.DataFrame({
        "Actual": y_test.values,
        "Predicted": preds
    })

    results.to_csv("outputs/predictions.csv", index=False)

    # Inventory report
    inventory_df = pd.DataFrame([inventory])
    inventory_df.to_csv("outputs/inventory_report.csv", index=False)

    print("\nCSV files saved in outputs/")