"""DEPRECATED: Old loader that will be removed."""
import snowflake.connector

def load_legacy():
    """Read from RAW.LEGACY_DATA and write to STAGING.LEGACY_TABLE."""
    conn = snowflake.connector.connect()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO STAGING.LEGACY_TABLE
        SELECT * FROM RAW.LEGACY_DATA
    """)
    conn.close()