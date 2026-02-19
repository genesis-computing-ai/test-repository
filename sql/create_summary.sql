-- Create daily revenue summary from fact_orders and dim_products
CREATE OR REPLACE TABLE ANALYTICS.DAILY_REVENUE AS
SELECT
    o.order_date,
    p.category,
    SUM(o.quantity * o.price) AS total_revenue,
    COUNT(DISTINCT o.id) AS order_count
FROM ANALYTICS.FACT_ORDERS o
JOIN ANALYTICS.DIM_PRODUCTS p ON o.product_id = p.id
GROUP BY o.order_date, p.category;