"""
Gradebook team git project

"""
import json


def read_students(filepath: str) -> list[tuple]:
    """
    reads information about students from csv file

    """
    ...


def generate_gradebook(students: list[tuple], activities: dict[str: dict[str: float]]) \
        -> dict[tuple: dict[str: dict[str: float]]]:
    """
    generates gradebook based on students information and acitivities

    activities = {
        "Лабораторні роботи": {
            "Лаба 1": 0.0,
            "Лаба 2": 0.0,
            "Лаба 3": 0.0,
            "Лаба 4": 0.0,
        },
        "Тести": {
            "Тест1": 0.0,
            "Тест2": 0.0,
            "Тест3": 0.0,
            "Тест4": 0.0,
            "Тест5": 0.0,
        }
    }
    """
    ...


def update_grade(gradebook: dict, student: str, activity: tuple[str, str], grade: float) -> dict:
    """
    updates given {students} grade for given {activity} in {gradebook}. Returns new gradebook
    student and activity are from user input. Might be invalid

    Args:
        gradebook (dict): of format like generate_gradebook()
        student (str): ПІБ
        activity (tuple[str, str]): ("Лабораторні роботи", "Лаба1"). 
        grade (float):

    Returns:
        dict: gradebook
    """

    ...


def read_gradebook(filepath: str, gradebook: dict|None = None) -> None|dict:
    """
    Read grades from file

    Args:
        filepath (str): _description_

        
    Returns:
        puts grades inplace if gradebook is specified
        Otherwise returns new gradebook from file
    """
    ...


def read_activities_from_sylabus(filepath: str) -> dict:
    """
    reads activities types and max grades.

    Args:
        filepath (str): json file

    Returns:
        dict: activities_max
    """
    ...


def add_activity(gradebook: dict, activities: dict, activity: tuple[str, str], max_grade: float) -> None:
    """
    adds activity with max_grade to activities. Inplace. Updates gradebook

    Args:
        activities (dict): dict of max acitivities grades
        activity (tuple[str, str]): ("Лабораторні роботи", "Лаба1")
        max_grade (float): _description_

    """
    ...


def delete_activity(gradebook: dict, activities: dict, activity: tuple[str, str]) -> None:
    """
    deletes activity from activities. Inplace. Updates gradebook

    Args:
        activities (dict): dict of max acitivities grades
        activity (tuple[str, str]): ("Лабораторні роботи", "Лаба1")

    """
    ...


def get_summary_grade(gradebook: dict) -> dict[tuple: float]:
    """
    gets sum of grades for each student
    """


def get_sorted_gradebook(gradebook: dict, activity: str):
    """
    вивести впорядкований список студентів згідно якоїсь активності, типу активності, усього курсу.

    Args:
        gradebook (dict): _description_
        activity (str): _description_
    """
    ...


def get_average_students_grade(grades: dict, activity: None | list[tuple[str, str]]) -> float:
    """
    From given grades (gradebook[student]) generates average grade

    Args:
        grades (dict): _description_
        activity (list[tuple[str, str]]): [("Лабораторні роботи", "Лаба1"), \
            ("Лабораторні роботи", "Лаба2")]
            if None -> all activities

    Returns:
        float: _description_
    """
    ...


def get_average_grade(gradebook: dict, activity: None | list[tuple[str, str]]) -> float:
    """
    вивести середній бал усіх студентів по одній або декільком активностям.

    Args:
        gradebook (dict): _description_
        activity (list[tuple[str, str]]): [("Лабораторні роботи", "Лаба1"), \
            ("Лабораторні роботи", "Лаба2")]
            if None -> all activities

    Returns:
        float: _description_
    """
    ...


def grade_to_letters(grade: float, max_grade: float) -> str:
    """
    transforms grade to letter

    Args:
        grade (float): _description_

    Returns:
        str: _description_
    """
    ...


def gradebook_to_letters_grade(gradebook: dict) -> dict[tuple, str]:
    """
    вивести список студентів з балом, що перетворений у відповідну літеру A-E згідно силабусу цього курсу.

    Returns:
        list[tuple[tuple, float]] -- list of (student_info, grade)
    """
    ...


def get_talons(gradebook: dict) -> list[tuple]:
    """
    returns list of students who got talon

    Args:
        gradebook (dict): _description_

    Returns:
        list[tuple]: [student_info, ]
    """
    ...


def dump_gradebook(gradebook: dict, filepath: str):
    """
    можливість вивантаження грейдбуку усіх студентів, заповненим оцінками у json файл.

    Args:
        gradebook (dict): _description_
        filepath (str): _description_
    """
    ...


def dump_student_grades(gradebook: dict, student: tuple, filepath: str):
    """
    можливість вивантаження грейдбуку для студента, заповненим оцінками у json файл.

    Args:
        gradebook (dict): _description_
        student (tuple): _description_
        filepath (str): _description_
    """
    ...


def get_student_by_info(student: list[tuple], student_info: str) -> tuple:
    """Микита напише всьо чікі-пукі

    Args:
        student (list[tuple]): _description_
        student_info (str): _description_

    Returns:
        tuple: _description_
    """


def main():
    """
    Main
    """
    students = read_students("students.csv")
    activities = read_activities_from_sylabus("sylabus.json")
    gradebook = generate_gradebook(students, activities)

    while True:
        print('''Введіть номер опції: (Enter to quit)
            1 -- стягнути оцінки з файлу
            2 -- додати оцінку
            3 -- додати тип роботи
            4 -- вивести сумарний бал по кожному студентові згідно активності
            5 -- вивести впорядкований список студентів
            6 -- вивести середній бал усіх студентів по активності
             7 -- вивести список студентів з балом від Е до А
            8 -- вивести список студентів, які отримали талон
            9 -- зберегти журнал оцінок в файл
            10 -- зберегти журнал оцінок певного студента
        ''')
        inp = input("Опція: ")
        if inp == "":
            break
        try:
            inp = int(inp)
        except ValueError:
            print("Опція має бути дійсним числом")
            continue

        match inp:
            case 1:
                read_gradebook("gradebook.json", gradebook)
            case 2:
                stud = input("Введіть ПІБ студента: ")
                activity_type = input("Введіть тип роботи за яку виставити оцінку: ")
                activity = input("Введіть роботу за яку виставити оцінку: ")
                grade = input("Введіть оцінку: ")
                try:
                    grade = float(grade)
                except ValueError: 
                    print("Оцінка має бути дійсним числом з крапкою")
                    continue

                gradebook = update_grade(gradebook, stud, (activity_type, activity), grade)
            case 3:
                activity_type = input("Введіть тип роботи за яку виставити оцінку: ")
                activity = input("Введіть роботу за яку виставити оцінку: ")
                max_grade = input("Введіть максимальну оцінку за активність: ")
                try:
                    max_grade = float(max_grade)
                except ValueError:
                    print("Оцінка має бути дійсним числом з крапкою")
                    continue

                add_activity(gradebook, activities, (activity_type, activity), max_grade)
            case 4: 
                print(get_summary_grade(gradebook))
            case 5:
                activity = input("Введіть активність для сортування: (нічого для сортування по всіх)")
                print(get_sorted_gradebook(gradebook, activity))            
            case 6:
                activities = []
                while True:
                    activity_type = input("Введіть тип роботи: (Enter to quit)")
                    if activity_type == "":
                        break
                    activity = input("Введіть назву роботи: (Enter to quit)")
                    if activity == "":
                        break
                    activities.append((activity_type, activity))
                print(get_average_students_grade(gradebook, activities if activities else None))
            case 7:
                print(gradebook_to_letters_grade(gradebook))
            case 8:
                print(get_talons(gradebook))
            case 9:
                filepath = input("Введіть шлях файлу для збереження")
                dump_gradebook(gradebook, filepath)
            case 10:
                filepath = input("Введіть шлях файлу для збереження")
                student = input("Введіть будь-які контактні дані студента")
                student = get_student_by_info(student)
                if student is None:
                    print("Не знайдено такого студента: ")
                    continue
                dump_student_grades(gradebook, student, filepath)
            case _:
                print("Опція має бути в межах від 1 до 10")


