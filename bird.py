"""
Author: Cameron Tee
A class representing the bird object.
Handles the movement, bird mask and drawing of the bird.
"""
import pygame

class Bird():
	"""
	Rotational constants used when tilting bird image.
	"""
	ROT_MAX = 25
	ROT_VEL = 15
	
	def __init__(self, screen, settings, stats):
		"""
		Initialise the bird object.
		"""
		self.screen = screen
		self.settings = settings
		self.stats = stats
		
		#Rect attributes
		self.image = pygame.image.load('images/bird.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#Highest (lowest on the screen) y the bird can reach
		self.max_y = self.settings.screen_height * 0.8 - self.image.get_height() + 5
		
		#Attributes used to update the bird's pos
		self.x = 0
		self.y = 0 
		self.height = self.y
		self.vel = 0
		self.frame_count = 0
		self.tilt = 0
		
	def flap(self):
		"""
		Flap method resets the frame count and 
		the velocity each time flap() is called 
		to stop the values of these attributes increasing
		indefinitely.
		"""
		
		self.vel = 0
		self.vel -= 7.5 
		self.frame_count = 0
		self.height = self.y
		
	def update(self):
		"""
		The bird moves based on a unit of time i.e. frame_count.
		This allows the bird to move a set amount of pixels PER FRAME as opposed 
		to moving a set amount of pixels PER N FRAMES in clock.tick(N) (line 51 in main.py).
		This means that we are able to produce smoother movement for the bird.
		
		Updates the bird's pos within the constraints: Not above the screen
		and not below the ground image
		
		Tilts the bird's image based on the displacement and the state of the game
		"""
		self.frame_count += 1
		
		#SUVAT equation (s = ut + 0.5at**2) for downwards vel
		displacement = self.vel*(self.frame_count) + 0.5*(3)*(self.frame_count)**2
		
		#Terminal vel
		if displacement >= 2:
			displacement = 2
		
		#Fine tuning
		if displacement < 0:
			displacement -= 3
		
		#Make sure the bird does not go above the screen
		if self.y + displacement < 0:
			self.y = 0
		else:
			self.y = self.y + displacement
			
		#Make sure the bird does not go below ground
		if self.y + displacement > self.max_y:
			self.y = self.max_y
		
		#Tilt upwards
		if (displacement < 0 or self.y < self.height + 50) and self.stats.game_active:
			if self.tilt < self.ROT_MAX:
				self.tilt = self.ROT_MAX
		else:
			#Tilt downards
			if self.tilt > -90 and (self.stats.game_active or self.stats.lives_left < 1):
				self.tilt -= self.ROT_VEL

	def blitme(self):
		"""
		Draw the bird at its updated position and tilt where
		the centre of rotation of the rotated image is the top left 
		of the original image.
		"""
		rot_image = pygame.transform.rotate(self.image, self.tilt)
		rot_rect = rot_image.get_rect(center=self.image.get_rect(topleft=(self.x, self.y)).center)
		self.screen.blit(rot_image, rot_rect.topleft)
		
	def get_mask(self):
		"""
		Get the mask for the current bird image
		"""
		return pygame.mask.from_surface(self.image)
