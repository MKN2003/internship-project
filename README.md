# 📘 Python & Django Developer Notes

Добро пожаловать! Этот документ содержит краткие, но насыщенные примеры и объяснения по самым важным темам Python, Django, асинхронного программирования и баз данных.

---

## 🔹 Hashable vs Unhashable

Hashable объекты:
- Имеют `__hash__()` и `__eq__()`
- Могут быть ключами в словарях (`dict`)

Unhashable объекты:
- Изменяемые (например, `list`, `dict`, `set`)
- Не могут быть ключами в `dict`

```python
hash("abc")       # ✅ строка — hashable
hash((1, 2, 3))   # ✅ tuple без изменяемых элементов — hashable
hash([1, 2, 3])   # ❌ list — unhashable
```

---

## 🔹 Stack и Queue

- **Stack (стек)** — LIFO (Last In First Out)
- **Queue (очередь)** — FIFO (First In First Out)

```python
# Stack
stack = []
stack.append("item")
stack.pop()

# Queue
from collections import deque
queue = deque()
queue.append("item")
queue.popleft()
```

---

## 🔹 Как работает `dict` под капотом

- `dict` использует **хеш-таблицу**
- Ключ преобразуется через `hash()` → индекс массива
- Коллизии решаются через **open addressing** (линейный поиск следующего свободного места)

Быстрые операции: `O(1)` в среднем случае.

---

## 🔹 Магические методы (dunder methods)

```python
class User:
    def __str__(self):
        return "User string"

    def __repr__(self):
        return "User()"

    def __eq__(self, other):
        return self.id == other.id

    def __len__(self):
        return len(self.name)
```

- `__str__` — пользовательское представление
- `__repr__` — техническое представление
- `__eq__` — логика сравнения
- `__len__` — поддержка `len(obj)`

---

## 🔹 @classmethod vs @staticmethod

```python
class Book:
    @classmethod
    def from_json(cls, data):
        return cls(**data)

    @staticmethod
    def validate_title(title):
        return isinstance(title, str)
```

- `@classmethod` — имеет доступ к классу (`cls`)
- `@staticmethod` — как обычная функция внутри класса

---

## 🔹 Генераторы и генераторные выражения

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = (x**2 for x in range(10))
```

- **Lazy evaluation**
- Экономия памяти
- Полезны при обработке больших данных или потоков

---

## 🔹 Context Managers

```python
with open("file.txt") as f:
    data = f.read()
```

Создание своего менеджера:

```python
class MyCtx:
    def __enter__(self):
        print("Start")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("End")

with MyCtx():
    ...
```

---

## 🔹 OOP: Инкапсуляция, Наследование, Полиморфизм, MRO

```python
class Animal:
    def speak(self):
        print("...")

class Dog(Animal):
    def speak(self):
        print("Woof!")

# MRO
print(Dog.__mro__)
```

- **Инкапсуляция** — скрытие деталей реализации
- **Наследование** — повторное использование
- **Полиморфизм** — разные поведения одного интерфейса
- **MRO (C3 linearization)** — порядок разрешения методов

---

## 🔹 Functional Concepts

### ✅ Pure Function
```python
def add(x, y): return x + y
```

### ✅ Immutability
```python
x = (1, 2, 3)  # кортеж — неизменяем
```

### ✅ Recursion
```python
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)
```

### ✅ Higher-Order Functions
```python
def apply(fn, value): return fn(value)
```

### ✅ map / filter / reduce
```python
list(map(lambda x: x*2, [1,2,3]))
list(filter(lambda x: x > 1, [1,2,3]))
from functools import reduce
reduce(lambda x, y: x + y, [1,2,3])
```

---

## 🔹 Асинхронное программирование

```python
import asyncio

async def download():
    await asyncio.sleep(1)
    print("Downloaded!")

asyncio.run(download())
```

- `async/await` — корутины
- **Event loop** управляет задачами
- Ускоряет I/O-операции (сеть, файлы)

---

## 🔹 Django Middleware

```python
class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Before view")
        response = self.get_response(request)
        print("After view")
        return response
```

Позволяет вмешиваться в запрос/ответ на уровне фреймворка.

---

## 🔹 Django Signals

```python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

Реагируют на события: создание, обновление, удаление объектов.

---

## 🔹 ORM vs Raw SQL

- ORM (Django, SQLAlchemy): читаемо, безопасно
- Raw SQL: гибкость, контроль

```python
User.objects.raw("SELECT * FROM users WHERE id = %s", [user_id])
```

---

## 🔹 Gunicorn

WSGI-сервер для запуска Django-приложений в продакшене:

```bash
gunicorn myproject.wsgi:application
```

---

## 🔹 SQL JOINs

| Тип JOIN | Описание |
|----------|----------|
| INNER JOIN | Совпадающие записи |
| LEFT JOIN | Все из левой, + совпадающие из правой |
| RIGHT JOIN | Все из правой, + совпадающие из левой |
| FULL JOIN | Все записи из обеих таблиц |

```sql
SELECT * FROM a INNER JOIN b ON a.id = b.a_id;
```

---

## 🔹 Практика SQL без ORM

```sql
SELECT name FROM users
WHERE id NOT IN (
    SELECT user_id FROM orders
);
```

Понимание SQL помогает писать более эффективные запросы в ORM.

---
