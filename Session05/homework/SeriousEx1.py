
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory["pocket"] = ['seashell', 'strange berry', 'lint']
print(inventory)
inventory["backpack"].remove("dagger")
print(inventory)
inventory["gold"] = [500,50]
print(inventory)