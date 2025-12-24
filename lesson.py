class Lesson:
    def __init__(self, date, topic, hours, discipline, group):
        self.date = date  # дата занятия
        self.topic = topic  # тема занятия
        self.hours = hours  # сколько часов
        self.discipline = discipline  # какой предмет
        self.group = group  # для какой группы

    def get_info(self):
        return f"{self.date}: {self.topic} ({self.hours} ч.)"  # красивая строка