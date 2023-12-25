import keyboard
import os
import time
import asyncio
import random


field = [
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]

def find_symbol(field, symbol):
    global player_x, player_y
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == symbol:
                player_x, player_y = j, i
                return True
    return None

if find_symbol(field, "@"):
    pass
else:
    #А потому что чё логику ломать?
    exit('ERR: Игрока нету на карте!')

fps = 9
frames = 0



async def debug():
    print(f'{player_x=},{player_y=},{frames=}')

async def screen():
    global field, player_x, player_y
    for i in range(len(field)):
        for j in range(len(field[0])):
            if i == player_y and j == player_x:
                print('@', end=' ')
            else:
                print(field[i][j], end=' ')
        print()

async def playercontrol():
    global player_x, player_y
    if keyboard.is_pressed('up') and player_y > 0 and field[player_y - 1][player_x] != "#" and field[player_y - 1][player_x] != " ":
        field[player_y][player_x] = '.'  # Стираем старое место игрока
        player_y -= 1
    elif keyboard.is_pressed('down') and player_y < len(field) - 1 and field[player_y + 1][player_x] != "#" and field[player_y + 1][player_x] != " ":
        field[player_y][player_x] = '.'  # Стираем старое место игрока
        player_y += 1
    elif keyboard.is_pressed('left') and player_x > 0 and field[player_y][player_x - 1] != "#" and field[player_y][player_x - 1] != " ":
        field[player_y][player_x] = '.'  # Стираем старое место игрока
        player_x -= 1
    elif keyboard.is_pressed('right') and player_x < len(field[0]) - 1 and field[player_y][player_x + 1] != "#" and field[player_y][player_x + 1] != " ":
        field[player_y][player_x] = '.'  # Стираем старое место игрока
        player_x += 1
    field[player_y][player_x] = '@'  # Устанавливаем новое место игрока

async def spawn_pokemons():
    global field
    pass

while True:
    frames += 1
    asyncio.run(debug())
    asyncio.run(screen())
    asyncio.run(playercontrol())
    time.sleep(1 / fps)
    os.system('cls' if os.name == 'nt' else 'clear')
    if keyboard.is_pressed('q'):
        break
