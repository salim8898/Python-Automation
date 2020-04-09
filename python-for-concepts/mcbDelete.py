#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> -Saves clipboard to keyboard.
#       py.exe mcb.pyw delete <keyword> - Will delete keyword
#       py.exe mcb.pyw delete   - Delete all keywords
#       py.exe mcb.pyw <keyword> - Loaads keyword to clipboard.
#       py.exe mcb.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcbd')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print(f'Keyword {sys.argv[2]} has been saved')
# Delete keyword
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
    print(f'Entered keyword {sys.argv[2]} deleted')
# List keyword
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        content = pyperclip.paste()
        print(content)
# Delete all keywords
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
# Load keyword in clipboard
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(f'Keyword {sys.argv[1]} has been loaded to clipboard')

mcbShelf.close()

