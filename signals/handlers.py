from signals import user_created

def log_user_creation(username):
    print(f"[LOG] User created: {username}")

def send_welcome_email(username):
    print(f"[EMAIL] Welcome email sent to {username}")

# Подписываем обработчики
user_created.connect(log_user_creation)
user_created.connect(send_welcome_email)