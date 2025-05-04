class Signal:
    def __init__(self):
        self._subscribers = []

    def connect(self, handler):
        self._subscribers.append(handler)

    def send(self, **kwargs):
        for handler in self._subscribers:
            handler(**kwargs)

# Инициализируем сигналы
user_created = Signal()
