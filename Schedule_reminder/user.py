import schedule
import command_ops
import time

def run():
    print("Welcome to Python's time reminder. Please first enter the command you would like to use: 'add' for adding another course, 'delete' to delete the existing course, 'list' to list all available courses and 'done' to start the time reminder"" ")
    schedule_obj = schedule.schedule()
    user = True
    while user:
        command = input("Enter the commands you want to use: ")
        while command not in ["done", "list", "delete", "add"]:
            command = input("Wrong command, type again: ")
        if command == "done":
            break
        elif command == "add":
            command_ops.add_course(schedule_obj)
        elif command == "list":
            course_list = schedule_obj.getlist()
            [print(x) for x in course_list] 
        elif command == "delete":
            command_ops.del_course(schedule_obj)



if __name__ == "__main__":
    run()