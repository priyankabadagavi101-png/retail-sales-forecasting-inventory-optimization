import matplotlib.pyplot as plt

def plot_sales(df):
    # Plot for one product
    product = df["product_id"].iloc[0]
    df_p = df[df["product_id"] == product]

    plt.figure()
    plt.plot(df_p["date"], df_p["qty_sold"])
    plt.title(f"Sales Trend - {product}")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("outputs/sales_trend.png")
    plt.close()


def plot_predictions(y_test, preds):
    plt.figure()
    plt.plot(y_test.values, label="Actual")
    plt.plot(preds, label="Predicted")
    plt.legend()
    plt.title("Actual vs Predicted")
    plt.tight_layout()
    plt.savefig("outputs/prediction_vs_actual.png")
    plt.close()