

import keyboard
import os
import time
import asyncio
import random


rows, columns = 11, 11
fps = 9
player_x, player_y = columns // 2, rows // 2
frames = 0




async def debug():
    print(f'{player_x=},{player_y=},{frames=}')

async def playercontrol():
    global player_x, player_y
    if keyboard.is_pressed('up') and player_y > 0:
        player_y -= 1
    elif keyboard.is_pressed('down') and player_y < rows - 1:
        player_y += 1
    elif keyboard.is_pressed('left') and player_x > 0:
        player_x -= 1
    elif keyboard.is_pressed('right') and player_x < columns - 1:
        player_x += 1

async def screen():
    global rows, columns, player_x, player_y
    for i in range(rows):
        for j in range(columns):
            if i == player_y and j == player_x:
                print('#', end=' ')
            else:
                print('.', end=' ')
        print()
async def spawn_pokemons():
    global rows,columns
    pass

while True:
    frames +=1
    asyncio.run(debug())
    asyncio.run(screen())
    asyncio.run(playercontrol())
    time.sleep(1/fps)
    os.system('cls' if os.name == 'nt' else 'clear')  
    if keyboard.is_pressed('q'):
        break
    
