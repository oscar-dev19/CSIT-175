
def processData(datafile) -> dict:
    """Processes the data in a given filename with names to be added to a dictionary of data.

    Args:
        datafile (Str): filename where name data is located.

    Returns:
        dict: Dictionary of names with first names as keys and corresponding last names as values.
    """
    names = dict()
    f_object = open(datafile, 'r')
    
    for line in f_object:
        line = line.rstrip()
        data = line.split('*')
        first_name = data[0]
        last_name = data[1]
        names[first_name] = last_name
    return names
    
def findName(data,firstName) -> str:
    """Finds corresponding last name from a given dictionary of data and a first name.

    Args:
        data (dict()): Dictionary of name data with first names as keys and last names as values.
        firstName (Str): first name to be looked for corresponding last name

    Returns:
        [str]: formatted String with concatanated first name and its corresponding last name.
    """
    lastName = data[firstName]
    fullname = f'{firstName} {lastName}'
    return fullname

def displaySortedNames(data) -> str:
    sorted_first_names = sorted(data.keys())
    name_list = ''
    for f in sorted_first_names:
        name_list += findName(data,f) + '\n'
    print(name_list)
        
        
    