class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in lectur.courses_attached and course in self.courses_in_progress and 0 < grade <= 10:
            if course in lectur.grades:
                lectur.grades[course] += [grade]
            else:
                lectur.grades[course] = [grade]
        else:
            return 'Ошибка'

    def rate_hw_avg(self):
        sum = 0
        quantity = 0
        if len(self.grades) != 0:
            for val in self.grades.values():
                for grade in val:
                    sum += grade
                    quantity += 1
                    average = sum / quantity
            return round(average, 1)
        else:
            return 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            return self.rate_hw_avg() < other.rate_hw_avg()

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.rate_hw_avg()} ' \
              f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self,name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_hw_avg(self):
        sum = 0
        quantity = 0
        if len(self.grades) != 0:
            for val in self.grades.values():
                for grade in val:
                    sum += grade
                    quantity += 1
                    average = sum / quantity
            return round(average, 1)
        else:
            return 0


    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.rate_hw_avg()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return self.rate_hw_avg() < other.rate_hw_avg()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and 0 < grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res



student_list = ['Шкадин', 'Петров']
lectur_list = ['Сергеев', 'Антипов']

def average_hw_student(students, courses):
    sum = 0
    quantity = 0
    for student in students:
        # if student in
        print(student)

average_hw_student(putin.__dict__, 'Python')


shkadin = Student('Шкадин', 'Александр', 'м')
shkadin.courses_in_progress += ['C++']
shkadin.courses_in_progress += ['Python']

petrov = Student('Иван', 'Петров', 'м')
petrov.courses_in_progress += ['C++']
petrov.finished_courses += ['Python']

sergeev = Lecturer('Пётр', 'Сергеев')
sergeev.courses_attached += ['C++']
sergeev.courses_attached += ['Python']

antipov = Lecturer('Юрий', 'Антипов')
antipov.courses_attached += ['C++']

pupkin = Reviewer('Алексей', 'Пупкин')
pupkin.courses_attached += ['C++']

putin = Reviewer('Владимир', 'Путин')
putin.courses_attached += ['Python']
putin.courses_attached += ['C++']


shkadin.rate_hw(sergeev, 'Python', 7)
shkadin.rate_hw(sergeev, 'C++', 10)
shkadin.rate_hw(antipov, 'C++', 8)
shkadin.rate_hw(antipov, 'C++', 4)

putin.rate_hw(shkadin, 'Python', 7)
putin.rate_hw(shkadin, 'Python', 10)
putin.rate_hw(shkadin, 'Python', 5)
putin.rate_hw(petrov, 'C++', 4)
putin.rate_hw(petrov, 'C++', 8)
putin.rate_hw(petrov, 'C++', 3)


# print(shkadin)
# print(f'')
# print(petrov)
# print(f'')
# print(sergeev)
# print(f'')
# print(antipov)
# print(f'')
# print(pupkin)
# print(f'')
# print(putin)
#
#
# print(shkadin > antipov)
# print(sergeev > petrov)
