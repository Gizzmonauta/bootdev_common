from typing import TypedDict, List, Dict


class Item(TypedDict):
    """Represents a purchased item."""
    price: float
    quantity: int


class Order(TypedDict):
    """Represents a customer order."""
    customer: str
    items: List[Item]

def _validate_order_structure(order: Order) -> None:
    """
    Validate that an order has the required structure.
    
    Args:
        order: A single order dictionary to validate.
        
    Raises:
        ValueError: If order or items are missing required fields.
    """
    if "customer" not in order or "items" not in order:
        raise ValueError("Each order must have 'customer' and 'items' fields.")
    
    for item in order["items"]:
        if "price" not in item or "quantity" not in item:
            raise ValueError("Each item must have 'price' and 'quantity' fields.")


def summarize_purchases(orders: List[Order]) -> Dict[str, float]:
    """
    Calculate total purchase amounts for each customer.
    
    Args:
        orders: List of orders, each containing customer name and items.
    
    Returns:
        Dictionary mapping customer names to their total purchase amounts.
        
    Raises:
        ValueError: If any order or item has invalid structure.
    """
    customer_totals: Dict[str, float] = {}
    
    for order in orders:
        _validate_order_structure(order)
        total = sum(item["price"] * item["quantity"] for item in order["items"])
        customer_totals[order["customer"]] = customer_totals.get(order["customer"], 0) + total

    return customer_totals