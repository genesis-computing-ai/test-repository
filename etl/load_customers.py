"""ETL pipeline that loads customer data with addresses."""
import snowflake.connector

def load_customers():
    """Read from RAW.CUSTOMERS and RAW.ADDRESSES, write to ANALYTICS.DIM_CUSTOMERS."""
    conn = snowflake.connector.connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ANALYTICS.DIM_CUSTOMERS
        SELECT c.id, c.name, c.email, c.created_at, a.city, a.country
        FROM RAW.CUSTOMERS c
        LEFT JOIN RAW.ADDRESSES a ON c.id = a.customer_id
        WHERE c.created_at > CURRENT_DATE - 30
    """)
    conn.close()