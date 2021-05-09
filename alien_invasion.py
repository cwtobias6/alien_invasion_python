import pygame 
import sys
from settings import Settings
from ship import Ship

class AlienInvasion():
	""" A class to manage game assets and behavior """


	def __init__(self):
		""" Init game, and create game resources """
		pygame.init()
		self.settings = Settings()

		self.rounds = 0
		self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption(f"Alien Invasion: {self.rounds}")

		self.ship = Ship(self)


	def run_game(self):
		""" Start the main loop for the game """
		while True:
			# Watch for keyboard and mouse events

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# Redraw the screen during each pass through the loop.
			self.screen.fill(self.settings.bg_color)
			self.ship.blitme()

			# Draw most current screen
			self.rounds += 1
			pygame.display.flip()

if __name__ == "__main__":
	# Make a game instance and run game
	ai = AlienInvasion()
	ai.run_game()