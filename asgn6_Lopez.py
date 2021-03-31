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
        line = line.rstrip()
        items.append(line)
        print(f'{line} has been added to list.')
    
def processPrices(_list_):
    """Process the price of eachitem in the list.

    Args:
        _list_ (list): list of items to set up pricing to.
    """
    for item in sorted(_list_):
        prices = open('costlist.txt', 'a')
        temp = input(f'How much should {item} cost: ')
        try:
            price = float(temp)
            formatted_price = '{:.2f}'.format(price)
            prices.write(f'{item} have a cost of {formatted_price} dollars\n')
        except(ValueError):
            print(f"You entered an invalid float that could not convert string to float: '{temp}'\n")
            print(f'Skipping to next item after {item}')

def display_cost():
    costs = open_file('costlist.txt')
    print('Cost List\n')
    for line in costs:
        print(line + '\n')
        
    
    
def main():
    print('Assignment 6\n')
    if os.path.exists("costlist.txt"):
        os.remove("costlist.txt")
    print("\nAssignment 6\n")
    while(True):
        f_name = input('Please enter a file name to open ')
        if not f_name:
            print('Please enter a name of the file to open. Type end to leave program.')
            continue
        if f_name.upper() == 'END':
            print('Program Ended')
            break
        if f_name.upper() == 'ITEMS.TXT':
            f_object = open_file(f_name)
            if f_object:
                processList(f_object)
                processPrices(items)
                break
            else:
                continue
        else:
            #check if file exists.
            f = open_file(f_name)
            if not f:
                print('Please Try Again')
            #if file is not items.txt just pass.
            pass
    if os.path.exists('costlist.txt'):
        display_cost()
        print('Program Ended')
    exit()
        
        
if __name__ == '__main__':
    main()
    

                