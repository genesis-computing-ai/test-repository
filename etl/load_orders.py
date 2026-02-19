"""ETL pipeline that loads order data."""
import snowflake.connector

def load_orders():
    """Read from RAW.ORDERS and RAW.ORDER_ITEMS, write to ANALYTICS.FACT_ORDERS."""
    conn = snowflake.connector.connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ANALYTICS.FACT_ORDERS
        SELECT o.id, o.customer_id, o.order_date, oi.product_id, oi.quantity, oi.price
        FROM RAW.ORDERS o
        JOIN RAW.ORDER_ITEMS oi ON o.id = oi.order_id
    """)
    conn.close()