# program to implement paint fill algorithm

class Pixel:
	def __init__(self, color):
		self.color = color

	def __str__(self):
		return self.color + '*'

	def get_color(self):
		return self.color

	def set_color(self, color):
		self.color = color

def paint_fill(monitor_screen, x, y, old_color, new_color):
	if(x < 0 or x > (len(monitor_screen) - 1) or y < 0 or y > len(monitor_screen[0]) - 1):
		return
		
	elif monitor_screen[x][y].get_color() != old_color:
		return

	else:
		if monitor_screen[x][y].get_color() == old_color:
			monitor_screen[x][y].set_color(new_color)
			paint_fill(monitor_screen, x - 1, y, old_color, new_color)
			paint_fill(monitor_screen, x, y - 1, old_color, new_color)
			paint_fill(monitor_screen, x - 1, y - 1, old_color, new_color)
			paint_fill(monitor_screen, x + 1, y + 1, old_color, new_color)

def main():
	monitor_screen = [[Pixel('\u001B[32m') if (i >= 5 and i <= 15) and (j >= 5 and j <= 15) else Pixel('\u001B[34m') for j in range(21)] for i in range(21)]

	for row in monitor_screen:
		for pixel in row:
			print(pixel, end = ' ')
		print('')

	paint_fill(monitor_screen, 7, 7, '\u001B[32m', '\u001B[31m')

	print('\n\n')
	for row in monitor_screen:
		for pixel in row:
			print(pixel, end = ' ')
		print('')

main()