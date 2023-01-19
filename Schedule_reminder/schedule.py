

class schedule:
    def __init__(self):
        self.name = []
        self.date = []
        self.course = dict()
        self.list_all = []
    
    def add_course(self, name):
        self.list_all.append(name)
    
    # def add_class(self, name):
    #     self.name.append(list(name)[0])
    
    def add_time(self, course):
        tokens = list(course.split())
        course_name = tokens[0]
        time = tokens[1]
        days = [tokens[i:i+3] for i in range(0, len(tokens[2]), 3)]
        dates = [x + " " + time for x in days]
        self.course[course_name] = dates

    def getlist(self):
        return self.list_all

    def del_course(self, name):
        self.list_all.remove(name)

    def removecourse(self, course):
        self.del_course(course)