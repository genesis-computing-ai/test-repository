"""ETL pipeline that loads customer data from raw to analytics."""
import snowflake.connector

def load_customers():
    """Read from RAW.CUSTOMERS and write to ANALYTICS.DIM_CUSTOMERS."""
    conn = snowflake.connector.connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ANALYTICS.DIM_CUSTOMERS
        SELECT id, name, email, created_at
        FROM RAW.CUSTOMERS
        WHERE created_at > CURRENT_DATE - 30
    """)
    conn.close()