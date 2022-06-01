import csv
from datetime import datetime

current_date_and_time = datetime.now(tz=None)
weekday = current_date_and_time.weekday()

def main():
    while answer != 'quit':
        
        theme = get_theme()
        test_grades = get_test_grades()
        activity_grades = get_activity_grades()
        final_grade = get_final_grade(test_grades, activity_grades)
        situation = get_student_situation(theme, final_grade)





def get_theme():
    theme = input('Type the course that you studied: ')
    return theme

def get_test_grades():
    test_grade = int(input('Enter your test grade: '))
    percentual_grade = test_grade * 0.60
    return percentual_grade

def get_activity_grades():
    week01 = int(input('Enter your week01\'s activity grade: '))
    week02 = int(input('Enter your week02\'s activity grade: '))
    week03 = int(input('Enter your week03\'s activity grade: '))
    week04 = int(input('Enter your week04\'s activity grade: '))
    average = (week01 + week02 + week03 + week04) / 4
    percentual_grade = average * 0.40
    return percentual_grade


def get_final_grade(test_grade, activity_grade): 
    final_grade = test_grade + activity_grade
    return final_grade 




def get_student_situation(course, final_grade):
    print('\nYour Situation:')
    if final_grade >= 5:
        print(f'{course} {final_grade} - Approved')
    else: 
        print(f'{course} {final_grade} - Disapproved')
    
    
    
    
def print_elements(option): 
    break_line = "\n***********************************************\n"
    section_line = "***********************************************"
    header       = "*                UNIVESP - Grades Calculator                *"
    footer       = "*                           Thank you!                      *"

    if option == "header":
        print(f"{break_line}{header}{break_line}")
    elif option == "footer":
        print(f"{break_line}{footer}{break_line}")
        print(f"{current_date_and_time:%A %I:%M %p}")
    elif option == "break_line":
        print(f"{break_line}")
    elif option == "section_line":
        print(f"{section_line}")





if __name__ == "__main__":
    main()