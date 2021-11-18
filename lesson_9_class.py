class DataUser:  # класс
    # просто атрибуты класса - плохая практика
    # name = ""  # атрибут класса
    # ip = "0.0.0.0"  # атрибут класса
    # user_time = 0.0  # атрибут класса
    def __init__(self, name, ip, user_time):
        self.name = name  # атрибут экземпляра класса
        self.ip = ip
        self.user_time = user_time

    def __str__(self):
        return f"name: {self.name}, ip: {self.ip}, user_time: {self.user_time}"

    def __repr__(self):
        return f"{self.name}({self.user_time})"

    def increase_user_time(self, add_time):  # метод экземпляра класса
        self.user_time += add_time