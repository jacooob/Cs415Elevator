import pygame
import constants
from Building import elevator
from random import randrange,randint
from spritesheet_functions import SpriteSheet

#controls the person sprite type.
# !! not done yet current just spawns random person with no goals
# eventually have the person sprite interact with the elevator through
# collisions. giving the elevator a floor, and a person inside the elevator.

class person(pygame.sprite.Sprite):
	"""Generate people to go on elevator"""
	current_floor = 0
	goto_floor = 0
	change_x = 1
	change_y = 0
	
	def __init__(self, sprite_sheet_data):
		pygame.sprite.Sprite.__init__(self)
		sprite_sheet = SpriteSheet("people.png")
		self.image = sprite_sheet.get_image(sprite_sheet_data[0], sprite_sheet_data[1], sprite_sheet_data[2], sprite_sheet_data[3])
		self.rect = self.image.get_rect()
	
	def update(self):
		#if the person walks off screen reset position
		if (self.rect.x == -20):
			self.rect.x = constants.SCREEN_WIDTH + 10
		if (self.rect.x == constants.SCREEN_WIDTH + 20):
			self.rect.x = -10
		# go up
		self.rect.y += self.change_y
		# go down
		self.rect.x += self.change_x
		
	
def create_person():
	color = randrange(0,111,10)
	height = randint(14,20)
	width = randint(5,10)
	p = (color,0,width,height)
	block = person(p)
	# change change_x for direction
	# if dont intialize then they stand still
	# could just use rand int from -1 to one but 
	# 0 makes them not move and thats boring
	dir = randint(0,1)
	if (dir == 0):
		block.change_x = -1
	else:
		block.change_x = 1
	block.rect.x = randrange(25,300,20)
	block.rect.y = 450 - height
	return block
	
