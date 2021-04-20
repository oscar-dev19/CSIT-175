from asgn8_Lopez_module import *

def main():
    print('Assignment 8\n')
    dataset = processData('A8_names.txt')
    displaySortedNames(dataset)
    
    while True:
        search_name = input("What is the first name you are looking for?")
        if not search_name:
            break
        try:
            fullname = findName(dataset,search_name)
            print(f'Your ful name is:{fullname}')
            
        except KeyError:
            print(f'I was unable to find{search_name} in the list.')
    print('End of Program')
    
if __name__ == '__main__':
    main()
    
