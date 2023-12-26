def find_caret_indices(field):
    caret_indices = []

    for i, row in enumerate(field):
        for j, char in enumerate(row):
            if char == '^':
                caret_indices.append((i, j))

    return caret_indices

def compare_caret_indices(field, index1, index2):
    caret_positions = find_caret_indices(field)
    
    if index1 in caret_positions and index2 in caret_positions:
        return field[index1[0]][index1[1]] == field[index2[0]][index2[1]]
    else:
        return False

# Пример использования:
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

index1 = (4, 3)
index2 = (3, 3)

result = compare_caret_indices(field, index1, index2)
print(f"Индексы {index1} и {index2} равны: {result}")
