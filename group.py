class Group:
    def __init__(self, name, student_count):
        self.name = name  # название группы
        self.student_count = student_count  # сколько студентов

    def get_name(self):
        return self.name  # просто возвращаем название