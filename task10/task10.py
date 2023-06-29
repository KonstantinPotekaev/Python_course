from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, name: str, rase: str):
        self.__name = name
        self.__rase = rase

    @abstractmethod
    def speak(self):
        print('Animal Speaking')

    @abstractmethod
    def __str__(self):
        return f'{self.getName()} {self.getRase()}'

    def getName(self):
        return self.__name

    def getRase(self):
        return self.__rase


class Cat(Animal):

    def __init__(self, name: str, rase: str):
        super().__init__(name, rase)

    def speak(self):
        print('meow-meow')

    def __str__(self):
        return super().__str__()


class Bird(Animal):

    def __init__(self, name: str, rase: str, sound: str):
        super().__init__(name, rase)
        self.__sound = sound

    def speak(self):
        print(self.__sound)

    def __str__(self):
        return super().__str__()


class Factory(Cat, Bird):
    def make_animal(self, animal_type: str, *args, **kwargs):
        new_animal = self._get_maker(animal_type)
        return new_animal(*args, **kwargs)

    def __get_maker(self, animal_type: str):
        type = {"cat": Cat, "bird": Bird}
        return type[animal_type.lower()]


if __name__ == '__main__':
    b1 = Bird('bird', 'Bird', 'aaa')
    c1 = Cat('Cat', 'Cat')

    c2 = Factory('Cat', 'Cat')

    print(b1)
    print(c1)
    print(c2)
