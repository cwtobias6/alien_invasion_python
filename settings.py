class Settings():
	"""docstring for Settings"""
	def __init__(self):
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)

		# Ship Settings
		self.ship_speed = 1.5

		# Bullet Settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3