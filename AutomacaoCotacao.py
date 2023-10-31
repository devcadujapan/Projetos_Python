import pyautogui as pa
import time

pa.PAUSE = 1
pa.press('win')
pa.write("brave")
pa.press('ENTER')
pa.write("uol.com.br")
pa.press('ENTER')
time.sleep(5)
pa.click(x=1022, y=339)
time.sleep(5)
pa.click(x=1153, y=170)
