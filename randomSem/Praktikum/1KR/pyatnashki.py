import random
import os
import time
from msvcrt import getch

mainarr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
random.shuffle(mainarr)
totalTurns = 0
isWin = False

def EndGame():
    os.system('cls')
    print("Вы Выйграли!\nКоличество ходов - ", totalTurns, "\n\n\n\n\n\n")
    key = input("Нажмите любую кнопку чтобы выйти")

def Win():
    global isWin
    it = 0
    if mainarr[0] > 0:
        while it < len(mainarr):
            if it == 10:
                isWin = True
            if mainarr[it]+1 == mainarr[it+1]:
                it+=1
                continue
            else:
                break

def moove():
    it = 0
    global totalTurns
    key = ord(getch())
    while it < len(mainarr):
        if mainarr[it] == 0:
            break
        it+=1

    if (it+4 < len(mainarr)) and (key == 80):
        temp = mainarr[it]
        mainarr[it] = mainarr[it+4]
        mainarr[it+4] = temp
        totalTurns += 1
    elif (key == 72) and it-4>=0:
        temp = mainarr[it]
        mainarr[it] = mainarr[it-4]
        mainarr[it-4] = temp
        totalTurns += 1
    elif (it+1 < len(mainarr)) and (key == 77) and (((it+1) % 4) !=0):
        temp = mainarr[it]
        mainarr[it] = mainarr[it+1]
        mainarr[it+1] = temp
        totalTurns += 1
    elif (key == 75) and (it % 4 !=0):
        temp = mainarr[it]
        mainarr[it] = mainarr[it-1]
        mainarr[it-1] = temp
        totalTurns += 1



def Update():
    it = 0
    os.system('cls')
    print("╔═══════╦═══════╦═══════╦═══════╦═══════╗\n║", end = "\t")
    while it < len(mainarr):
        if mainarr[it] != 0:
            print(mainarr[it], end = "\t")
        else:
            print("■", end = "\t")
        it+=1
        if (it % 4 == 0) and (it< len(mainarr)):
            print("║")
            print("║", end = "\t")
    print("║\n╚═══════╩═══════╩═══════╩═══════╩═══════╝\n")

    print("Управление стрелочками")

def mainloop():
    Update()
    moove()
    Win()

while not isWin:
    mainloop()
EndGame()
