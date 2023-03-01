class Student:
    def __init__(self, Id, firstname, lastname, courseInfo):
        self.__courseInfo = courseInfo
        self.__firstname = firstname
        self.__lastname = lastname
        self.__Id = Id

    @property
    def get_id(self):
        return self.__Id

    @property
    def get_name(self):
        return [self.__firstname, self.__lastname]

    @property
    def get_courses(self):
        return [tuple(self.__courseInfo[i:i + 2]) for i in range(0, len(self.__courseInfo), 2)]

    @property
    def get_fname(self):
        return self.get_name[0]

    @property
    def get_lname(self):
        return self.get_name[1]

    @property
    def get_ccode(self):
        return [i[0] for i in self.get_courses]

    @property
    def get_grade(self):
        return [i[1] for i in self.get_courses]

st1 = Student('500000601', "Jane", "Doe",
              ["COMP1210", 80, "COMP1215", 60, "COMP2210", 50, "COMP1205", 60, "FOUN2003", 85, "COMP2220", 80])
credit_list = {'COMP1210': 3, 'COMP1215': 3, 'COMP1205': 3, 'COMP2210': 3, 'COMP2220': 3, 'COMP225': 3,
               'FOUN2003': 1}
q_plist = {"A+": 4.3, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "F1": 1.7,
           "F2": 1.3, "F3": 0.0}

def compute_letter_grade(num):
    grades = {'A+': range(100, 91, -1), 'A': range(90, 81, -1), 'A-': range(80, 71, -1), 'B+': range(70, 61, -1),
              'B': range(60, 51, -1), 'B-': range(50, 41, -1), 'C+': range(40, 31, -1), 'C': range(30, 21, -1),
              'C-': range(20, 11, -1), 'D': range(10, 1, -1), 'F': range(0, 0, -1)}
    return ''.join(k for k, v in grades.items() for i in v if num == i)

def calc_letter_grade(student):
    return [(i[0], compute_letter_grade(i[1])) for i in student.get_courses]

def convert_to_wtqp(course):
    return credit_list[course[0]], q_plist[course[1]]

def calc_gpa(studentRecord):
    return sum([i[0]*i[1] for i in [convert_to_wtqp(i) for i in calc_letter_grade(studentRecord)]])/4

def print_student_gpa(std):
    """Prints the students details and GPA"""
    print("Student Id:", std.get_id)
    print("Student name:", std.get_fname, std.get_lname)
    print('GPA: %.2f' % (calc_gpa(std)))

print_student_gpa(st1)
