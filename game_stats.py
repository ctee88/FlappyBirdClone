"""
Author: Cameron Tee
A class keeping track of the game stats.
Only one life in Flappy Bird.
This class controls the game state (whether playing or not).
"""

class GameStats():
	
	def __init__(self, settings):
		"""
		Initialise the gamestats object.
		"""
		self.settings = settings
		self.reset_stats()
		
		#Begin the game in an inactive state
		self.game_active = False
		
		#Hiscore should never be reset
		self.hiscore = 0		
		
	def reset_stats(self):
		"""
		Score and the single life are reset between attempts
		"""
		self.lives_left = self.settings.lives
		self.score = 0
