import numpy as np
from scipy.stats import norm

def calculate_inventory(preds, on_hand=100, lead_time=7, service_level=0.95):
    # Demand during lead time
    demand_lead_time = sum(preds[:lead_time])

    # Demand variability
    std_dev = np.std(preds)

    # Z-score for service level
    z = norm.ppf(service_level)

    # Safety Stock
    safety_stock = z * std_dev

    # Reorder Point
    reorder_point = demand_lead_time + safety_stock

    # Order Quantity
    order_qty = max(0, reorder_point - on_hand)

    return {
        "demand_lead_time": round(demand_lead_time, 2),
        "safety_stock": round(safety_stock, 2),
        "reorder_point": round(reorder_point, 2),
        "order_quantity": round(order_qty, 2)
    }