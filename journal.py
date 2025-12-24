import pickle  # для бинарного файла
import csv  # для текстового файла
class Journal:
    def __init__(self, teacher):
        self.teacher = teacher  # какой учитель
        self.lessons = []  # список для занятий

    def add_lesson(self, lesson):
        self.lessons.append(lesson)  # просто добавляем

    def get_lessons_by_date(self, start_date, end_date):
        result = []  # сюда складываем подходящие
        for lesson in self.lessons:
            if start_date <= lesson.date <= end_date:  # если дата в диапазоне
                result.append(lesson)
        return result

    def calculate_total_hours(self, start_date, end_date):
        total = 0  # начинаем с нуля
        for lesson in self.get_lessons_by_date(start_date, end_date):
            total += lesson.hours  # складываем часы
        return total

    def save_to_file(self, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')  # разделитель точка с запятой

            # пишем заголовки
            writer.writerow(['Дата', 'Группа', 'Дисциплина', 'Тема', 'Часы'])

            # пишем каждое занятие
            for lesson in self.lessons:
                writer.writerow([
                    lesson.date,  # дата
                    lesson.group.get_name(),  # группа
                    lesson.discipline.get_name(),  # предмет
                    lesson.topic,  # тема
                    lesson.hours  # часы
                ])

    def save_pickle(self, filename):
        with open(filename, 'wb') as f:  # wb = запись бинарного
            pickle.dump(self.lessons, f)  # сохраняем список

    def load_pickle(self, filename):
        with open(filename, 'rb') as f:  # rb = чтение бинарного
            self.lessons = pickle.load(f)  # загружаем список