"""ETL pipeline that loads inventory data."""
import snowflake.connector

def load_inventory():
    """Read from RAW.INVENTORY and write to ANALYTICS.DIM_INVENTORY."""
    conn = snowflake.connector.connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ANALYTICS.DIM_INVENTORY
        SELECT product_id, warehouse, quantity, last_updated
        FROM RAW.INVENTORY
        WHERE last_updated > CURRENT_DATE - 7
    """)
    conn.close()