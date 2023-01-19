

class schedule:
    def __init__(self):
        self.name = []
        self.date = []
        self.time = []
        self.list_all = []
    
    def add_course(self, name):
        self.list_all.append(name)
    
    def add_class(self, name):
        self.name.append(list(name)[0])

    def getlist(self):
        return self.list_all

    def del_course(self, name):
        self.list_all.remove(name)

    def removecourse(self, course):
        self.del_course(course)