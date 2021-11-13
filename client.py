from pynput import keyboard
import time
import os
import socket
import sys


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
		
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


encoding = sys.getdefaultencoding()
CLIENT_KEY = None


def draw(w, h, l, p1x, p1y, p2x, p2y, bx, by):
	y = 0
	pitch = {
		f'[0, 0]': '╔',
		f'[0, {h - 1}]': '╚',
		f'[{w - 1}, 0]': '╗',
		f'[{w - 1}, {h - 1}]': '╝',
	}

	while y < h:
		x = 0
		result = ''
		
		while x < w:
			if y == 0 or y == h - 1:
				try:
					result += pitch[str([x, y])]
				except KeyError:
					result += '═'
			elif x == 0 or x == w - 1:
				result += '║'
			elif x == round(bx) and y == round(by):
				result += 'o'
			elif p1y <= y <= p1y + l and x == p1x:
				result += '|'
			elif p2y <= y <= p2y + l and x == p2x:
				result += '|'
			else:
				result += ' '
			x += 1

		print(result)
		y += 1


WIDTH = 40
HEIGHT = 10
LENGTH = 1
BORDER = LENGTH + 2
BALL_DIR_X = 1
BALL_DIR_Y = 1
DIFFICULTY = 0.01

ballX = WIDTH / 2
ballY = HEIGHT / 2

directionX = 1
directionY = 1

player1_y = HEIGHT / 2
player2_y = HEIGHT / 2
player1_x = 1
player2_x = WIDTH - 2


def press_instruction(key):
	global CLIENT_KEY
	data = 0
	if key == keyboard.Key.up:
		data = 1
	if key == keyboard.Key.down:
		data = 2
	s.sendall(str.encode(str(data)))


def release_instruction(key):
	pass


keyboard.Listener(
	on_press=press_instruction,
	on_release=release_instruction
).start()


while True:
	data = s.recv(1024)
	res = data.decode(encoding)
	res = res.split(',')
	os.system('cls')
	draw(WIDTH, HEIGHT, LENGTH, player1_x, int(res[2]), player2_x, int(res[3]), int(res[0]), int(res[1]))
	time.sleep(DIFFICULTY)
