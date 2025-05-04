import psycopg2

def run_query(query, description):
    print(f"\n--- {description} ---")
    with psycopg2.connect(
        dbname="shop_db",
        user="postgres",
        password="postgres",
        host="localhost",
        port=5432
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                print(row)

# INNER JOIN
inner_query = """
SELECT customers.name, orders.total
FROM customers
INNER JOIN orders ON customers.id = orders.customer_id;
"""

# LEFT JOIN
left_query = """
SELECT customers.name, orders.total
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id;
"""

# RIGHT JOIN
right_query = """
SELECT customers.name, orders.total
FROM customers
RIGHT JOIN orders ON customers.id = orders.customer_id;
"""

# FULL JOIN
full_query = """
SELECT customers.name, orders.total
FROM customers
FULL OUTER JOIN orders ON customers.id = orders.customer_id;
"""

run_query(inner_query, "INNER JOIN")
run_query(left_query, "LEFT JOIN")
run_query(right_query, "RIGHT JOIN")
run_query(full_query, "FULL OUTER JOIN")