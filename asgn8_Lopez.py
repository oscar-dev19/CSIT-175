from asgn8_Lopez_module import *

def main():
    print('Assignment 8\n')
    """Processes names from data file before start of program"""
    
    dataset = processData('A8_names.txt')
    displaySortedNames(dataset)
    
    while True:
        search_name = input("What is the first name you are looking for? ")
        """assures first name doesnt have to be capitalized."""
        search_name = search_name.title()
        """removing unecessary white space"""
        search_name = search_name.strip()
        if not search_name:
            break
        try:
            fullname = findName(dataset,search_name)
            print(f'Your full name is: {fullname}') 
        except KeyError:
            print(f'I was unable to find {search_name} in the list.')
    print('End of Program')
    
if __name__ == '__main__':
    main()
    
