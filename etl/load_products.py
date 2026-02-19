"""ETL pipeline that loads product catalog."""
import snowflake.connector

def load_products():
    """Read from RAW.PRODUCTS and write to ANALYTICS.DIM_PRODUCTS."""
    conn = snowflake.connector.connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ANALYTICS.DIM_PRODUCTS
        SELECT id, name, category, price
        FROM RAW.PRODUCTS
    """)
    conn.close()