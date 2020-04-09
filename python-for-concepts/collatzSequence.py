'''# collatz sequence recursive using if else statement and calling function inside function
def collatz(number):
    if number == 1:
        print('Collatz completed!!')
    elif number % 2 == 0:
        print(number // 2)
        collatz(number // 2)
    elif number % 2 == 1:
        print(3 * number + 1)
        collatz(3 * number + 1)

        
try:
    collatz(int(input('Choose any integer greater than 1: ')))
except ValueError:
    print('Non-Onteger entered, program will exit')
    
'''

# collatz sequence using while loop recursively

def collatz(number):
    print('Welcome to Collatz Sequence')
    while number != 1:
        if number % 2 == 0:
            print(number // 2)
            number = number // 2
        else:
            print(number * 3 + 1)
            number = number * 3 + 1

    print('Collatz is completed!')

try:
    collatz(int(input('Please enter numbers only: ')))

except ValueError:
    print('I told you to enter number, now exiting program...')
