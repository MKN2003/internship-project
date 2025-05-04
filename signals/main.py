from signals import user_created
import handlers 

def create_user(username):
    print(f"Creating user {username}...")
    
    user_created.send(username=username)

create_user("alice")