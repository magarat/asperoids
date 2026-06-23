from circleshape import CircleShape
import pygame, random
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
	def __init__(self, x: float, y: float, radius: float) -> None:
		super().__init__(x, y, radius)
	def draw(self,screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
	def update(self, dt):
		self.position += self.velocity * dt
	def split(self):
		self.kill()
		if self.radius < ASTEROID_MIN_RADIUS:
			return
		else:
			log_event("asteroid_split")
			angle = random.uniform(20, 50)
			velo_1 = self.velocity.rotate(angle)
			velo_2 = self.velocity.rotate(-1 * angle)
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
			new_asteroid_1.velocity = velo_1 * 1.2
			new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
			new_asteroid_2.velocity = velo_2 * 1.2
