# Example of pure function

def calculate_final_price(base_price, tax_rate, discount):
    taxed_price = base_price * (1 + tax_rate)
    final_price = taxed_price * (1 - discount)
    return round(final_price, 2)

print(calculate_final_price(100, 0.2, 0.1))