from pynput import keyboard
import time
import os

WIDTH = 40
HEIGHT = 10
ballX = WIDTH / 2
ballY = HEIGHT / 2
BALL_DIR_X = 0.2
BALL_DIR_Y = 0.2
directionX = 1
directionY = 1
player1_y = HEIGHT / 2
player2_y = HEIGHT / 2
player1_x = 1
player2_x = WIDTH - 2
LENGTH = 1

def draw():
	y = 0
	pitch = {
		f'[0, 0]': '╔',
		f'[0, {HEIGHT - 1}]': '╚',
		f'[{WIDTH - 1}, 0]': '╗',
		f'[{WIDTH - 1}, {HEIGHT - 1}]': '╝',
	}
	while y < HEIGHT:
		x = 0
		result = ''
		while x < WIDTH:
			if y == 0 or y == HEIGHT - 1:
				try:
					result += pitch[str([x, y])]
				except KeyError:
					result += '═'
			elif x == 0 or x == WIDTH - 1:
				result += '║'
			elif x == round(ballX) and y == round(ballY):
				result += 'o'
			elif player1_y <= y <= player1_y + LENGTH and x == player1_x:
				result += '|'
			elif player2_y <= y <= player2_y + LENGTH and x == player2_x:
				result += '|'
			else:
				result += ' '
			x += 1
		print(result)
		y += 1


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
	draw()
	time.sleep(0.01)

