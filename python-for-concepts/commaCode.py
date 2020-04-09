spam = ['apples', 'bannas', 'tofu', 'cats']

def comma(name):
    count = 0
    joined = ''
    while count < len(name) -2:
        joined += spam[count] + ', '
        count += 1
    joined += name[-2] + ' and '
    joined += name[-1]
    print(joined)


comma(spam)
