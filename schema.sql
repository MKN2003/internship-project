CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    total NUMERIC NOT NULL
);

INSERT INTO customers (name) VALUES 
    ('Alice'),
    ('Bob'),
    ('Charlie');

INSERT INTO orders (customer_id, total) VALUES 
    (1, 100.50), 
    (1, 50.00), 
    (2, 80.00);