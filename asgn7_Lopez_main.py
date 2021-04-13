from asgn7_Lopez_module import *

def main():
    print("**The Wizard**\n")
    print("The Wizard will see you now")
    if not payMe():
        print("Go Away!")
        exit()
    while True:
        name = input("What is your name? ")
        if not name:
            continue
        break
    while True:
        question = input(f'Please {name.title()} ask any question you like.')
        if not question:
            print(f'{name.title()} please dont be shy.')
            continue
        break
    t = getTarget(question)
    list_ = createList(t)
    input('Press Enter to Spin the Wheel.')
    answer = spinTheWheel(name,list_)
    print("Spin..Spin..Spin....Spin.......Spin........tick, tick, tick, stop\n")
    print(answer)
    

if __name__ == '__main__':
    main()
    