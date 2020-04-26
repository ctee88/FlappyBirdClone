"""
Author: Cameron Tee
The module controlling the running of flappy bird.
"""
import pygame

from settings import Settings
from bird import Bird
from background import BackGround
from ground import Ground
from game_stats import GameStats
from scoreboard import Scoreboard
from messages import Messages
import game_functions as gf

def run_game():
	"""
	Initializes the pygame module and instantiates all the game elements.
	While loop controls what functions are called based on the conditions 
	of the game (lives left and the game state).
	"""
	pygame.init()
	settings = Settings()
	screen = pygame.display.set_mode((
		settings.screen_width, settings.screen_height))
	pygame.display.set_caption("Flappy Bird clone by Cameron Tee")
	
	background = BackGround(screen)
	ground = Ground(screen, settings)
	stats = GameStats(settings)
	sb = Scoreboard(screen, settings, stats)
	msgs = Messages(screen, settings)
	bird = Bird(screen, settings, stats)
	
	pipes = []
	
	clock = pygame.time.Clock()
	
	while True:
		gf.check_events(screen, settings, bird, pipes, sb, stats, msgs)
		
		if not stats.game_active and stats.lives_left > 0:
			gf.centre_bird(screen, bird)
			
		if stats.game_active:
			gf.collision_check(screen, settings, bird, pipes, stats)
			gf.update_pipes(screen, settings, bird, pipes, sb, stats)
			
		gf.update_screen(screen, settings, background, ground, bird, pipes, sb, stats, msgs) 
		
		clock.tick(100)
		
if __name__ == '__main__':
	run_game()
