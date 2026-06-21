import pygame, sys
import circleshape
from logger import log_event
from asteroidfield import AsteroidField
from player import Player
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0.0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	AsteroidField.containers = (updatable)
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	player1 = Player(x,y)
	field = AsteroidField()
	while True:
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		for item in drawable:
			item.draw(screen)
		for item in updatable:
			item.update(dt)
		for item in asteroids:
			if player1.collides_with(item):
				log_event("player_hit")
				print("Game over!")
				sys.exit()
		pygame.display.flip()
		dt = clock.tick(60) / 1000
		# print(dt)

if __name__ == "__main__":
    main()
