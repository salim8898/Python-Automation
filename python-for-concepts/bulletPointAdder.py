#! python3
# bulletPointAdder.py -Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]

text = '\n'.join(lines)
print('''You know what, we have just added extra '*' in your clipboard copied string
Just CTR+v in blank text and see the magic''')
pyperclip.copy(text)
