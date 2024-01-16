import time
import random

key = 0
key_moment = 0
monument_complete = False

def Start():
    print("Здравствуй путник!")
    time.sleep(1)
    print("Вы находитесь в загадочном мире, полном приключений.")
    time.sleep(1)
    print("Ваша задача - принимать решения и исследовать этот мир.")
    time.sleep(1)
    print("Приготовьтесь к захватывающему путешествию!\n")
    main()

def Player_choice(choices):
    print("Выберите действие:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Введите номер вашего выбора: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Пожалуйста, выберите корректный номер.")
        except ValueError:
            print("Пожалуйста, введите число.")

def main():
    global key, key_moment, monument_complete
    print("\nГлава 1: Загадочный лес")
    while True:
        time.sleep(1)
        print("Вы просыпаетесь в густом лесу. Ваши действия:")
        choice = Player_choice(["Идти налево", "Идти направо", "Остаться на месте"])
        #Идти налево (Готово)
        if choice == 1:
            if not monument_complete:
                print("Вы направились налево и обнаружили старый храм.")
                time.sleep(1)
                print("Вход в храм блокирован таинственным щитом.")
                time.sleep(1)
                print("Ваши действия:")
                choice = Player_choice(["Исследовать храм", "Вернуться в лес"])
                #Исследовать храм
                if choice == 1:
                    print("Вы нашли древний свиток с заклинанием. Что вы хотите сделать?")
                    time.sleep(1)
                    choice = Player_choice(["Произнести заклинание", "Вернуться в лес"])
                    #Произнести заклинание
                    if choice == 1:
                        print("Таинственный щит исчез, открывая вход в храм.")
                        time.sleep(1)
                        print("Вы вошли в храм!")
                        time.sleep(1)
                        
                        print("Таинственный щит вновь повился и запер вас в храме, что будете делать?")
                        time.sleep(1)
                        choice = Player_choice(["Успокоиться и осмотреть храм", "Пытаться орать заклинание и сломать щит"])
                        if choice == 1:
                            print('Вы успокоились, в темноте вы смогли разглядеть лабиринт. Что будете делать?')
                            choice = Player_choice(["Попытаться пройти лабиринт", "Ничего не делать"])
                            if choice == 1:
                                die_or_pass = random.randint(0,2)
                                print(die_or_pass)
                                if die_or_pass == 1:
                                    while True:
                                        #Лабиринт пройден
                                            if key == 0:
                                                print("Лабиринт пройден. Вы видете дверь и плиту на которую что-то нужно положить.")
                                                choice = Player_choice(["Встать на плиту", "вернуться в лабиринт"])
                                                if choice == 1:
                                                    print("Вы встали на плиту и дверь открылась, Ваши действия?")
                                                    choice = Player_choice(["Войти в дверь", "стоять на месте"])
                                                    if choice == 1:
                                                        print("Как только вы встали с плиты дверь захлопнулась.")
                                                        pass
                                                    if choice == 2: 
                        #Гора)
                                                        print("Вы постояли на плите, подумали о жизни. Вскоре вы начали слышать голоса, видеть странные вещи")
                                                        choice = Player_choice(["Встать с плиты", "Стоять дальще"])
                                                        if choice == 1:
                                                            print('Вы встали с плиты, дверь перед вами закрылась')
                                                            pass
                                                        elif choice == 2:
                                                            print("Галлюцинации стали усиливаться, вскоре вы потеряли сознание...")
                                                            break
                                                    
                                                if choice == 2:
                                                    print("Вы вернулись в лабиринт и нашли ключ.")
                                                    key = 1
                                            else:
                                                while True:
                                                    choice = Player_choice(["Встать на плиту", "Положить на плиту ключ."])
                                                    if choice == 1:
                                                        print("Вы встали на плиту и дверь открылась, Ваши действия?")
                                                        choice = Player_choice(["Войти в дверь", "стоять на месте"])
                                                        if choice == 1:
                                                            print("Вы попытались войти в дверь но она закрыласт.")
                                                            monument_complete = True
                                                            break
                                                        if choice == 2: 
                                                            print("Вы постояли на плите, подумали о жизни. Вскоре вы начали слышать голоса, видеть странные вещи")
                                                            choice = Player_choice(["Встать с плиты", "Стоять дальще"])
                                                            if choice == 1:
                                                                print('Вы встали с плиты, дверь перед вами закрылась')
                                                                pass
                                                            elif choice == 2:
                                                                print("Галлюцинации стали усиливаться, вскоре вы потеряли сознание...")
                                                                break
                                                    if choice == 2: 
                                                        print("Вы положили ключ и прошли сквозь дверь.")
                                                        monument_complete = True
                                                        break
                                                break       
                                    
                                elif die_or_pass == 2:
                                    while True:
                                        #Лабиринт пройден с доп. предметом
                                        print('Вы вышли с лабиринта с ключом. Перед вами находится плита и дверь')
                                        choice = Player_choice(['Встать на плиту','Положить ключ на плиту', 'Вернуться в лабиринт'])
                                        if choice == 1:
                                            print('Дверь перед вами открылась!')
                                            choice = Player_choice(['Войти в дверь','Стоять на плите'])
                                            if choice == 2:
                                                print("Вы постояли на плите, подумали о жизни. Вскоре вы начали слышать голоса, видеть странные вещи")
                                                choice = Player_choice(["Встать с плиты", "Стоять дальще"])
                                                if choice == 1:
                                                    print('Вы встали с плиты, дверь перед вами закрылась')
                                                    pass
                                                elif choice == 2:
                                                    print("Галлюцинации стали усиливаться, вскоре вы потеряли сознание...")
                                                    break
                                            if choice == 1:
                                                print("Как только вы встали с плиты дверь захлопнулась.")
                                                pass

                                        elif choice == 2:
                                            print('Вы положили ключ на плиту и дверь открылась.')
                                            choice = Player_choice(['Войти в дверь','Забрать ключ','Встать на плиту'])
                                            if choice == 1:
                                                print("Вы прошли сквозь дверь.")
                                                monument_complete = True
                                                break
                                            if choice == 2:
                                                if key_moment != 4:
                                                    print('Вы забрали ключ и дверь закрылась')
                                                    key_moment = random.randint(0,4)
                                                else:
                                                    print("Вы взяли ключ и потеряли сознание...")
                                                    break
                                            if choice == 3:
                                                print('Встав на плиту вместе с ключом на вас упал T-34')
                                                break

                                        elif choice == 3:
                                            print('После входа в лабиринт вы больше не смогли найти выход, вы потеряли сознание от страха...')
                                            break
                                else:
                                    print("Вы заблудились в лабиринте и потеряли сознание.")
                                    pass
                            elif choice == 2:
                                print('Вы потеряли сознание от голода...')
                        elif choice == 2:
                            print('Из-за паники вы не заметили пропасть и упали в неё, вы потеряли сознание...')
                    elif choice == 2:
                        print("Вы решили вернуться в лес. Приключение продолжается...")
                        pass
               #Вернуться в лес
                elif choice == 2:
                    print("Вы решили вернуться в лес. Приключение продолжается...")
                    pass
            
            #Вернуться в лес
                elif choice == 2:
                    print("Вы решили вернуться в лес.")
                    pass
            else:
                print('Вы обнаружили сгоревший домик')
                choice = Player_choice(['Войти в него','Уйти обратно в лес']) 
                if choice == 1:
                    print('Вы вошли в дом. После осмотра на вас упала доска и вы потеряли сознание...')
                    pass
                if choice == 2:
                    print('Вы вернулись в лес')
                    pass
        #Идти на право
        elif choice == 2:
            print("Вы направились направо и наткнулись на реку.")
            time.sleep(1)
            print("Ваши действия:")
            choice = Player_choice(["Проплыть реку", "Искать мост", "Вернуться в лес"])
            #Переплыть реку
            if choice == 1:
                print("Вы решили проплыть реку и обнаружили таинственный остров.")
                time.sleep(1)
                print("Приключение продолжается на острове!")
            #Искать мост
            elif choice == 2:
                print("Вы решили искать мост. Приключение продолжается...")
            #Вернуться в лес
            elif choice == 3:
                print("Вы решили вернуться в лес. Приключение продолжается...")
        #Остаться на месте
        elif choice == 3:
            exit("Вас сьели волки.")

# Главная часть игры
Start()
