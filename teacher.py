class Teacher:
    def __init__(self, name, position):
        self.name = name  # имя учителя
        self.position = position  # должность

    def get_name(self):
        return self.name  # просто возвращаем имя