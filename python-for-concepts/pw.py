#! python3
# pw.py - An insecure password locker program.

import sys, pyperclip
PASSWORD = {'email': 'F5kljlsksldkjsljg',
            'blog': 'dflsakjgasjgsajgjsdf',
            'luggage': '12345'}


if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   #first command line arg is the account name
print(account)

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)

    
    

