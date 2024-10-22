class Student:
    def __init__(self, first_name, last_name, age, group):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.group = group


def find_students(students, search_first_name=None, search_last_name=None):
    matching_students = []
    for student in students:
        if (search_first_name is None or student.first_name == search_first_name) and \
           (search_last_name is None or student.last_name == search_last_name):
            matching_students.append(student)
    return matching_students


def select_student(matching_students):
    if len(matching_students) == 0:
        print("Студенты не найдены.")
        return

    if len(matching_students) == 1:
        selected_student = matching_students[0]
        print(f"Найден студент:\nФамилия: {selected_student.last_name}\nИмя: {selected_student.first_name}\nВозраст: {selected_student.age}\nГруппа: {selected_student.group}")
    else:
        print("Найдены следующие студенты:")
        for i, student in enumerate(matching_students):
            print(f"{i + 1}. Фамилия: {student.last_name}, Имя: {student.first_name}, Возраст: {student.age}, Группа: {student.group}")

        selection = int(input("Введите номер студента, чтобы выбрать его: ")) - 1

        if 0 <= selection < len(matching_students):
            selected_student = matching_students[selection]
            print(f"Вы выбрали студента:\nФамилия: {selected_student.last_name}\nИмя: {selected_student.first_name}\nВозраст: {selected_student.age}\nГруппа: {selected_student.group}")
        else:
            print("Некорректный выбор.")


def main():
    students = [
        Student("Иван", "Иванов", 20, "А"),
        Student("Алексей", "Петров", 21, "Б"),
        Student("Мария", "Сидорова", 22, "А"),
        Student("Анна", "Кузнецова", 23, "В"),
        Student("Дмитрий", "Смирнов", 20, "Б"),
        Student("Иван", "Иванов", 21, "Б"),
        Student("Иван", "Иванов", 22, "А"),
        Student("Алексей", "Петров", 21, "В"),
        Student("Дмитрий", "Иванов", 20, "А"),
        Student("Иван", "Петров", 22, "А"),
    ]

    search_input = input("Введите имя и фамилию для поиска (например, 'Иван Иванов'): ").strip()

    if search_input:
        parts = search_input.split()
        if len(parts) == 2:
            search_first_name = parts[0]
            search_last_name = parts[1]
        else:
            print("Пожалуйста, введите как имя, так и фамилию.")
            return
    else:
        print("Вы ничего не ввели.")
        return

    matching_students = find_students(students, search_first_name, search_last_name)
    select_student(matching_students)


if __name__ == "__main__":
    main()
