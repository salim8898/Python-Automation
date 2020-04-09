name = '' #empty string, 0, 0.0 always considered as false, whill all other values considered true
while not name:
    print('Enter your name: ')
    name = input()
print('How many guests will you have?')
numofGuests = int(input())
if numofGuests:
    print('Be sure to have enough room for all your guests.')
print('Done')
    
