from openpyxl import load_workbook
import pyautogui
import time
import keyboard
import pygetwindow as gw

# planilha = load_workbook('credenciais.xlsx')
# pagina = planilha['Plan1']

# produto = []
# quantidade = []
# armazen = []
# documento = 123456z
# for dados in pagina.iter_rows(values_only=True):
#     produto.append(dados[0])
#     quantidade.append(dados[1])
#     armazen.append(dados[2])

def clicar(vezes, tecla):
    i = 0
    while i < vezes: 
        keyboard.send(tecla)
        i = i + 1  

keyboard.send('windows')

time.sleep(1)
pyautogui.write("smartview")

time.sleep(1)
keyboard.send('enter')

time.sleep(1)
keyboard.send('tab')
pyautogui.write("admin")

time.sleep(1)
keyboard.send('tab')
pyautogui.write("sccp@1910")

time.sleep(3)
keyboard.send('tab')
keyboard.send('enter')

time.sleep(3)
clicar(3, 'tab')
pyautogui.write('721914')

clicar(1, 'tab')
pyautogui.write("1")

clicar(5, 'tab')
pyautogui.write("03")

clicar(10, 'tab')
pyautogui.write("45788")


