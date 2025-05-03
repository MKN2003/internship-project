from functools import reduce

# Examples of lambda functions

transactions = [105.5, -20.0, 99.99, -5.25, 150.0, -30.0]

# Rounds every sum
rounded = list(map(lambda x: round(x, 2), transactions))

# Leaving onlny positiv profit
income = list(filter(lambda x: x > 0, rounded))

# Calculating total profit
total_income = reduce(lambda acc, x: acc + x, income)

print("Income transactions:", income)
print("Total income:", total_income)