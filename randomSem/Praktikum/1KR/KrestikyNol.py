import os

WorkArray = [0,0,0]                                          #Основной рабочий список

for i in range(len(WorkArray)):
    WorkArray[i] = [0] * 3

Draw = False
gonext = False                                          #Переменная передачи хода другому игроку
endgame = False                                         #Переменная которая поможет завершить игру
ErrorText = ""                                          #Переменная которая нужна чтобы выводить ошибки
Player = 1

def updateScreen():                                     #Функция которая обновляет экран
    global ErrorText                                    #Объявляем что ErrorText это не локальная переменная
    os.system('cls')                                    #Очистка консоли        
    print("╔═══╦═══╦═══╗", end = "")
    
    for i in range(len(WorkArray)):
        print("\n║", end="")
        for j in range(len(WorkArray)):
            if WorkArray[i][j] == 0:
                print("   ",end="║")
            elif WorkArray[i][j] == 1:
                print(" X " ,end="║")
            elif WorkArray[i][j] == 2:
                print(" O ",end="║" )
        if i < 2:
            print("\n╠═══╬═══╬═══╣", end = "")

    print("\n╚═══╩═══╩═══╝")
    print(ErrorText)
    ErrorText = ""
    print("Ход игрока: ", "X" if Player == 1 else "O") 

def Win():                                              #Расчет победы игроков
    global endgame
    global Draw
    chain = 0
    if Player == 1:
        use = 1
    else:
        use = 2

    for i in range(len(WorkArray)):
        for j in range(len(WorkArray)):
            if WorkArray[i][j] == use:
                if i+2 < 3:
                    if WorkArray[i+1][j] == use:        #от метки может быть 8 направлений расчета победы. Если находится одна из сторон с 3 метками подряд, то расчет прекращается и засчитывается победа
                        if WorkArray[i+2][j] == use:
                            endgame = True
                            break
                if j+2 < 3:        
                    if WorkArray[i][j+1] == use:
                        if WorkArray[i][j+2] == use:
                            endgame = True
                            break
                if i-2>=0:
                    if WorkArray[i-1][j] == use:
                        if WorkArray[i-2][j] == use:
                            endgame = True
                            break
                if j-2>=0:
                    if WorkArray[i][j-1] == use:
                        if WorkArray[i][j-2] == use:
                            endgame = True
                            break
                if i-2 >= 0 and j-2 >= 0:    
                    if WorkArray[i-1][j-1] == use:
                        if WorkArray[i-2][j-2] == use:
                            endgame = True
                            break
                if i+2 < 3 and j+2 < 3:
                    if WorkArray[i+1][j+1] == use:
                        if WorkArray[i+2][j+2] == use:
                            endgame = True
                            break
                if i-2 >= 0 and j+2 < 3:
                    if WorkArray[i-1][j+1] == use:
                        if WorkArray[i-2][j+2] == use:
                            endgame = True
                            break
                if i+2 < 3 and j-2 >= 0:
                    if WorkArray[i+1][j-1] == use:
                        if WorkArray[i+2][j-2] == use:
                            endgame = True
                            break
    if not endgame:                                     #если все метки заняты и победа не найдена, то засчитывается ничья.
        for i in range(3):
            for j in range(3):
                if WorkArray[i][j] == 1 or WorkArray[i][j] == 2:
                    chain += 1
        if chain == 9:
            endgame = " -Ничья- "
            Draw = True


def IsDigit (txt):                                      #проверка введенного числа на то цифра это или нет.
    if txt != "" and txt.isdigit():
        return int(txt) - 1
    else:
        return -1                                       #Если не цифра, то возвращает -1 что не попадает ни в один интервал.

def Turn():                                             
    global ErrorText
    global gonext
    global WorkArray
    iny = IsDigit(input("Введите строку: "))
    inx = IsDigit(input("Введите столбец: "))           #ввод строки и столбца с последующей проверкой на то цифра или нет.
    if iny > 2 or iny < 0:                             
        ErrorText += " -Нет такой строки- "
    if inx > 2 or inx < 0: 
        ErrorText += " -Нет такого столбца- "
    if ErrorText == "":
        if WorkArray[iny][inx] == 0:                   #проверка на возможность поставить в это место метку.
            WorkArray[iny][inx] = 1 if Player == 1 else 2
            gonext = True
        else:
            ErrorText += " -Нельзя ставить метку сюда- "
    

def MainLoop():                                         #основной рабочий цикл. обновляет экран, запрашивает порядок хода и проверяет победу игроков, если никто не победил, то повторяется.
    global Player
    global ErrorText
    global gonext
    updateScreen()
    Turn()
    Win()
    if not endgame:
        if gonext == True:
            Player = 1 if Player == 2 else 2
            gonext = False
        MainLoop()
    else: 
        ErrorText += " -Конец Игры- "
        updateScreen()



MainLoop()
if Draw:
    print("Ничья")
else:
    print("Победил игрок: ", Player)
input("Нажмите Enter чтобы выйти ")