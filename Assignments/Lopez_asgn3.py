best_friends= ''
invitees= ''

print('Assignment3\n')
name = input('Enter your name:\n')

print(name,'Please enter the names of your three bestfriends:')
for i in range(1,4):
    b_friend = input()
    best_friends += str(i)+'.'+b_friend.title()+'\n'

print('My Best Friends are:\n')
print(best_friends)


print('Now enter the names of your wedding invitees please (or simply press enter when done)')
done= False
num_guests = 0
while not done:
    guest = input("Guest's Name(or press Enter to quit):")
    if guest:
        num_guests+=1
        invitees += str(num_guests) +"."+guest.title()+'\n'
    else:
        done = True

print("My Wedding Attendees are:\n")
print(invitees)

print('END OF ASSIGNMENT 3')

