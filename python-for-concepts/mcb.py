#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
#Usage: py.exe mcb.pyw save <keyword> -Saves clipboard to keyboard.
#       py.exe mcb.pyw <keyword> - Loaads keyword to clipboard.
#       py.exe mcb.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
print('MultiClipboard Program')
# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print(f'Clipboard content has been saved in database with keyword {sys.argv[2]}.')
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print(f'Loaded all keywords to clipboard')
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(f'Content associated with key {sys.argv[1]} has been loaded to clipboard')

mcbShelf.close()
