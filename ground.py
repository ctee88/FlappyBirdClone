"""
Author: Cameron Tee
A class representing the ground class.
Used to load and draw 2 images to give the
scrolling effect.
"""
import pygame

class Ground():
	
	def __init__(self, screen, settings):
		"""
		Intialise the ground object.
		"""
		self.settings = settings
		self.screen = screen
		
		self.image = pygame.image.load("images/ground.png")
		self.image_width = self.image.get_width()
		
		#y pos for both images
		self.y = self.settings.screen_height * 0.8
		
		#x pos for first image
		self.x0 = 0
		
		#x pos for second image
		self.x1 = self.image_width
		
	def update(self):
		"""
		Moves the 2 ground images.
		Set the x co-ord of the image to be off the right side of the
		screen when the image moves off the left side.
		"""
		self.x0 -= self.settings.ground_speed
		self.x1 -= self.settings.ground_speed
		
		if self.x0 + self.image_width < 0:
			self.x0 = self.x1 + self.image_width
		
		if self.x1 + self.image_width < 0:
			self.x1 = self.x0 + self.image_width
			
	def blitme(self, screen):
		"""
		Draw the ground 
		"""
		self.screen.blit(self.image, (self.x0, self.y))
		self.screen.blit(self.image, (self.x1, self.y))
