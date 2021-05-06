import pygame

class Ship():
	"""docstring for Ship"""
	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		self.image = pygame.image.load("images/ship.bmp")
		self.rect = self.image.get_rect()

		self.rect.midbottom = self.screen_rect.midbottom

		# Movement Flag
		self.moving_right = False
		self.moving_left = False


	def update(self):
		""" Update ship's movement based on Movement Flag """
		if self.moving_right:
			self.rect.x += 1
		elif self.moving_left:
			self.rect.x -=1

	def blitme(self):
		self.screen.blit(self.image,self.rect)

