import datetime 
import calendar

def payMe():
    print("What is the most you are willing to pay for my advice?\n")
    print("The more you pay, the better the answer! (minimum price: $975.46)\n")
    amount = input()
    if float(amount) >= 975.46:
        print(f'I guess {amount} seems like a fair price')
        return True
    else:
        return False

def getTarget(question):
    q_words = question.split()
    key_words = ['WHO', 'WHAT', 'WHERE', 'WHEN', 'WHY', 'HOW']
    if key_words.__contains__(q_words[0].upper()):
        return q_words[0]
    else:
        return 'unknown'
    
def createList(targetWord):
    display_list = list()
    filename = 'A7_answers.txt'
    f_object = open(filename, 'r')
    
    for line in f_object:
        parsedInfo = line.split('*')
        keyword = getTarget(parsedInfo[0])
        answer = parsedInfo[1]
        if keyword == 'unkown':
            display_list.insert(-1, 'unknown')
        else:
            display_list.insert(-1, answer)
            
    return display_list

def spinTheWheel(name, list_):
    remainder = 0
    num_elements = len(list_)
    
    if num_elements >0:
        t = datetime.datetime.now().second
        remainder = t%num_elements
        print(remainder)
    return list_[remainder]

def declareDate():
    date = datetime.datetime.now()
    day = date.day
    month = calendar.month_name[date.month]
    year = date.year
    
    decleration =f'On this day the {day} in the month of {month} in the year of {year}'
    return decleration
        
    
    
            
        
        
    
