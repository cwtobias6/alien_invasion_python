<<<<<<< HEAD
import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""docstring for Bullet"""
	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color


=======
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage bullets fired from the ship"""

	def __init__(self,ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = ai_game.settings.bullet_color

		# Create a bullet rect at (0, 0) and then set correct position.
>>>>>>> alien_invasion2
		self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		self.y = float(self.rect.y)

	def update(self):
		self.y -= self.settings.bullet_speed
		self.rect.y = self.y

	def draw_bullet(self):
<<<<<<< HEAD
		pygame.draw.rect(self.screen,self.color,self.rect)
=======
		"""Draw the bullet to the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)
>>>>>>> alien_invasion2
