"""
The module containing all of the functions to run the game.
"""
import sys
import pygame

from pipe import Pipe

def check_events(screen, settings, bird, pipes, sb, stats, msgs):
	"""
	Check for KB and mouse events.
	"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
		elif event.type == pygame.KEYDOWN:
			#Game cannot be activated when lives == 0
			if (event.key == pygame.K_SPACE and stats.lives_left > 0) and not stats.game_active:
				stats.game_active = True
			#Bird flaps only when the game is active
			if event.key == pygame.K_SPACE and stats.game_active:	
				bird.flap()
			if event.key == pygame.K_r and (stats.lives_left < 1):	
				reset_game(screen, settings, bird, pipes, sb, stats)
			if event.key == pygame.K_q:
				sys.exit()
				
def update_screen(screen, settings, background, ground, bird, pipes, sb, stats, msgs):
	"""
	Draws updated game elements each pass through the loop.
	Screen drawn first, then other elements drawn on top of screen.
	"""
	screen.blit(background.image, background.rect)
	blit_pipes(screen, settings, bird, pipes)
	
	#Don't move the ground if the bird is dead
	if stats.lives_left > 0:
		ground.update()
	ground.blitme(screen)
	
	sb.blitme()
	bird.update()
	bird.blitme()
	
	#Draw the message depending on game state
	if not stats.game_active and (stats.lives_left <= 0):
		msgs.draw_game_over()
	elif not stats.game_active:
		msgs.draw_start()

	pygame.display.flip()
	
def centre_bird(screen, bird): 
	"""
	Centre the bird's pos.
	"""
	bird.x = bird.screen_rect.left + 40
	bird.y = bird.screen_rect.bottom / 2 - 10

def collision_check(screen, settings, bird, pipes, stats):
	"""
	Checks if the bird collides with the ground or pipes.
	Removes the life and sets the game state to inactive.
	"""
	#Ground collision
	if bird.y >= bird.max_y:
		stats.lives_left -= 1
		stats.game_active = False
		
	#Pipe collision
	for pipe in pipes:
		if pipe.collide_bird(bird):
			stats.lives_left -= 1
			stats.game_active = False

def update_pipes(screen, settings, bird, pipes, sb, stats):
	"""
	Adds the first pipe pair.
	Updates the pipes' pos.
	Adds new pipes as the game progresses.
	Removes pipes off the screen.
	Increments score for when the bird passes through a pipe.
	"""
	#First pipe
	if len(pipes) == 0:
		pipe_pair = Pipe(screen, settings, bird)
		pipes.append(pipe_pair)
	
	#Move pipes
	for pipe_pair in pipes:
		pipe_pair.top_pipe['x'] -= settings.pipe_speed
		pipe_pair.bot_pipe['x'] -= settings.pipe_speed
	
	#Add new pipes, spaced by half the screen width		
	for pipe in pipes:
		if pipe.top_pipe['x'] == settings.screen_width / 2:
			new_pipe = Pipe(screen, settings, bird)
			pipes.append(new_pipe)
	
	#Remove pipes
	if pipes[0].top_pipe['x'] < -pipe_pair.pipe_width:
		pipes.pop(0)
	
	#Scoring
	if pipes[0].top_pipe['x'] == bird.x:
		stats.score += 1
		sb.prep_score()
		check_hiscore(stats, sb)
		
def check_hiscore(stats, sb):
	"""
	Updates the hiscore based on current score.
	"""
	if stats.score > stats.hiscore:
		stats.hiscore = stats.score
		sb.prep_hiscore()

def blit_pipes(screen, settings, bird, pipes):
	"""
	Draw pipes.
	"""
	for pipe_pair in pipes:
		screen.blit(pipe_pair.image_top, (pipe_pair.top_pipe['x'], pipe_pair.top_pipe['y']))
		screen.blit(pipe_pair.image_bot, (pipe_pair.bot_pipe['x'], pipe_pair.bot_pipe['y']))
	
def reset_game(screen, settings, bird, pipes, sb, stats):
	"""
	Resets the various values of the game to 
	the starting values.
	"""
	stats.game_active = False
	stats.reset_stats()
	bird.tilt = 0
	
	#Empty the list of pipes
	pipes.clear()

	#Draw starting score
	sb.prep_score()
	sb.blitme()
