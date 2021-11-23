####################################################################################################
# 1
from datetime import datetime


class FilesReader:
    def __init__(self, filename):
        self.filename = filename

    def get_domains(self):
        result = []
        with open(self.filename, "r") as file:
            for line in file.readlines():
                if line.startswith('.'):
                    result.append(line.strip()[1:])
                else:
                    result.append(line)  # на случай если где-то пропущена точка
            return result

    def get_names(self):
        result = []
        with open(self.filename, 'r') as file:
            for line in file.readlines():
                result.append(line.split('\t')[1])
        return result

    def get_dates(self):
        result = []
        with open(self.filename, "r") as file:
            for line in file.readlines():
                one_line = line.split(" - ")
                if len(one_line) > 1:
                    date_original = one_line[0]
                    day, month, year = date_original.split()
                    date_modified = datetime.strptime(f'{day[:-2]} {month} {year}', '%d %B %Y')
                    result.append(
                        {
                            'date_original': date_original,
                            'date_modified': datetime.strftime(date_modified, '%d/%m/%Y')
                        }
                    )
        return result




##########################################################################################################
# 2
class Unit:
    _max_health = 100  # добавила максимальные значения и шаги увеличения на тот случай, если нужно будет
    _max_force = 10  #  их менять в игре, и чтобы не пришлось перебирать для замены все функции
    _max_agility = 10
    _max_intelligence = 10
    _point_health_up = 10
    _point_force_up = 1
    _point_agility_up = 1
    _point_intelligence_up = 1



    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 100
        self.force = 1
        self.agility = 1
        self.intelligence = 1

    def increase_unit_health(self):
        if self.health <= Unit._max_health - Unit._point_health_up:
            self.health += Unit._point_health_up
        else:
            self.health = Unit._max_health


    def increase_unit_force(self):
        if self.force < Unit._max_force:
            self.force += Unit._point_force_up

    def increase_unit_agility(self):
        if self.agility < Unit._max_agility:
            self.agility += Unit._point_agility_up

    def increase_unit_intelligence(self):
        if self.intelligence < Unit._max_intelligence:
            self.intelligence += Unit._point_intelligence_up

    def __repr__(self):
        return f"name: {self.name}, clan: {self.clan}, health: {self.health}, " \
               f"force: {self.force}, agility: {self.agility}, intelligence: {self.intelligence}"

