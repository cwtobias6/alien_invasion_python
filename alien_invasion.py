import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion():
	"""docstring for AlienInvasion"""
	def __init__(self):
		pygame.init()

		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()


	def run_game(self):
		while True:
			self._check_events()
			self._update_screen()
			self._update_bullets()
			self.ship.update()


			# Make the most recently drawn screen visible.
			pygame.display.flip()

	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					self._check_keydown_events(event)
				elif event.type == pygame.KEYUP:
					self._check_keyup_events(event)

	def _check_keydown_events(self,event):
		if event.key == pygame.K_RIGHT:
			self.ship.rect.x += 1
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.rect.x -= 1
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()



	def _check_keyup_events(self,event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False	
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_screen(self):
		# Redraw the screen during each pass through the loop.
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

	def _update_bullets(self):
		self.bullets.update()

		for bullet in self.bullets.copy():
			if bullet.rect.bottom <=0:
				self.bullets.remove(bullet)




if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()