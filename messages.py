"""
Author: Cameron Tee
A class representing the messages for START and GAME OVER conditions.
Handles the drawing of the desired message based on if the game is active.
"""
import pygame.font

class Messages():
	
	def __init__(self, screen, settings):
		"""
		Initialise the messages object.
		"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.settings = settings
		
		#Font format
		self.font_colour = (255, 255, 0)
		self.font = pygame.font.SysFont("Helvetica", 18)
		
		#y pos
		self.y = self.settings.screen_height / 2 
		
		#Prepare the msgs images
		self.prep_start()
		self.prep_game_over()
		
	"""
	prep() methods:
	Change the text to be displayed as an image
	so that it can be drawn to the screen.
	Both messages positioned centrally.
	"""
	def prep_start(self):
		start_str = "SPACE TO FLAP"
		self.start_image = self.font.render(start_str, True, self.font_colour)
		self.start_rect = self.start_image.get_rect()
		self.start_rect.centerx = self.screen_rect.centerx
		self.start_rect.y = self.y
		
	def prep_game_over(self):
		game_over_str = "GAME OVER! R TO RESTART"
		self.game_over_image = self.font.render(game_over_str, True, self.font_colour)
		self.game_over_rect = self.game_over_image.get_rect()
		self.game_over_rect.centerx = self.screen_rect.centerx
		self.game_over_rect.y = self.y
		
	def draw_start(self):
		"""
		Draw start msg
		"""
		self.screen.blit(self.start_image, self.start_rect)
		
	def draw_game_over(self):
		"""
		Draw game over msg
		"""
		self.screen.blit(self.game_over_image, self.game_over_rect)
