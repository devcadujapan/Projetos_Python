import pyautogui as pa
import time
import pyperclip

pa.PAUSE = 1
digite = input("Digite o Louvor: ")

pa.press('win')
pa.write("brave")
pa.press('ENTER')
pa.write("cifraclub.com.br")
pa.press('ENTER')
time.sleep(3)
pa.hotkey('F11')
pa.click(x=721, y=33)
pyperclip.copy(digite)
pa.hotkey('ctrl', 'v')
pa.press('ENTER')
