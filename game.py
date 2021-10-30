from pynput import keyboard
import time
import os

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
BALL_DIR_X = 0.2
BALL_DIR_Y = 0.2

ballX = WIDTH / 2
ballY = HEIGHT / 2

directionX = 1
directionY = 1

player1_y = HEIGHT / 2
player2_y = HEIGHT / 2
player1_x = 1
player2_x = WIDTH - 2

def press_instruction(key):
	global player1_y, player2_y
	if key == keyboard.KeyCode.from_char('w'):
		if player1_y > 1:
			player1_y -= 1
	elif key == keyboard.KeyCode.from_char('s'):
		if player1_y < HEIGHT - 3:
			player1_y += 1
	if key == keyboard.Key.up:
		if player2_y > 1:
			player2_y -= 1
	elif key == keyboard.Key.down:
		if player2_y < HEIGHT - 3:
			player2_y += 1	

def release_instruction(key):
	pass

keyboard.Listener(
	on_press=press_instruction,
	on_release=release_instruction
).start()

while True:
	ballX += BALL_DIR_X * directionX
	ballY += BALL_DIR_Y * directionY
	if round(ballX) == WIDTH - 1:
		print('Left gamer wins!')
		break
	if round(ballX) == 0:
		print('Right gamer wins!')
		break
	if player1_y <= round(ballY) <= player1_y + LENGTH and round(ballX) == player1_x:
		directionX = 1
	if player2_y <= round(ballY) <= player2_y + LENGTH and round(ballX) == player2_x:
		directionX = -1
	if round(ballY) == 0:
		directionY = 1
	if round(ballY) == HEIGHT - 1:
		directionY = -1
	os.system('cls')
	draw(WIDTH, HEIGHT, LENGTH, player1_x, player1_y, player2_x, player2_y, ballX, ballY)
	time.sleep(0.01)

