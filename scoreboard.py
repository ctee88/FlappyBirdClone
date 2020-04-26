"""
Author: Cameron Tee
A class providing the live updates to the player stats: Score and Hiscore.
Manages the drawing of these updated values to the screen.
"""
import pygame.font

class Scoreboard():
	
	def __init__(self, screen, settings, stats):
		"""
		Initialise the scoreboard object.
		"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.settings = settings
		self.stats = stats
		
		#Font format
		self.font_colour = (255, 0, 0)
		self.font = pygame.font.SysFont("Helvetica", 18)
		
		#Prepare initial score images
		self.prep_score()
		self.prep_hiscore()
		
	"""
	prep() methods:
	Change the text to be displayed as an image
	so that it can be drawn to the screen.
	"""
	def prep_score(self):
		score_str = str(self.stats.score)
		self.score_image = self.font.render("SCORE: {}".format(score_str), 
			True, self.font_colour) 
			
		#Positioned top left
		self.score_rect = self.score_image.get_rect()
		self.score_rect.left = self.screen_rect.left
		self.score_rect.top = self.screen_rect.top
		
	def prep_hiscore(self):
		hiscore_str = str(self.stats.hiscore)
		self.hiscore_image = self.font.render("HISCORE: {}".format(hiscore_str),
			True, self.font_colour) #See prep_score()
			
		#Positioned top right
		self.hiscore_rect = self.hiscore_image.get_rect()
		self.hiscore_rect.right = self.screen_rect.right
		self.hiscore_rect.top = self.screen_rect.top
		
	def blitme(self):
		"""
		Draw the scores
		"""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.hiscore_image, self.hiscore_rect)
