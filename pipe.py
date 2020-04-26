"""
Author: Cameron Tee
A class representing the pipe object.
Handles the movement, collision detection and drawing of the pipes.
"""
import pygame
import random

class Pipe():
	
	def __init__(self, screen, settings, bird):
		"""
		Initialise the pipe object.
		"""
		self.screen = screen
		self.settings = settings
		self.bird = bird
		
		#Pipe images
		self.image_top = pygame.image.load("images/pipetop.png")
		self.image_bot = pygame.transform.flip(self.image_top, False, True)
		
		#Pipe height and width
		self.pipe_height = self.image_top.get_height()
		self.pipe_width = self.image_top.get_width()
	
		self.generate_pipes()
		
	def generate_pipes(self):
		"""
		Sets the starting x co-ord of each pipe.
		Sets the gap size based on bird image size.
		Sets the y co-ord of the gap within the range of 10% - 40% of the screen.
		Sets the starting pos (x,y) for top and bot pipe
		"""
		#Pipes start 20 px off the screen
		self.x_start = self.settings.screen_width + 20
		
		#Determine gap size
		self.bird_height = self.bird.image.get_height()
		self.gap_size = self.bird_height * 3
		
		#Determine gap y
		self.gap_y = random.randint(round(self.settings.screen_height * 0.1),
			round(self.settings.screen_height * 0.4))
			
		#Determine starting pos for pipes
		self.top_pipe = {'x': self.x_start, 'y': self.gap_y - self.pipe_height} 
		self.bot_pipe = {'x': self.x_start, 'y': self.gap_y + self.gap_size}
		
	
	def collide_bird(self, bird):
		"""
		Returns true if any point of the bird
		collides with any point of the pipes.
		"""
		#Get the masks for the bird and the pipes.
		bird_mask = bird.get_mask()
		top_mask = pygame.mask.from_surface(self.image_top)
		bot_mask = pygame.mask.from_surface(self.image_bot)
		top_offset = (self.top_pipe['x'] - bird.x, self.top_pipe['y'] - round(bird.y))
		bot_offset = (self.bot_pipe['x'] - bird.x, self.bot_pipe['y'] - round(bird.y))
		
		#Points of intersection between bird and top or bot pipes
		top_point = bird_mask.overlap(top_mask, top_offset)
		bot_point = bird_mask.overlap(bot_mask, bot_offset)
		
		if top_point or bot_point:
			return True
			
		return False
