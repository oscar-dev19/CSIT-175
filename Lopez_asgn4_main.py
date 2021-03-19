from asgn4_module import *

age = ''
first_name= ''
last_name =''


def enterFirstName():
    f_name = input("What is your first name?")
    return f_name


def enterLastName():
    l_name = input("What is your last name?")
    return l_name


def enterAge():
    a= input("What is your age")
    return a



def isAgeOverHill(age):
    return age > 40


def main():
    print("Assignment 4\n")
    first_name = enterFirstName()
    while not first_name:
        first_name = enterFirstName()
        if is_field_blank(first_name):
            print("First Name must be Entered")
            continue
        else:
            break
    last_name = enterLastName()
    while not last_name:
        last_name = enterLastName()

        if not last_name:
            print("Last Name must be Entered")
            continue
        else:
            break
    age = str(enterAge())
    while not age:
        age = str(enterAge())
        if is_field_blank(age):
            print("Age must be entered.")
            continue
        if not is_field_a_number(age):
            print("Age must be a number")
            continue
        else:
            break
    if isAgeOverHill(int(age)):
        print("Well, {1} {2} it looks like you areover the hill".format(first_name,last_name))

    print("END OF ASSIGNMENT 4")


    if __name__=="__main__":
        main()
        

    
