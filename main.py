# Импорты библиотек
import keyboard
import os
import time
import asyncio
import pickle
import levels
# Создание поля

direction = '@'

# Для поиска игрока на карте и управления им
def find_symbol(field, symbol):
    global player_x, player_y
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == symbol:
                player_x, player_y = j, i
                return True
    return None

# Переменные
fps = 600
rfps = 0
start = 0
speed = 1 
field = levels.level2
save_file = "save_game.pkl"

# Проверка на нахождение игрока в игре
if find_symbol(field, "@"):
    pass
else:
    exit('ERR: Игрока нету на карте!')

# Для вывода информации о кадрах в секунду
async def debug(start_time, frame_count):
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time >= 1:
        fps = frame_count / elapsed_time
        print(f'FPS: {fps:.2f},{player_x=},{player_y=}')
        return current_time, 0
    else:
        return start_time, frame_count + 1

# Обновление направления
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

# Вывод игрового поля
async def screen():
    global field, player_x, player_y, direction
    for i in range(len(field)):
        row = ' '.join([direction if i == player_y and j == player_x else cell for j, cell in enumerate(field[i])])
        print(row)

# Для управлений
# pos = field[player_y][player_x]
# left = field[player_y][player_x - 1]
# right = field[player_y][player_x + 1]
# down = field[player_y + 1][player_x]
# up = field[player_y - 1][player_x]

# Управление игроком через координаты
async def playercontrol(frame_count):
    global player_x, player_y
    if frame_count % (2 * speed) == 0:
        if keyboard.is_pressed('up') and player_y > 0 and field[player_y - 1][player_x] != "#" and field[player_y - 1][player_x] != "^":
            field[player_y][player_x] = '.'
            player_y -= 1
        elif keyboard.is_pressed('down') and player_y < len(field) - 1 and field[player_y + 1][player_x] != "#" and field[player_y + 1][player_x] != "^":
            field[player_y][player_x] = '.'
            player_y += 1
        elif keyboard.is_pressed('left') and player_x > 0 and field[player_y][player_x - 1] != "#" and field[player_y][player_x - 1] != "^":
            field[player_y][player_x] = '.'
            player_x -= 1
        elif keyboard.is_pressed('right') and player_x < len(field[0]) - 1 and field[player_y][player_x + 1] != "#" and field[player_y][player_x + 1] != "^":
            field[player_y][player_x] = '.'
            player_x += 1
        field[player_y][player_x] = '@'

# Функция сохранения игры
def save_game():
    data = {
        'player_x': player_x,
        'player_y': player_y,
        'field': field,
    }
    with open(save_file, 'wb') as f:
        pickle.dump(data, f)

def load_game():
    try:
        with open(save_file, 'rb') as f:
            data = pickle.load(f)
            return data
    except FileNotFoundError:
        print("Файл сохранения не найден.")
        time.sleep(1)
        main_menu()
    
def main_menu():
    print("Меню:")
    print("1. Новая игра")
    print("2. Продолжить")
    print("3. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        return {'player_x': 4, 'player_y': 4, 'field': field}  # Новая игра, установка начального уровня
    elif choice == "2":
        saved_game = load_game()
        if saved_game:
            return saved_game  # Продолжить, загрузка сохраненного уровня
        else:
            print("Нет сохраненной игры.")
            return None
    elif choice == "3":
        exit("Выход из игры.")
    else:
        print("Неверный выбор.")
        return None

# Основной игровой цикл
async def main_loop():
    global player_x, player_y, current_level

    while True:
        game_data = main_menu()
        if game_data is None:
            pass
        else:
            # Продолжение игры, загрузка данных
            player_x = game_data['player_x']
            player_y = game_data['player_y']
            current_level = game_data['field']

        start_time = time.time()
        frame_count = 0

        while True:
            await asyncio.gather(screen(), playercontrol(frame_count), direction_arrow(), debug(start_time, frame_count))
            await asyncio.sleep(speed / fps)  # Изменено
            os.system('cls' if os.name == 'nt' else 'clear')
            frame_count += 1
            # Выход в меню
            if keyboard.is_pressed('q'):
                save_game()  # Сохранение при выходе из игры
                break

asyncio.run(main_loop())
