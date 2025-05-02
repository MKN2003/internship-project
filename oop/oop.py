from abc import ABC, abstractmethod

# Абстрактный класс (инкапсуляция + полиморфизм)
class Animal(ABC):
    population = 0  # class variable

    def __init__(self, name: str, age: int):
        self._name = name             # protected attribute (инкапсуляция)
        self.__age = age              # private attribute
        Animal.population += 1

    def __str__(self):
        return f"{self.__class__.__name__} named {self._name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.__age})"

    def __eq__(self, other):
        return isinstance(other, Animal) and self._name == other._name

    def __len__(self):
        return self.__age

    @abstractmethod
    def make_sound(self):
        pass

    @classmethod
    def get_population(cls):
        return cls.population

    @staticmethod
    def is_valid_age(age):
        return 0 < age < 50


# Полиморфизм через переопределение метода
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

    def fetch(self):
        return f"{self._name} is fetching a stick."


class Cat(Animal):
    def make_sound(self):
        return "Meow!"

    def scratch(self):
        return f"{self._name} is scratching the couch."


# Ещё один базовый класс
class ServiceAnimal:
    def assist(self):
        return f"{self.__class__.__name__} is assisting its owner."


# Multiple inheritance: Dog + ServiceAnimal
class GuideDog(Dog, ServiceAnimal):
    def make_sound(self):
        return "Bark! (but calmly)"

    def guide(self):
        return f"{self._name} is guiding the person."

# Демонстрация работы
if __name__ == "__main__":
    dog = Dog("Rex", 5)
    cat = Cat("Whiskers", 3)
    guide = GuideDog("Buddy", 4)

    animals = [dog, cat, guide]

    for a in animals:
        print(str(a))                      # __str__
        print("Sound:", a.make_sound())    # полиморфизм
        print("Age (len):", len(a))        # __len__

    print("\nPopulation:", Animal.get_population())  # @classmethod
    print("Valid age check:", Animal.is_valid_age(100))  # @staticmethod

    print("\nEquality check:", dog == Dog("Rex", 5))  # __eq__
    print("Repr of cat:", repr(cat))                 # __repr__

    # Проверка множественного наследования
    print("MRO of GuideDog:", [cls.__name__ for cls in GuideDog.__mro__])
