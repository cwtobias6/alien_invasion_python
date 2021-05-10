import pygame

class Ship():
	""" A class to manage a ship """

	def __init__(self,ai_game):
		""" Initialize ship and set starting position """
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load ship image and get its rect
		self.image = pygame.image.load("./images/ship.bmp")
		self.rect = self.image.get_rect()

		# Start ship and midbottom of the screen
		self.rect.midbottom = self.screen_rect.midbottom

		# Store a decimal value for the ship's horizontal position.
		self.x = float(self.rect.x)


		# Moving Flags
		self.moving_right = False
		self.moving_left = False

	def update(self):
		""" Update ship's movement based on Movement Flag """
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		elif self.moving_left and self.rect.left > 0 :
			self.x -= self.settings.ship_speed

		self.rect.x = self.x

	def blitme(self):
		""" Draw ship at current location """
		self.screen.blit(self.image, self.rect)

	def update(self):
		# Update the ship's x value, not the rect.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		elif self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		# Update rect object from self.x.
		self.rect.x = self.x



