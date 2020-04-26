"""
Author: Cameron Tee
A class storing the settings for flappy bird.
"""
import pygame

class Settings():
	
	def __init__(self):
		"""
		Initialise the settings object.
		"""
		self.screen_width = 288
		self.screen_height = 512
		
		self.pipe_speed = 2 
		self.ground_speed = 2
		
		self.lives = 1
