# Example of recursive function

categories = {
    "Electronics": {
        "Phones": {
            "Smartphones": {},
            "Feature Phones": {}
        },
        "Laptops": {
            "Ultrabooks": {},
            "Gaming": {}
        }
    },
    "Books": {
        "Fiction": {},
        "Non-Fiction": {}
    }
}

def print_tree(tree, indent=0):
    for category, subcategories in tree.items():
        print("  " * indent + category)
        print_tree(subcategories, indent + 1)

print_tree(categories)