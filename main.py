"""
Gradebook team git project

"""
import json


def read_students(filepath: str) -> list[tuple]:
    """
    reads information about students from csv file

    """
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.readlines()

        text = text[1::]

        student_list = []

        for line in text:
            line = line.strip()

            striped = line.split(',')

            student_list.append(tuple(striped))

        return student_list




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
    gradebook = {}

    for el in students:
        gradebook[el] = activities

    return gradebook



def update_grade(gradebook: dict[tuple: dict[str: dict[str: float]]], activities:\
                 dict[str: dict[str: float]], student: str, activity: tuple[str, str],\
                    grade: float | str) -> dict[tuple: dict[str: dict[str: float]]]:
    """
    updates given {students} grade for given {activity} in {gradebook}. Returns new gradebook
    student and activity are from user input. Might be invalid

    Args:
        gradebook (dict): of format like generate_gradebook()
        student (str): Прізвище, Ім'я
        activity (tuple[str, str]): ("Лабораторні роботи", "Лаба1")
        grade (float):

    Returns:
        dict: gradebook

    >>> gradebook = {
    ...     ("Doe", "John", "john.doe@example.com", "Group A"): {
    ...         "Лабораторні роботи": {
    ...             "Лаба1": 8.5,
    ...             "Лаба2": 7.0
    ...         },
    ...         "Практичні заняття": {
    ...             "Практика1": 9.0,
    ...             "Практика2": 8.5
    ...         }
    ...     },
    ...     ("Smith", "Jane", "jane.smith@example.com", "Group B"): {
    ...         "Лабораторні роботи": {
    ...             "Лаба1": 9.0,
    ...             "Лаба2": 8.0
    ...         },
    ...         "Практичні заняття": {
    ...             "Практика1": 8.0,
    ...             "Практика2": 7.0
    ...         }
    ...     },
    ...     ("Melnyk", "Ivan", "ivan.melnyk@example.com", "Group A"): {
    ...         "Лабораторні роботи": {
    ...             "Лаба1": 7.5,
    ...             "Лаба2": 8.0
    ...         },
    ...         "Практичні заняття": {
    ...             "Практика1": 8.5,
    ...             "Практика2": 7.0
    ...         }
    ...     }
    ... }
    >>> activities = {
    ...     "Лабораторні роботи": {
    ...         "Лаба1": 10.0,
    ...         "Лаба2": 12.0
    ...     },
    ...     "Практичні заняття": {
    ...         "Практика1": 10.0,
    ...         "Практика2": 12.0
    ...     }
    ... }
    >>> gradebook = update_grade(gradebook, activities, 'Smith Jane', \
        ('Лабораторні роботи', 'Лаба2'), 5.7)
    >>> print(gradebook[("Smith", "Jane", "jane.smith@example.com", "Group B")]\
        ['Лабораторні роботи']['Лаба2'])
    5.7
    >>> gradebook = update_grade(gradebook, activities, 'Doe John', \
        ('Практичні заняття', 'Практика1'), 7.7)
    >>> print(gradebook[("Doe", "John", "john.doe@example.com", "Group A")]\
        ['Практичні заняття']['Практика1'])
    7.7
    >>> gradebook = update_grade(gradebook, activities, 'Melnyk Ivan', \
        ('Лабораторні роботи', 'Лаба1'), 20.0)
    >>> print(gradebook[("Melnyk", "Ivan", "ivan.melnyk@example.com", "Group A")]\
        ['Лабораторні роботи']['Лаба1'])
    7.5
    >>> gradebook = update_grade(gradebook, activities, 'Smith Jane', \
        ('Практичні заняття', 'Практика2'), -3.0)
    >>> print(gradebook[("Smith", "Jane", "jane.smith@example.com", "Group B")]\
        ['Практичні заняття']['Практика2'])
    7.0
    >>> gradebook = update_grade(gradebook, activities, 'Doe John', \
        ('Практичні заняття', 'Практика1'), 'No grade')
    >>> print(gradebook[("Doe", "John", "john.doe@example.com", "Group A")]\
        ['Практичні заняття']['Практика1'])
    No grade
    """
    if isinstance(grade, float) and (grade < 0 or grade > activities[activity[0]][activity[1]]):
        return gradebook
    student = student.split()
    last_name, first_name = student[0], student[1]
    for student_profile in gradebook.keys():
        if student_profile[0] == last_name and student_profile[1] == first_name:
            gradebook[student_profile][activity[0]][activity[1]] = grade
    return gradebook



def read_gradebook(filepath: str, gradebook: dict|None = None) -> None|dict:
    """
    Read grades from file

    Args:
        filepath (str): _description_

        
    Returns:
        puts grades inplace if gradebook is specified
        Otherwise returns new gradebook from file
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = 'w+', encoding='utf_8', delete=False) as temp_file:
    ...     dump_gradebook({
    ...         ('Михасяк', 'Ярема', 'ucu@ucu.com'): {
    ...             "Фінальний іспит": {
    ...                 "Теоретичне завдання": 8,
    ...                 "Завдання на програмування": 22
    ...             }
    ...         },
    ...         ('Стрийська', 'Білочка', 'park@ucu.com', '+380933333333'): {
    ...             "Фінальний іспит": {
    ...                 "Теоретичне завдання": 2,
    ...                 "Завдання на програмування": 100
    ...             }
    ...         }
    ...     }, temp_file.name)
    ...     read_gradebook(temp_file.name)
    {('Михасяк', 'Ярема', 'ucu@ucu.com'): \
{'Фінальний іспит': {'Теоретичне завдання': 8, \
'Завдання на програмування': 22}}, \
('Стрийська', 'Білочка', 'park@ucu.com', '+380933333333'): \
{'Фінальний іспит': {'Теоретичне завдання': 2, \
'Завдання на програмування': 100}}}
    """
    loaded_gradebook = None
    try:
        with open(filepath, 'r', encoding = 'utf-8') as file:
            loaded_gradebook = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file path '{filepath}' does not exist.")
    except PermissionError:
        print(f"Error: Insufficient permissions to write to '{filepath}'.")
    except TypeError as err:
        print(f"Error: Failed to serialize gradebook to JSON - {err}.")
    except OSError as err:
        print(f"OS error occurred: {err}.")
    new_gradebook = {}
    for key in loaded_gradebook:
        new_key = tuple(key.split(","))
        new_gradebook[new_key] = loaded_gradebook[key]
    gradebook = new_gradebook
    return gradebook


def read_activities_from_sylabus(filepath: str) -> dict:
    """
    Reads activities types and max grades from a JSON file.

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        dict: Dictionary containing activities and their max grades.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data



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
    Deletes activity from activities. Inplace. Updates gradebook

    Args:
        activities (dict): dict of max acitivities grades
        activity (tuple[str, str]): ("Лабораторні роботи", "Лаба1")

    >>> gradebook = {('name1', 'surname1'): {'labs': {'lab1': 1, 'lab2': 3},
    ...               'tests': {'test1': 2.4}},
    ...              ('name2', 'surname2'): {'labs': {'lab1': 4, 'lab2': 2},
    ...               'tests': {'test1': 1.1}}}
    >>> activities = {'labs': {'lab1': 1, 'lab2': 3}, 'tests': {'test1': 3}}
    >>> delete_activity(gradebook, activities, ('tests', 'test1'))
    >>> print(f'{activities = }, {gradebook = }')
    activities = {'labs': {'lab1': 1, 'lab2': 3}}, \
gradebook = {('name1', 'surname1'): {'labs': {'lab1': 1, 'lab2': 3}}, \
('name2', 'surname2'): {'labs': {'lab1': 4, 'lab2': 2}}}
    """
    act, sub_act = activity
    if act in activities.keys():
        del activities[act][sub_act]
        if activities[act] == {}:
            del activities[act]

    for stud in gradebook:
        stud_activity = gradebook[stud]
        if act in stud_activity.keys():
            del stud_activity[act][sub_act]
            if stud_activity[act] == {}:
                del stud_activity[act]


def get_summary_grade(gradebook: dict) -> dict[tuple: float]:
    """
    gets sum of grades for each student
    """


def get_sorted_gradebook(gradebook: dict, activity: str=None) -> list[list[str, str, str, int]]:
    """
    Returns a sorted list of students based on the specified activity type, 
    or by total grade across all activities of this course if activity isn't specified.
    вивести впорядкований список студентів згідно якоїсь активності, типу активності, усього курсу.

    Args:
        gradebook (dict): A dictionary where keys are tuples with student info, 
        and values are dictionaries with grades.
        activity (str): A type of activity 
        
    Returns:
        list: A sorted list of students by their score for the specified 
        activity or total score if activity is None.

    Example:
    >>> gradebook = {
    ...     ('Щорс', 'Костянтин', 'kamilla48@satsiuk.net', 'A'): {
    ...         'Лабораторні роботи': {'Лабораторна робота 1': 2, 'Лабораторна робота 2': 2, 
    ...         'Лабораторна робота 3': 2},
    ...         'Проміжний іспит': {'Теоретичне завдання': 5, 'Завдання на програмування': 15},
    ...     }
    ... }
    >>> get_sorted_gradebook(gradebook, 'Лабораторні роботи')
    [['Щорс', 'Костянтин', 'kamilla48@satsiuk.net', 6]]
    
    >>> get_sorted_gradebook(gradebook)
    [['Щорс', 'Костянтин', 'kamilla48@satsiuk.net', 26]]
    >>> gradebook = {
    ...     ('Тимченко', 'Ольга', 'gduplii@ivanchenko-vernydub.net', 'B'): {
    ...         'Міні-проєкти': {'Міні-проєкт 1': 10, 'Міні-проєкт 2': 10}
    ...     },
    ...     ('Давиденко', 'Олекса', 'ieshchenkodmytro@gmail.com', 'B'): {
    ...         'Міні-проєкти': {'Міні-проєкт 1': 12, 'Міні-проєкт 2': 10}
    ...     }
    ... }
    >>> get_sorted_gradebook(gradebook, 'Міні-проєкти')
    [['Давиденко', 'Олекса', 'ieshchenkodmytro@gmail.com', 22], \
['Тимченко', 'Ольга', 'gduplii@ivanchenko-vernydub.net', 20]]
        
    """
    students_sorted = []
    for student, grades in gradebook.items():
        if activity:
            total_score = sum(grades.get(activity, {}).values())
        else:
            total_score = sum(
                score for each_activity in grades.values()
                for score in each_activity.values()
            )
        students_sorted.append(list(student[:3]) + [total_score])

        students_sorted.sort(key=lambda x: x[3], reverse=True)

    return students_sorted


# def get_average_students_grade(grades: dict, student: tuple, activity: None | list[tuple[str, str]]) -> float:
#     """
#     From given grades (gradebook[student]) generates average grade

#     Args:
#         grades (dict): _description_
#         activity (list[tuple[str, str]]): [("Лабораторні роботи", "Лаба1"), \
#             ("Лабораторні роботи", "Лаба2")]
#             if None -> all activities

#     Returns:
#         float: _description_
#     """
#     ...


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
    
    >>> gradebook = {
    ...     "Student1": {
    ...         "Лабораторні роботи": {"Лаба1": 3, "Лаба2": 4.0},
    ...         "Проміжний іспит": {"Теоретичне завдання": 5.0}
    ...     },
    ...     "Student2": {
    ...         "Лабораторні роботи": {"Лаба1": 4, "Лаба2": 5.0},
    ...         "Проміжний іспит": {"Теоретичне завдання": 4.0}
    ...     }
    ... }
    
    # Test average grade for all activities
    >>> get_average_grade(gradebook, None)
    4.2

    # Test average grade for a specific activity
    >>> get_average_grade(gradebook, [("Лабораторні роботи", "Лаба1")])
    3.5

    # Test average grade for multiple specific activities
    >>> get_average_grade(gradebook, [("Лабораторні роботи", "Лаба1"),\
          ("Лабораторні роботи", "Лаба2")])
    4.0

    # Test with an empty gradebook
    >>> get_average_grade({}, None)
    0.0

    # Test with activity not found in any student's record
    >>> get_average_grade(gradebook, [("Лабораторні роботи", "Лаба3")])
    0.0
    """
    total_grades = 0
    count = 0
    for _, activities in gradebook.items():
        if activity is not None:
            for act_type, act_name in activity:
                if act_type in activities and act_name in activities[act_type]:
                    total_grades += activities[act_type][act_name]
                    count += 1
        else:
            for act_type, sub_activities in activities.items():
                for grade in sub_activities.values():
                    total_grades += grade
                    count += 1

    if count == 0:
        return 0.0

    return round(total_grades / count, 1)


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

    >>> gradebook = {\
            ("Тимченко", "Ольга", "gduplii@ivanchenko-vernydub.net"): {\
                "Лабораторні роботи": {"Лаба1": 80, "Лаба2": 75},
                "Практичні заняття": {"Практика1": 85, "Практика2": 90}\
            },\
            ("Давиденко", "Олекса", "ieshchenkodmytro@gmail.com"): {\
                "Лабораторні роботи": {"Лаба1": 70, "Лаба2": 60},\
                "Практичні заняття": {"Практика1": 75, "Практика2": 80}\
            }\
        }\
    >>> gradebook_to_letters_grade(gradebook)
        {\
            ("Тимченко", "Ольга", "gduplii@ivanchenko-vernydub.net"): "B",\
            ("Давиденко", "Олекса", "ieshchenkodmytro@gmail.com"): "C"\
        }\
    """
    gradebook_with_letters = {}

    for student, info in gradebook.items():
        grades = []
        for e in info.values():
            for grade in e.values():
                grades.append(grade)

        sum_grades = sum(grades)
        if sum_grades > 100:
            sum_grades = 100
        grade_letter = grade_to_letters(sum_grades, 100.0)
        gradebook_with_letters[student] = grade_letter

    return gradebook_with_letters


def get_talons(gradebook: dict) -> list[tuple]:
    """
    returns list of students who got talon

    Args:
        gradebook (dict): _description_

    Returns:
        list[tuple]: [student_info]

    >>> gradebook = {\
            ("Тимченко", "Ольга", "gduplii@ivanchenko-vernydub.net"): {\
                "Лабораторні роботи": {"Лаба1": 40, "Лаба2": 20},\
                "Практичні заняття": {"Практика1": 35, "Практика2": 30}\
            },\
            ("Давиденко", "Олекса", "ieshchenkodmytro@gmail.com"): {\
                "Лабораторні роботи": {"Лаба1": 50, "Лаба2": 45},\
                "Практичні заняття": {"Практика1": 55, "Практика2": 58}\
            }\
        }\

    >>> get_talons(gradebook)

    """
    students_with_talon = []

    for students, info in gradebook.items():
        grades = []
        for e in info.values():
            for grade in e.values():
                grades.append(grade)
        sum_grades = sum(grades)
        if sum_grades < 60:
            students_with_talon.append(students)

    return students_with_talon


def dump_gradebook(gradebook: dict, filepath: str):
    """
    Ability to export the gradebook of all students, filled with grades, into a JSON file.

    Args:
        gradebook (dict): The gradebook with students' grades.
        filepath (str): The name of the file to write JSON.

    Doctests:
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode = 'w+', encoding='utf_8', delete=False) as temp_file:
    ...     dump_gradebook({
    ...         ('Михасяк', 'Ярема', 'ucu@ucu.com'): {
    ...             "Фінальний іспит": {
    ...                 "Теоретичне завдання": 8,
    ...                 "Завдання на програмування": 22
    ...             }
    ...         },
    ...         ('Стрийська', 'Білочка', 'parku@cu.com', '+380933333333'): {
    ...             "Фінальний іспит": {
    ...                 "Теоретичне завдання": 2,
    ...                 "Завдання на програмування": 100
    ...             }
    ...         }
    ...     }, temp_file.name)
    ...     print(temp_file.read())
    {
      "Михасяк,Ярема,ucu@ucu.com": {
        "Фінальний іспит": {
          "Теоретичне завдання": 8,
          "Завдання на програмування": 22
        }
      },
      "Стрийська,Білочка,parku@cu.com,+380933333333": {
        "Фінальний іспит": {
          "Теоретичне завдання": 2,
          "Завдання на програмування": 100
        }
      }
    }
    """

    if len(gradebook) == 0:
        print("The gradebook is empty.")
        return

    str_gradebook = {
        ','.join(key): value for key, value in gradebook.items()
    }

    try:
        with open(filepath, 'w', encoding = 'utf_8') as file:
            json.dump(str_gradebook, file, ensure_ascii = False, indent = 2)
    except FileNotFoundError:
        print(f"Error: The file path '{filepath}' does not exist.")
    except PermissionError:
        print(f"Error: Insufficient permissions to write to '{filepath}'.")
    except TypeError as err:
        print(f"Error: Failed to serialize gradebook to JSON - {err}.")
    except OSError as err:
        print(f"OS error occurred: {err}.")

    return


def dump_student_grades(gradebook: dict, student: tuple, filepath: str):
    """
    The possibility of exporting the gradebook for a student, filled with grades, to a JSON file.

    Args:
        gradebook (dict): The gradebook with students' grades.
        student (tuple): The student for whom grades are set.
        filepath (str): The name of the file to write JSON.
    
    Doctest:
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode='w+', encoding='utf_8', delete = False) as temp_file:
    ...     temp_filepath = temp_file.name
    ...     dump_student_grades({
    ...         ('Михасяк', 'Ярема', 'ucu@ucu.com'): {
    ...             "Фінальний іспит": {
    ...                 "Теоретичне завдання": 8,
    ...                 "Завдання на програмування": 22
    ...             }
    ...         },
    ...         ('Стрийська', 'Білочка', 'parku@ucu.com', '+380933333333'): {
    ...             "Фінальний іспит": {
    ...                 "Теоретичне завдання": 2,
    ...                 "Завдання на програмування": 100
    ...             }
    ...         }
    ...     }, ('Михасяк', 'Ярема', 'ucu@ucu.com') ,temp_filepath)
    ...     print(temp_file.read())
    {
      "Фінальний іспит": {
        "Теоретичне завдання": 8,
        "Завдання на програмування": 22
      }
    }
    """
    if len(student) == 0:
        print("The information of a student is empty.")
        return

    if len(gradebook) == 0:
        print("The gradebook is empty.")
        return

    if student not in gradebook:
        print("There is no student with given information in the gradebook")
        return

    student_info = gradebook[student]

    try:
        with open(filepath, 'w', encoding = 'utf-8') as file:
            json.dump(student_info, file, ensure_ascii = False, indent = 2)
    except FileNotFoundError:
        print(f"Error: The file path '{filepath}' does not exist.")
    except PermissionError:
        print(f"Error: Insufficient permissions to write to '{filepath}'.")
    except TypeError as err:
        print(f"Error: Failed to serialize gradebook to JSON - {err}.")
    except OSError as err:
        print(f"OS error occurred: {err}.")

    return


def get_student_by_info(students: list[tuple], student_info: str) -> tuple|None:
    """
    Returns first accurency of student by some provided info about them.

    Args:
        students (list[tuple]): list of infos about student [(name, surname, email, phone, ...)]
        student_info (str): any of info specified in student's tuple: name or surname or email or...

    Returns:
        tuple: (name, surname, email, phone, ...)
                None if students wasn't found

    >>> get_student_by_info([("Тимченко","Ольга","gduplii@ivanchenko-vernydub.net","B"), \
("Давиденко","Олекса","ieshchenkodmytro@gmail.com","B"), \
("Гаєвський","Володимир","qzasukha@pavlychenko.info","A"), \
("Сіробаба","Хома","iaroslav53@palii.info","B"), \
("Щорс","Костянтин","kamilla48@satsiuk.net","A")], "Сіробаба")
    ('Сіробаба', 'Хома', 'iaroslav53@palii.info', 'B')
    """
    for stud in students:
        if student_info in stud:
            return stud
    return None


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
                print(get_average_grade(gradebook, activities if activities else None))
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


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
