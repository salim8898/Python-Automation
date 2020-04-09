catNames = []
while True:
    print('Enter the name of cat' + ' (or enter nothing to stop.):')
    name = input()
    if name == "":
        break
    catNames = catNames + [name]
print('The cat names are:')
for n in catNames:
    print(n)
