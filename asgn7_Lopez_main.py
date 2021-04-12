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
    

if __name__ == '__main__':
    main()
    