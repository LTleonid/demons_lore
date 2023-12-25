import tkinter as tk

def change_color_left(event):
    change_color(event, left_click=True)

def change_color_right(event):
    change_color(event, left_click=False)

def change_color(event, left_click=True):
    x, y = event.x // square_size, event.y // square_size
    if left_click:
        # Левая кнопка мыши
        if colors[y][x] == '#808080':  # Серый цвет
            colors[y][x] = '#000000'  # Черный цвет
        elif colors[y][x] == '#000000':  # Черный цвет
            colors[y][x] = '#808080'  # Серый цвет
    else:
        # Правая кнопка мыши
        if colors[y][x] == '#808080':  # Серый цвет
            colors[y][x] = '#00FF00'  # Зеленый цвет
        elif colors[y][x] == '#00FF00':  # Зеленый цвет
            colors[y][x] = '#808080'  # Серый цвет
    update_display()

def get_symbol(color):
    if color == '#808080':  # Серый цвет
        return '.'
    elif color == '#000000':  # Черный цвет
        return '#'
    elif color == '#00FF00':  # Зеленый цвет
        return '@'
    else:
        return '?'  # Неизвестный цвет

def show_data():
    for row in colors:
        print('[', end='')
        print(', '.join([f"'{get_symbol(color)}'" for color in row]), end='')
        print('],')

def update_display():
    for i in range(height):
        for j in range(width):
            canvas.itemconfig(squares[i][j], fill=colors[i][j])

def create_field():
    global window, canvas, squares, colors, width, height, square_size, cursor_x, cursor_y

    width = int(entry_width.get())
    height = int(entry_height.get())
    square_size = 20

    window.destroy()

    window = tk.Tk()  
    window.title("Поле")

    canvas = tk.Canvas(window, width=width*square_size, height=height*square_size)
    canvas.pack()

    colors = [['#808080' for _ in range(width)] for _ in range(height)]
    squares = [[None for _ in range(width)] for _ in range(height)]
    cursor_x, cursor_y = 0, 0

    for i in range(height):
        for j in range(width):
            x1, y1 = j * square_size, i * square_size
            x2, y2 = x1 + square_size, y1 + square_size
            squares[i][j] = canvas.create_rectangle(x1, y1, x2, y2, fill=colors[i][j])

    canvas.bind('<Button-1>', change_color_left)  # Левая кнопка мыши
    canvas.bind('<Button-3>', change_color_right)  # Правая кнопка мыши
    canvas.bind('<Motion>', lambda event: update_cursor_position(event))

    btn_show = tk.Button(window, text="Вывести поле", command=show_data)
    btn_show.pack()

    window.mainloop()

def update_cursor_position(event):
    global cursor_x, cursor_y
    cursor_x, cursor_y = event.x, event.y

window = tk.Tk()
window.title("Настройка поля")

label_width = tk.Label(window, text="Ширина:")
label_width.pack()
entry_width = tk.Entry(window)
entry_width.pack()

label_height = tk.Label(window, text="Высота:")
label_height.pack()
entry_height = tk.Entry(window)
entry_height.pack()

btn_create = tk.Button(window, text="Создать поле", command=create_field)
btn_create.pack()

window.mainloop()
