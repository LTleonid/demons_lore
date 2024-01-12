pos = 0
hp = 20
inventory = [
    'Steak',
    'Steak1',
    'steak2',
    'notAnumber',
    '5'
]
inventory_modificater = 0

def fight():
    global pos
    if pos == 0:
        Inventory_menu1(inventory[0 + inventory_modificater], inventory[1 + inventory_modificater],
                         inventory[2 + inventory_modificater], inventory[3 + inventory_modificater])

def Inventory_menu1(item1, item2, item3, item4):
    print('   ┌─────────────────────────────┐')
    print('   │                             │')
    print('   │                             │')
    print('   │        ┌─┐      ┌─┐         │')
    print('   │        │ │      │ │         │')
    print('   │        └─┘ ──── └─┘         │')
    print('   │                             │')
    print('   ├─────────────────────────────┤')
    print(f'   │ >{item1}    *{item2}      ',end='|\n')
    print(f'   │ *{item3}    *{item4}      ',end='|\n')
    print('   │          HP:100             │')
    print('   └─────────────────────────────┘')
    print('\n')

fight()
