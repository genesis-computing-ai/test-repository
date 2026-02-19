"""Product catalog utilities - refactored, no more direct DB access."""
import json

def get_product_categories():
    """Return list of valid product categories."""
    return ["electronics", "clothing", "food", "furniture"]

def validate_product(product: dict) -> bool:
    """Validate a product dict has required fields."""
    required = {"id", "name", "category", "price"}
    return required.issubset(product.keys())