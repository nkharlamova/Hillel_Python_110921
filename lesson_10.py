# Область видимости в классах
# Наследование
from lesson10_class import AlphabetWorker
import json

dir_name = "alphabet"
alphabet_worker = AlphabetWorker(dir_name)
alphabet_worker._dir_name = "alphabet2"
# alphabet_worker._AlphabetWorker__crate_folder()  # плохая практика так делать!!!
# alphabet_worker.dir_name = "alphabet2"
# alphabet_worker.create_file("1")
alphabet_worker.create_alphabet_files()
# alphabet_worker.do_tanos_click()
print(dir(alphabet_worker))


class Unit:
    def __init__(self, name, strength, agility, intelligence):
        self._name = name
        self._strength = strength
        self._agility = agility
        self._intelligence = intelligence

    def __repr__(self):
        return f"{self._name}, params: {self._strength}, {self._agility}, {self._intelligence}"

    def level_up(self):
        self._strength += 1
        self._agility += 1
        self._intelligence += 1

    @property
    def name(self):
        return self._name

    @property
    def strength(self):
        return self._strength


class Barbarian(Unit):
    def __init__(self, name, strength, agility, intelligence, weapon):
        super().__init__(name, strength, agility, intelligence)
        self._weapon = weapon

    def __repr__(self):
        super_repr = super().__repr__()
        return super_repr + f" weapon: {self._weapon}"

    def increase_strength(self):
        self._strength += 1

    def level_up(self):
        super().level_up()
        self.increase_strength()


barbarian = Barbarian("Konan", 3, 1, 1, 'Axe')
print(barbarian)
# print(f"Герой {barbarian.name} имеет силу {barbarian.strength}")
barbarian.level_up()
print(barbarian)
# barbarian.increase_strength()
# print(barbarian)