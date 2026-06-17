import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0.0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	player1 = Player(x,y)
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	while True:
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		player1.draw(screen)
		player1.update(dt)
		pygame.display.flip()
		dt = clock.tick(60) / 1000
		# print(dt)

if __name__ == "__main__":
    main()
