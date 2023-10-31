import pyautogui as pa
import time
import pyperclip

pa.PAUSE = 1
digite = input("Pesquisar sobre: ")

pa.press('win')
pa.write("brave")
pa.press('ENTER')
pa.write("youtube.com")
pa.press('ENTER')
time.sleep(4)
pa.hotkey('F11')
pa.click(x=1035, y=28)
pyperclip.copy(digite)
pa.hotkey('ctrl', 'v')
pa.press('ENTER')
