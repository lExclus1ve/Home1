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
            return average
        else:
            return 0

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
            return average
        else:
            return 0


    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.rate_hw_avg()}'
        return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

student1 = Student('Александр','Шкадин', 'м')
student2 = Student('Юлия', 'Шкадина', 'ж')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['C++']
student1.finished_courses += ['JS']
student1.finished_courses += ['Java']



# print(student1.name)
# print(student1.surname)
# print(student1.gender)


mentor1 = Mentor('Евгений', 'Васильевич')
mentor2 = Mentor('Валентина', 'Ивановна')
# print(mentor1.name)
# print(mentor1.surname)


lectur1 = Lecturer('Ольга', 'Валентиновна')
lectur2 = Lecturer('Людмила', 'Васильевна')
lectur1.courses_attached += ['Python']
lectur1.courses_attached += ['C++']

student1.rate_hw(lectur1, 'Python', 9) # Выставление оценки лектору, Студентом
student1.rate_hw(lectur1, 'C++', 10) # Выставление оценки лектору, Студентом

# print(lectur1) #Вывод лектора

# print(lectur1.grades)
# print(lectur1.name)
# print(lectur1.surname)

reviewer1 = Reviewer('Олег', 'Булыгин')
reviewer2 = Reviewer('Петр', 'Никитин')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['C++']
# print(reviewer1.name)
# print(reviewer1.surname)

reviewer1.rate_hw(student1, 'Python', 5) # Выставление оценки студенту, Лектором
reviewer1.rate_hw(student1, 'C++', 10) # Выставление оценки студенту, Лектором

# print(reviewer1) #Вывод проверяющего
print(student1) #Вывод студента