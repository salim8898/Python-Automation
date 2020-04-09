def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(k) + ' ' + str(v))
        item_total = item_total + v
    print('Total number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):
    newDict = {}
    for items in inventory:
        newDict.setdefault(items, 0)
        newDict[items] += 1

    for k, v in addedItems.items():
        newDict.setdefault(k, 0)
        newDict[k] += v
    return newDict


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dragger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(dragonLoot, inv)
displayInventory(inv)


