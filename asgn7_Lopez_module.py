import time

def payMe():
    print("What is the most you are willing to pay for my advice?\n")
    print("The more you pay, the better the answer! (minimum price: $975.46)\n")
    amount = input()
    if float(amount) > 975.46:
        print(f'I guess {amount} seems like a fair price')
        return True
    else:
        return False

def getTarget(question):
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

def spinTheWheel(username, list):
    remainder = 0
    num_elements = len(list)
    
    if num_elements >0:
        t = time.time()
        remainder = num_elements%t
    return list[remainder]
        
    
    
            
        
        
    
