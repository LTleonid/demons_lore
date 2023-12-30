# Импорты библиотек
import keyboard
import os
import time
import asyncio
import pickle
import levels
# Создание поля
'''
# - Стена
. - Пустота
@ - игрок
^ - письмо
'''
direction = '@'


# Добавим словарь для текстов писем
letters = {
    '^': "Это письмо содержит важную информацию!",
}

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
fps = 0.5
rfps = 0
start = 0
field = levels.level2

# Проверка на нахождение игрока в игре
if find_symbol(field, "@"):
    pass
else:
    exit('ERR: Игрока нету на карте!')

# Для управлений
# pos = field[player_y][player_x]
# left = field[player_y][player_x - 1]
# right = field[player_y][player_x + 1]
# down = field[player_y + 1][player_x]
# up = field[player_y - 1][player_x]

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

# Логика поднятия писем
async def letter_pickup():
    global player_x, player_y
    left = field[player_y][player_x - 1]
    right = field[player_y][player_x + 1]
    down = field[player_y + 1][player_x]
    up = field[player_y - 1][player_x]

    await direction_arrow()

    if left == "^" and keyboard.is_pressed('e') and direction == '←':
        # Поднимаем письмо и выводим его текст
        letter = letters[left]
        print(f'Получено письмо: {letter}')
        field[player_y][player_x - 1] = '.'
    if right == "^" and keyboard.is_pressed('e') and direction == '→':
        # Поднимаем письмо и выводим его текст
        letter = letters[right]
        print(f'Получено письмо: {letter}')
        field[player_y][player_x + 1] = '.'
    if down == "^" and keyboard.is_pressed('e') and direction == '↓':
        # Поднимаем письмо и выводим его текст
        letter = letters[down]
        print(f'Получено письмо: {letter}')
        field[player_y + 1][player_x] = '.'
    if up == "^" and keyboard.is_pressed('e') and direction == '↑':
        # Поднимаем письмо и выводим его текст
        letter = letters[up]
        print(f'Получено письмо: {letter}')
        field[player_y - 1][player_x] = '.'
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

# Управление игроком через координаты
async def playercontrol():
    global player_x, player_y
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

save_file = "save_game.pkl"

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
            await asyncio.gather(screen(), playercontrol(), letter_pickup(), direction_arrow(), debug(start_time, frame_count))
            await asyncio.sleep(1 / fps)
            os.system('cls' if os.name == 'nt' else 'clear')
            frame_count += 1

            if keyboard.is_pressed('q'):
                save_game()  # Сохранение при выходе из игры
                break

asyncio.run(main_loop())
