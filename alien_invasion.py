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

		self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption(f"Alien Invasion")

		self.ship = Ship(self)


	def run_game(self):
		""" Start the main loop for the game """
		while True:
			self._check_events()
			self._update_screen()
			self.ship.update()



	def _check_events(self):
		# Watch for keyboard and mouse events
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					self._check_keydown_events(event)
				elif event.type == pygame.KEYUP:
					self._check_keyup_events(event)
					
	def _check_keydown_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == K_q:
			sys.exit()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False


	def _update_screen(self):
		# Redraw the screen during each pass through the loop.
			self.screen.fill(self.settings.bg_color)
			self.ship.blitme()

		# Draw most current screen
			pygame.display.flip()

if __name__ == "__main__":
	# Make a game instance and run game
	ai = AlienInvasion()
	ai.run_game()