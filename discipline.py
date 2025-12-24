class Discipline:
    def __init__(self, name, total_hours):
        self.name = name  # название предмета
        self.total_hours = total_hours  # всего часов

    def get_name(self):
        return self.name  # просто возвращаем название