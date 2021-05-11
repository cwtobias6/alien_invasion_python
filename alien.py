import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
	""" A class to represent Aliens """

	def __init__(self, ai_game):
		super().__init__()
		self.screen = ai_game.screen

		# Load alien image and rect attribute
		self.image = pygame.image.load("./images/alien.bmp")
		self.rect = self.image.get_rect()

		# Start each new alien near the top of the screen 
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)