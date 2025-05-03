# Example of immutability concept

def update_profile(user, new_email):
    return {**user, "email": new_email}

user1 = {"id": 1, "name": "Alice", "email": "old@example.com"}
user2 = update_profile(user1, "new@example.com")

print(user1) 
print(user2)  