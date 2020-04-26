"""
Author: Cameron Tee
A class representing the background object.
"""
import pygame

class BackGround():
	
	def __init__(self, screen):
		"""
		Initialise the background object.
		"""
		self.screen = screen
		
		#Rect attributes
		self.image = pygame.image.load("images/bg.png")
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = (0, 0)
		
	def blitme(self):
		"""
		Draw background
		"""
		self.screen.blit(self.image, self.rect)
