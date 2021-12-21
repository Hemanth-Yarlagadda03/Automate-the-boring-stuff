stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    total_items = 0
    for k,v in inventory.items():
        print(str(v)+' '+k)
        total_items += v
    print("Total number of items: "+str(total_items))


displayInventory(stuff)

#second part of the project which adds the item to the dictionary
def addToInventory(inventory, addedItems):
    for k in addedItems:
        inventory.setdefault(k, 0) 
        inventory[k] += 1 
    return inventory

inv = {'gold coin': 42, 'rope': 1}
displayInventory(inv)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)