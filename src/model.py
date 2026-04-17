from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

def train_model(df):
    # Sort by time (IMPORTANT)
    df = df.sort_values("date")

    # Split (80% train, 20% test)
    split_index = int(len(df) * 0.8)

    train = df.iloc[:split_index]
    test = df.iloc[split_index:]

    # Features & target
    X_train = train.drop(["date", "product_id", "qty_sold"], axis=1)
    y_train = train["qty_sold"]

    X_test = test.drop(["date", "product_id", "qty_sold"], axis=1)
    y_test = test["qty_sold"]

    # Model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predict
    preds = model.predict(X_test)

    # Evaluate
    mae = mean_absolute_error(y_test, preds)

    print(f"\nTest MAE: {mae:.2f}")

    # Save model
    joblib.dump(model, "models/model.pkl")

    return model, preds, y_test