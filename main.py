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

    Args:
        gradebook (dict): of format like generate_gradebook()
        student (str): ПІБ
        activity (tuple[str, str]): ("Лабораторні роботи", "Лаба1")
        grade (float):

    Returns:
        dict: gradebook
    """

    ...

def read_grades_from_file(filepath: str) -> dict:
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

def get_average_students_grade(grades: dict, activity: None|list[tuple[str, str]]) -> float:
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

def get_average_grade(gradebook: dict, activity: None|list[tuple[str, str]]) -> float:
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



def main():


    # gradebook = read_grades_from_file("gradebook.json")
    ...



