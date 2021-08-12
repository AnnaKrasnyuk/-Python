from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def amount(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        super().__init__(size)

    @property
    def amount(self):
        return round(self.size/6.5+0.5)


class Suit(Clothes):
    def __init__(self, size):
        super().__init__(size)

    @property
    def amount(self):
        return round(self.size*2+0.3)


coat = Coat(int(input('Размер пальто: ')))
print('Расход ткани на пальто:', coat.amount)
suit = Suit(int(input('Размер костюма: ')))
print('Расход ткани на костюм:', suit.amount)
print('Общий расход ткани =', coat.amount+suit.amount)
