import time

def add_course(schedule):
    course = input("Enter the course details in respective order: name, time, date. Use hour:minute format for time and Mon, Tue, Wed, Thu, Fri, Sat Sun for dates, for courses with multiple dates write them together without space: ")
    while len(list(course.split())) != 3:
        print("Invalid input:, make sure to type course name without whitespace and do the same thing for the rest of the tokens, try again: ")
    
    schedule.add_course(course)
    pass

def del_course(schedule):
    course = input("Enter course details to delete, remember to enter the right details correctly as originally provided, use 'list' command to aid with this process: ")
    if course == "list":
        print(schedule.getlist())  
    while len(list(course.split())) != 3:
        course = input("Wrong input format, please retype according the format and provide the correct details: ")
    list_course = schedule.getlist()

    if course not in list_course:
        print("Course not found! Try again.")
    else:
        schedule.removecourse(course)

if __name__ == "__main__":
    

    pass