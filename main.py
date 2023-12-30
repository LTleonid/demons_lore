#Импорты библеотек
import keyboard #Для удобного управления
import os #Для очистки кончоли (надо сделать сохранение)
import time #Для задержек
import asyncio #Для Асинхронового запуска функций
import random #Для рандомизации спавна врагов мб
#Создание поля(Его можно делать в редакторе)
'''
# - Стена
. - Пустота
@ - игрок
^ - письмо
'''
direction = '@'
field = [
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
['#', '.', '.', '^', '.', '@', '.', '.', '.', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '^', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
]
#Для поиска игрока на карте чтобы им можно было потом управлять, плюс это фигня не даёт создать карту без игрока
def find_symbol(field, symbol):
    global player_x, player_y
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == symbol:
                #Тут игре дают координаты (ближайшего) игрока
                player_x, player_y = j, i
                return True
    return None
#Проверка на нахождение игрока в игре
if find_symbol(field, "@"):
    pass
else:
    #А потому что чё логику ломать?
    exit('ERR: Игрока нету на карте!')
#Переменные
#Максимальный фпс 55(с пролагами) оптимальный 60(20)
fps = 60 #Кол-во кадров в секунду, расчитываються по формуле 1 секунда/кол-во кадорв (1/fps)
rfps = 0 #Количетсво Реальных кадров в секунду Real Frame Per Second
start = 0
'''Для управлений
    pos = field[player_y][player_x]
    left = field[player_y][player_x - 1]
    right = field[player_y][player_x + 1]
    down = field[player_y + 1][player_x]
    up = field[player_y - 1][player_x]
'''
#Везде где есть приписка async в функциях делает её асинхронной
'''
Для тебя макс, как работает функция тоесть def(без асинхрона). 
def - указывает что это функция 
name() - Name это название функции в скобках ты пишешь что может принимать эта функция(как в графических уравнениях где в функциях стоит x)
дальше всего этого пишется код который она выполняет в себе (например, если ты указал h в функции ты можешь посчитать её там h += 1)
после если ты хочешь чтобы эта функция что то отдавала после себя ты можешь написат return и что вернуть например return h + 1 а потом если вызвать эту функцию в принт то при значении h = 1 мы получим 2 print(name(1)) = 2
это был краткий экскурс по данной штуке, более понятнее объясню когда созвонимся
'''
async def debug(start_time, frame_count):
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time >= 1:
        fps = frame_count / elapsed_time
        print(f'FPS: {fps:.2f},{player_x=},{player_y=}')
        return current_time, 0
    else:
        return start_time, frame_count + 1

async def letter_pickup():
    global player_x,player_y
    left = field[player_y][player_x - 1]
    right = field[player_y][player_x + 1]
    down = field[player_y + 1][player_x]
    up = field[player_y - 1][player_x]

    await direction_arrow()

    if left == "^" and keyboard.is_pressed('e') and direction == '←':
        field[player_y][player_x - 1] = '.'
    



async def direction_arrow():
    global direction, player_x, player_y
    if keyboard.is_pressed('up'):
        direction = '↑'
    elif keyboard.is_pressed('down'):
        direction = '↓'
    elif keyboard.is_pressed('left'):
        direction = '←'
    elif keyboard.is_pressed('right'):
        direction = '→'


async def screen():
    global field, player_x, player_y, direction
    for i in range(len(field)):
        row = ' '.join([direction if i == player_y and j == player_x else cell for j, cell in enumerate(field[i])])
        print(row)

#Управление игроком через координаты
async def playercontrol():
    global player_x, player_y
    if keyboard.is_pressed('up') and player_y > 0 and field[player_y - 1][player_x] != "#" and field[player_y - 1][player_x] != "^":
        field[player_y][player_x] = '.'  # Стираем старое место игрока
        player_y -= 1
    elif keyboard.is_pressed('down') and player_y < len(field) - 1 and field[player_y + 1][player_x] != "#" and field[player_y + 1][player_x] != "^":
        field[player_y][player_x] = '.'  # Стираем старое место игрока
        player_y += 1
    elif keyboard.is_pressed('left') and player_x > 0 and field[player_y][player_x - 1] != "#" and field[player_y][player_x - 1] != "^":
        field[player_y][player_x] = '.'  # Стираем старое место игрока
        player_x -= 1
    elif keyboard.is_pressed('right') and player_x < len(field[0]) - 1 and field[player_y][player_x + 1] != "#" and field[player_y][player_x + 1] != "^":
        field[player_y][player_x] = '.'  # Стираем старое место игрока
        player_x += 1
    field[player_y][player_x] = '@'  # Устанавливаем новое место игрока
#Надо сделать спавнелку мобов
async def spawn_pokemons():
    global field
    pass

async def main_loop():
    start_time = time.time()
    frame_count = 0

    while True:
        await asyncio.gather(screen(), playercontrol(), direction_arrow(), debug(start_time, frame_count), letter_pickup())
        await asyncio.sleep(1/fps)
        os.system('cls' if os.name == 'nt' else 'clear')    
        frame_count += 1

        if keyboard.is_pressed('q'):
            break

asyncio.run(main_loop())
