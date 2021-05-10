import pygame 
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion():
	""" A class to manage game assets and behavior """


	def __init__(self):
		""" Init game, and create game resources """
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption(f"Alien Invasion")

		self.ship = Ship(self)

		self.bullets = pygame.sprite.Group()


	def run_game(self):
		""" Start the main loop for the game """
		while True:
			self._check_events()
			self._update_screen()
			self.bullets.update()
			self.ship.update()
			self._update_bullets()




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
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _fire_bullet(self):
		if  len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _update_bullets(self):
		# Remove bullets that have disappeared from screen

		self.bullets.update()
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)


	def _update_screen(self):
		# Redraw the screen during each pass through the loop.
			self.screen.fill(self.settings.bg_color)
			self.ship.blitme()

			for bullet in self.bullets:
				bullet.draw_bullet()

		# Draw most current screen
			pygame.display.flip()

if __name__ == "__main__":
	# Make a game instance and run game
	ai = AlienInvasion()
	ai.run_game()