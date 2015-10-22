import pygame
import constants
import Building
import People

# controls the base world and the current level

ELEVS = constants.ELEVS
FLOORS = constants.FLOORS

class World(): 
	#sprite lists for each part of the level
	elevator_list = None
	Building_list = None
	people_list = None
	background = None
	
	def __init__(self):
		self.elevator_list = pygame.sprite.Group()
		self.Building_list = pygame.sprite.Group()
		self.people_list = pygame.sprite.Group()	
			
	def update(self):
		self.Building_list.update()
		self.elevator_list.update()
		self.people_list.update()
		
	def draw(self, screen):
		screen.fill(constants.BLUE)
		screen.blit(self.background, (0,0))
		self.Building_list.draw(screen)
		self.elevator_list.draw(screen)
		self.people_list.draw(screen)
		
class level(World):
	
	def __init__(self):
		World.__init__(self)
		#load background
		self.background = pygame.image.load("Background.png").convert()
		
		#build building without elevators
		b = (0,0,150*ELEVS,50*FLOORS)
		block = Building.building(b)
		block.rect.x = 50
		block.rect.y = 450 - (FLOORS*50)
		self.Building_list.add(block)
		
		#build proper amount of elevators
		for i in range(0,ELEVS):
			eblock = Building.elevator(Building.E)
			eblock.rect.x = 100 + (i * 150) 
			eblock.rect.y = 400 
			self.elevator_list.add(eblock)
		
		#generate random people who just walk either direction
		for i in range(0,10):
			pblock = People.create_person()
			self.people_list.add(pblock)
		
		
		
