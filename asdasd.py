import colorama
colorama.init(autoreset=True)

lines = [
        "С Новым Годом, дорогие родители!",
        "Желаем вам счастья, здоровья и удачи в новом году!",
        "Пусть каждый день будет наполнен радостью и уютом.",
        "С любовью и благословением,",
        "Ваши дети"
    ]
line_length = max(len(line) for line in lines)
print(colorama.Fore.WHITE + "#" * (line_length + 4))
for line in lines:
    print(colorama.Fore.GREEN + "# " + line.center(line_length) + " #")
print(colorama.Fore.WHITE + "#" * (line_length + 4))
