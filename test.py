import keyboard
import time
pos = 0
hp = 20
inventory = [
    'Steak',
    'Steak1',
    'steak2',
    'notAnumber',
    '5'
]
inventory_modificater=0
def fight():
    global pos
    if pos == 0:
        Inventory_menu1(inventory[0+inventory_modificater],inventory[1+inventory_modificater],inventory[2+inventory_modificater],inventory[3+inventory_modificater])

def Attack_Choice():
    global hp
    print('   ┌─────────────────────────────┐')
    print('   │                             │')
    print('   │                             │')
    print('   │        ┌─┐      ┌─┐         │')
    print('   │        │ │      │ │         │')
    print('   │        └─┘ ──── └─┘         │')
    print('   │                             │')
    print('   ├─────────┬──────────┬────────┤')
    print('   │^Attack  │*Inventory│*Mercy  │')
    print('   ├─────────┴──────────┴────────┤')
    print('   │          HP:100             │')
    print('   └─────────────────────────────┘')
    print('\n')

def Inventory_Choice():
    global hp
    print('   ┌─────────────────────────────┐')
    print('   │                             │')
    print('   │                             │')
    print('   │        ┌─┐      ┌─┐         │')
    print('   │        │ │      │ │         │')
    print('   │        └─┘ ──── └─┘         │')
    print('   │                             │')
    print('   ├─────────┬──────────┬────────┤')
    print('   │*Attack  │^Inventory│*Mercy  │')
    print('   ├─────────┴──────────┴────────┤')
    print('   │          HP:100             │')
    print('   └─────────────────────────────┘')
    print('\n')

def Mercy_Choice():
    global hp
    print('   ┌─────────────────────────────┐')
    print('   │                             │')
    print('   │                             │')
    print('   │        ┌─┐      ┌─┐         │')
    print('   │        │ │      │ │         │')
    print('   │        └─┘ ──── └─┘         │')
    print('   │                             │')
    print('   ├─────────┬──────────┬────────┤')
    print('   │*Attack  │*Inventory│^Mercy  │')
    print('   ├─────────┴──────────┴────────┤')
    print('   │          HP:100             │')
    print('   └─────────────────────────────┘')
    print('\n')

def Inventory_menu1(item1,item2,item3,item4):
    global hp
    print('   ┌─────────────────────────────┐')
    print('   │                             │')
    print('   │                             │')
    print('   │        ┌─┐      ┌─┐         │')
    print('   │        │ │      │ │         │')
    print('   │        └─┘ ──── └─┘         │')
    print('   │                             │')
    print('   ├─────────────────────────────┤')
    print(f'    >{item1}    *{item3}      ')
    print(f'    *{item2}     *{item4}      ')
    print(f'             HP:{hp}             ')

    print('\n')
def Inventory_menu2():    
    print('   ┌─────────────────────────────┐')
    print('   │                             │')
    print('   │                             │')
    print('   │        ┌─┐      ┌─┐         │')
    print('   │        │ │      │ │         │')
    print('   │        └─┘ ──── └─┘         │')
    print('   │                             │')
    print('   ├─────────────┬───────────────┤')
    print('   │ *text       │ *text         │')
    print('   │ >text       │ *text         │')
    print('   │          HP:100             │')
    print('   └─────────────────────────────┘')
    print('\n')
def Inventory_menu3():
    print('   ┌─────────────────────────────┐')
    print('   │                             │')
    print('   │                             │')
    print('   │        ┌─┐      ┌─┐         │')
    print('   │        │ │      │ │         │')
    print('   │        └─┘ ──── └─┘         │')
    print('   │                             │')
    print('   ├─────────────┬───────────────┤')
    print('   │ *text       │>text          │')
    print('   │ *text       │ *text         │')
    print('   │          HP:100             │')
    print('   └─────────────────────────────┘')
    print('\n')
def Inventory_menu4():
    print('   ┌─────────────────────────────┐')
    print('   │                             │')
    print('   │                             │')
    print('   │        ┌─┐      ┌─┐         │')
    print('   │        │ │      │ │         │')
    print('   │        └─┘ ──── └─┘         │')
    print('   │                             │')
    print('   ├─────────────┬───────────────┤')
    print('   │ *text       │ *text         │')
    print('   │ *text       │ >text         │')
    print('   │          HP:100             │')
    print('   └─────────────────────────────┘')
    print('\n')
def Dialog_menu():
    print('   ┌─────────────────────────────┐')
    print('   │                             │')
    print('   │                             │')
    print('   │        ┌─┐      ┌─┐         │')
    print('   │        │ │      │ │         │')
    print('   │        └─┘ ──── └─┘         │')
    print('   │                             │')
    print('   ├─────────────────────────────┤')
    print('   │ -text                       │')
    print('   │                             │')
    print('   │                             │')
    print('   └─────────────────────────────┘')
    print('\n')
def Attack_Choice():
    global hp
    print('   ┌─────────────────────────────┐')
    print('   │                             │')
    print('   │                             │')
    print('   │        ┌─┐      ┌─┐         │')
    print('   │        │ │      │ │         │')
    print('   │        └─┘ ──── └─┘         │')
    print('   │                             │')
    print('   ├─────────────────────────────┤')
    print('   │ >Name                       │')
    print('   │                             │')
    print('   │          HP:100             │')
    print('   └─────────────────────────────┘')
    print('\n')
def Attack_menu():
    print('   ┌─────────────────────────────┐')
    print('   │                             │')
    print('   │                             │')
    print('   │        ┌─┐      ┌─┐         │')
    print('   │        │ │      │ │         │')
    print('   │        └─┘ ──── └─┘         │')
    print('   │                             │')
    print('   ├──┬───────────────────────┬──┤')
    print('   │  │                       │  │')
    print('   │  │|──────────/──────────►│  │')
    print('   │  │                       │  │')
    print('   └──┴───────────────────────┴──┘')

fight()
