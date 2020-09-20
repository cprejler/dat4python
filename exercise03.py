


class Student():

    def __init__(self, name, gender, dataSheet, imageUrl):
        self.name = name,
        self.gender = gender,
        self.dataSheet = dataSheet,
        self.imageUrl = imageUrl

#Af en eller anden grund virker det her ikke. Får fejl AttributeError: 'tuple' object has no attribute 'getGradesAsList'
#Har tjekket nogle af de andres løsninger og de gør præcis det samme, jeg kan ikke se hvorfor mit ikke virker

    def getAvgGrade(self):
        grades = self.dataSheet.getGradesAsList()
        total = sum(grades)
        return total / len(grades)

class Course():

    def __init__(self, name, classRoom, teacher, ects, grade=0):
        self.name = name,
        self.classRoom = classRoom,
        self.teacher = teacher,
        self.ects = ects,
        self.grade = grade
        


    def __str__(self):
        return 'Course name: {name}, Classroom: {classRoom}, Teacher: {teacher}, Number of ECTS points granted from course completion {ects}'.format(name=self.name, classRoom=self.classRoom, teacher=self.teacher, ects=self.ects)



class DataSheet():

    def __init__(self, courses=[]):
        self.courses = courses

    def __repr__(self):
        return self.__str__()

    def getGradesAsList(self):
        gradeList = []
        for course in self.courses:
            gradeList.append(course.grade)

        return gradeList






history = Course('history', 'cl202', 'hans', 30, 5)
math = Course('math', 'cl102', 'georg', 40, 10)
physics = Course('physics', 'cl405', 'steve', 50, 3)

courses = [history, math, physics]

dataSheet = DataSheet(courses)

print(dataSheet.getGradesAsList())

casper = Student('casper', 'male', dataSheet,'google.com')

hans = Student('hans', 'male', dataSheet, 'coolshop.dk')

print(casper.getAvgGrade())



