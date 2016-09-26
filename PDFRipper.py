import ImageGrab
import Image
import pyautogui
from fpdf import FPDF

pyautogui.keyDown('alt'); pyautogui.press('tab'); pyautogui.keyUp('alt')

pdf = FPDF()

for i in range (291):
	im = ImageGrab.grab((765,134,1458,1030));
	
	name = 'screenie'
	name += `i`
	name += '.png'
	
	im.save(name, 'png')
	
	pdf.add_page()
	pdf.image(name, 0, 0, 210, 297)
	
	pyautogui.press('space')

pdf.output('ENTR 3400 TextBook.pdf', 'F')