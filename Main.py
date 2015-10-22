import pygame
import constants
import World
from People import person
from random import randint, randrange 

def main():
	pygame.init()
	
	#set height and width of screen
	size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
	screen = pygame.display.set_mode(size)
	# window label
	pygame.display.set_caption("ELEV8R")
	
	# choose level (only one level currently just )
	level_list = []
	level_list.append(World.level())
	current_level = level_list[0]
	
	#main group of sprites that need to be updated and drawn
	active_sprite_list = pygame.sprite.Group()
	
	done = False
	clock = pygame.time.Clock()
	
	while not done:
		for event in pygame.event.get():
			# check for events
			if event.type == pygame.QUIT:
				# close the screen
				done = True
		
		# update the positions of all sprites
		current_level.update()
		# prepare the new frame drawing to be flip
		current_level.draw(screen)
		
		clock.tick(60)
		#update the screen
		pygame.display.flip()
		
	pygame.quit()

if __name__ == "__main__":
	main()
