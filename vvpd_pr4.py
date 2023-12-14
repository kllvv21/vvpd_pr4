""""Определение оценки по её дате сдачи студентом"""
import datetime


def deadline_score(pass_date: str, deadline_date: str) -> int:
    """
    Эта функция вычисляет балл за практическую на основе даты сдачи
    и даты дедлайна.

    Проверяет, соответствуют ли строки даты формату "дд.мм.гггг".
    Если формат неверен, возникает ошибка ValueError. После чего создаются datetime-объекты.
    Вычисляется разница между датой сдачи и датой дедлайна, исходя из количества дней после дедлайна
    определяется оценка.

    :param pass_date: Дата, когда задание было сдано.
    Оно должно быть в формате "дд.мм.гггг".

    :param deadline_date: Дата, когда задание было сдано.
    Оно должно быть в формате "дд.мм.гггг"

    :return: int: Оценка студента, исходя из даты сдачи и даты
    дедлайна

    Исключения:
    ValueError: Вызывается, если строка даты имеют неправильный
    формат или содержат нецифровые символы.

    Примеры использования:
    score = deadline_score("15.05.2022", "20.05.2022")
    print(score)  # Output: 5

    score = deadline_score("25.07.2022", "01.06.2022")
    print(score)  # Output: 0
    """
    try:
        if (pass_date[2] != '.'
                or pass_date[5] != '.'
                or deadline_date[2] != '.'
                or deadline_date[5] != '.'):
            raise ValueError
        if (not pass_date[:2].isdigit()
                or not pass_date[3:5].isdigit()
                or not pass_date[6:].isdigit()):
            raise ValueError
        if (not deadline_date[:2].isdigit()
                or not deadline_date[3:5].isdigit()
                or not deadline_date[6:].isdigit()):
            raise ValueError
        list_p_date = pass_date.split(".")
        list_d_date = deadline_date.split(".")
        d_date = datetime.date(int(list_d_date[2]),
                               int(list_d_date[1]),
                               int(list_d_date[0]))
        p_date = datetime.date(int(list_p_date[2]),
                               int(list_p_date[1]),
                               int(list_p_date[0]))
        delta = p_date - d_date
        if d_date >= p_date:
            return 5
        elif delta.days >= 29:
            return 0
        elif delta.days >= 22:
            return 1
        elif delta.days >= 15:
            return 2
        elif delta.days >= 8:
            return 3
        elif delta.days >= 1:
            return 4
    except ValueError:
        print("Увы, дата написана неправильно!")

def late_list (grades: dict, deadline_date: str) -> list:
    """
    Функция создает список студентов, кто сдал практическую после дедлайна.

    Функция принимает словарь grades с датами сдачи
    практической студентами и строку deadline_date с указанием дедлайна.
    Для этого, функция сначала проверяет правильность формата даты deadline_date
    и каждой даты из словаря grades.
    Затем, функция сравнивает даты сдачи работ каждого студента с указанным дедлайном
    и добавляет студентов, чьи работы были сданы после дедлайна, в список list_of_shame.
    В конце, функция возвращает список list_of_shame.

    :param grades: Словарь с оценками студентов, где ключ - имя студента (тип: str),
    значение - дата сдачи работы (str).

    :param deadline_date: Строка с указанием крайнего срока в формате "дд.мм.гггг".

    :return: list_of_shame: Список студентов, чьи работы были сданы после указанного  (list).

    Исключения:
    ValueError: Генерируется, если формат даты deadline_date
    или даты сдачи работы в словаре grades неправильный.

    Примеры:
    grades = {
    "Иванов": "10.05.2022",
    "Петров": "15.04.2022",
    "Сидоров": "30.04.2022"
    }
    deadline_date = "01.05.2022"
    late_list(grades, deadline_date) # Возвращает: ["Иванов", "Петров"]

    grades = {
    "Иванов": "25.06.2022",
    "Петров": "20.06.2022",
    "Сидоров": "15.06.2022"
    }
    deadline_date = "30.06.2022"
    late_list(grades, deadline_date) # Возвращает: []
    """
    list_of_shame = []
    try:
        if (deadline_date[2] != '.'
                or deadline_date[5] != '.'):
            raise ValueError
        if (not deadline_date[:2].isdigit()
                or not deadline_date[3:5].isdigit()
                or not deadline_date[6:].isdigit()):
            raise ValueError
        list_d_date = deadline_date.split(".")
        d_date = datetime.date(int(list_d_date[2]),
                               int(list_d_date[1]),
                               int(list_d_date[0]))
        for student, pass_date in grades.items():
            if (pass_date[2] != '.'
                    or pass_date[5] != '.'):
                raise ValueError
            if (not pass_date[:2].isdigit()
                    or not pass_date[3:5].isdigit()
                    or not pass_date[6:].isdigit()):
                raise ValueError
            list_p_date = pass_date.split(".")
            p_date = datetime.date(int(list_p_date[2]),
                                   int(list_p_date[1]),
                                   int(list_p_date[0]))
            if p_date > d_date:
                list_of_shame.append(student)
        return list_of_shame
    except ValueError:
        print("Увы, дата написана неправильно!")


def main():
    while True:
        try:
            print("Операция 1 - Определение оценки за работу")
            print("Операция 2 - Определение студентов, сдавших работу после дедлайна")
            code = input('Введите код операции: ')
            match code:
                case '1':
                    pass_date = input("Введите дату сдачи работы (dd.mm.yyyy): ")
                    deadline_date = input("Введите дату дедлайна работы (dd.mm.yyyy): ")
                    print(deadline_score(pass_date, deadline_date))
                case '2':
                    print(late_list({'Иванов': '03.09.2020', 'Петров': '01.09.2020'}, '02.09.2020'))
                case '3':
                    raise KeyboardInterrupt
        except KeyboardInterrupt:
            print("Программа прервана")
            print("До новой встречи!")
            break


main()


print(deadline_score('13.11.2023', '12.11.2023'))
print(late_list({'Иванов': '03.09.2020', 'Петров': '01.09.2020'}, '02.09.2020'))
print("Пока-пока!)")
print("cool!!!")

