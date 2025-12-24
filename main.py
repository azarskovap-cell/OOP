from teacher import Teacher
from group import Group
from discipline import Discipline
from lesson import Lesson
from journal import Journal
from excel_report import ExcelReport  # оставляем Excel


def main():
    # создаем учителя
    teacher = Teacher("Иванов П.С.", "Старший преподаватель")

    # создаем группы
    group1 = Group("ИС-22", 25)
    group2 = Group("ИС-23", 28)

    # создаем предметы
    disc1 = Discipline("ООП", 72)
    disc2 = Discipline("Базы данных", 64)

    # создаем журнал
    journal = Journal(teacher)

    # добавляем занятия
    journal.add_lesson(Lesson("2025-11-01", "Введение в ООП", 2, disc1, group1))
    journal.add_lesson(Lesson("2025-11-03", "Классы и объекты", 2, disc1, group1))
    journal.add_lesson(Lesson("2025-11-05", "SQL основы", 2, disc2, group2))
    journal.add_lesson(Lesson("2025-11-08", "Транзакции", 2, disc2, group2))
    journal.add_lesson(Lesson("2025-11-10", "Наследование", 2, disc1, group1))

    # сохраняем в файлы
    journal.save_to_file("lessons.txt")  # текстовый файл
    journal.save_pickle("lessons.pkl")  # бинарный файл

    # создаем Excel отчет (ИСПРАВЛЕНО)
    report = ExcelReport(journal)
    excel_file = report.generate("2025-11-01", "2025-11-30", "teacher_report.xlsx")

    # выводим информацию
    print(f"Преподаватель: {teacher.get_name()}")
    print(f"Всего занятий: {len(journal.lessons)}")
    print(f"Часов за ноябрь: {journal.calculate_total_hours('2025-11-01', '2025-11-30')}")
    print("Данные сохранены в lessons.txt и lessons.pkl")
    print(f"Excel отчёт сохранён в: {excel_file}")


if __name__ == "__main__":
    main()