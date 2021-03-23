import os


items = list()

def open_file(filename):
    """Opens a file with given filename.

    Args:
        filename (String): name of file to be opened.

    Returns:
        file object(object): returns file object with associated filename otherwise returns None if no file with associated filename is found.
    """
    try:
        f = open(filename, 'r')
        return f
    except(FileNotFoundError):
        print(f'Could not find file named {filename} !')
        return None

def processList(File):
    """ReadsFile object and processes its data to the list of items.

    Args:
        File (File object): opened file object with data to be processed.
    """
    for line in File:
        items.append(line)
        print(f'{line} has been added to list.')
    
def processPrices(_list_):
    """Process the price of eachitem in the list.

    Args:
        _list_ (list): list of items to set up pricing to.
    """
    for item in _list_:
        prices = open('costlist.txt', 'a')
        temp = input(f'How much should {item} cost: ')
        try:
            price = float(temp)
            prices.write('%:.2f'.format(price),'\n')
        except(ValueError):
            print(f"You entered an invalid float that could not convert string to float: '{temp}'\n")
            print(f'Skipping to next item after {item}')
        
    
    
def main():
    print('Assignment 6\n')
    if os.path.exists("costlist.txt"):
        os.remove("costlist.txt")
    print("\nAssignment 6\n")
    while(True):
        f_name = input('Please enter a file name to open ')
        if f_name.upper() == 'END':
            print('Program now exiting...')
            break
        if f_name.upper() == 'ITEMS.TXT':
            f_object = open_file(f_name)
            if f_object:
                processList(f_object)
                break
            else:
                continue
        else:
            #if file is not items.txt just pass.
            pass
    print('Program Ended')
    exit()
        
        
if __name__ == '__main__':
    main()

                