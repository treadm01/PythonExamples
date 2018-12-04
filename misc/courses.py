from datetime import date

class Course:
    def __init__(self, department, code, title, *instructors): 
        self.department = department
        self.code = code
        self.title = title
        self.students = {}
        self.instructorLst = []
        for elem in instructors:
            self.instructorLst.append(elem)

    def __eq__(self, other):
        return ((self.department, self.code) == (other.department,
                other.code))

    def mark_attendance(self, date, *students):
        for elem in students:
            if date not in self.students:
                self.students[date] = elem
            else:
                self.students[date] += " " + elem

    def is_present(self, student):
        if student in self.students:
            return True
        return False

class CSISCourse(Course):
    def __init__(self, department, code, title, recorded=False):
        super().__init__(department, code, title)
        self.is_recorded = recorded
  
    def __le__(self, other):
        return ((self.code.lower()) <= (other.code.lower()))

    def isPrerequisite(self, other):
            return (self <= other)

class CourseCatalog:
    def __init__(self, courses):
        self.courses = courses
       
    def courses_by_department(self, department_name):
        lst = []
        for elem in self.courses:
            if elem.department == department_name:
                lst.append(elem)
        return lst
        
        
    def courses_by_search_term(self, search_snippet):
        lst = []
        for elem in self.courses:
            if search_snippet in elem.title:
                lst.append(elem)
        return lst
