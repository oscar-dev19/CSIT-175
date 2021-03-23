"""A simple program that adds/removes/displays list of classes offered.
   Author: Oscar Lopez
   Date Last Modified: 3/18/21.
"""

from Assignments.asgn4_module import *
import random

classes_offered = ["Python", "Javascript", "PHP"]


def display_my_classes():
    """
    Displays all classes offered in a sorted manner.
    """
    n = 1
    for c in sorted(classes_offered):
        print(f'{n}:{c}')
        n+=1
       
def  add_class(class_):
    """Adds a given class to list of classes_offered.

    Args:
        class_ (String): class to be added to list of classes_offered.
    """
    classes_offered.append(class_)
    
def removeClass(class_):
    """Removes a class from the list of classes offered.

    Args:
        class_ (String): name of class to be removed from list of classes_offered.
    """
    classes_offered.remove(class_)
    
def guess_next():
    """Returns a random class from the list f classes offered.

    Returns:
        String: name of class in classes_offered list.
    """
    guess = random.randrange(0, len(classes_offered))
    return classes_offered[guess]

    


def main():
    print('ASSIGNMENT 5\n')
    print('List Of Classes I Teach:\n')
    display_my_classes()
    
    while(True):
        choice = input('Do you need to Add or Remove a class?(A/R)')
        if choice.upper() == 'A':
            while(True):
                added_class = input('Enter the name of the class you wish to add:')
            
                if is_field_blank(added_class):
                    print('Please enter a class.')
                    continue
                else:
                    if added_class not in classes_offered:
                        add_class(added_class)
                        print(f'{added_class} has been added to classes offered.')
                        break
                    else:
                        print(f'{added_class} is already in list of classes offered.')
                        continue
        elif choice.upper() == 'R':
            while(True):
                removed_class = input('Enter the name of the class you wish to remove:')
                if is_field_blank(removed_class):
                    print('Please enter a class you want to remove.')
                    continue
                elif removed_class not in classes_offered:
                    print(f'ERROR: {removed_class} is not in list of classes offered.')
                    continue
                else:
                    removeClass(removed_class)
                    print(f'{removed_class} has been removed from classes offered list.')
                    break
                
        elif is_field_blank(choice):
                print('\nList Of Classes I Teach:')
                display_my_classes()
                break
        
        else:
                print("You must choose an 'A' to Add or an 'R' to Remove a class")
                continue
        
    next = guess_next()
    print(f'\nThe next class you should teach is: {next}')
    print('\nEND OF ASSIGNMENT 5')
            
            
if __name__ == '__main__':
    main()
    