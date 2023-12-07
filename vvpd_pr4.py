""""Определение оценки по её дате сдачи студентом"""
import datetime


def deadline_score(pass_date: str, deadline_date: str) -> int:
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
