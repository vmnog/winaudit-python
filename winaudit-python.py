import pyautogui
import keyboard
from time import sleep
import os
from datetime import date
import schedule

# Algumas funcoes pra facilitar 
def move(x, y):
    pyautogui.moveTo(x, y)   

def clica():
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    

def start():    
    #####   INICIO DO PROGRAMA ########
    
    os.startfile(r"C:\Users\HP G2 240\Desktop\WinAudit.exe") #executa o programa que ta na area de trabalho
    sleep(2)
    move(45, 75) #dentro do programa em full screen clica no audit 
    clica()
    sleep(1)
    move(190, 70)#clica em save
    clica()
    sleep(1)
    today = date.today()
    #print("Today's date:", today)
    d1 = today.strftime("%d-%m-%Y")
    #print("d1 =", d1)
    keyboard.write(d1)#insere data no nome do arquivo
    keyboard.press_and_release('enter')# salva o arquivo
    keyboard.press_and_release('enter')
    sleep(1)
    keyboard.press_and_release('alt + F4') #fecha o programa winaudit
    keyboard.press_and_release('alt + F4')

    
#PARTE QUE O PROGRAMA EXECUTA
print ('Aguardando hora definida para executar o script...')
#https://pypi.org/project/schedule/ 
#schedule.every(15).seconds.do(start) # executa a cada 15 segundos
schedule.every().monday.do(start) # vai executar a cada segunda

while True:
    # Aqui o programa fica checando a cada 1 segundo se ja esta na hora de executar a funcao 
    schedule.run_pending()
    sleep(1)
