import sys

# Generators vs List
regular_list = [x*x for x in range(10000)]

generator_list = (x*x for x in range(10000))

print(f"List size: {sys.getsizeof(regular_list)}")
print(f"Generator size: {sys.getsizeof(generator_list)}")

# Generator function

def countdown(n):
    print("Start countdown")
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)