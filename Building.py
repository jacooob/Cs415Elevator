import pygame
import constants

from random import randint
from spritesheet_functions import SpriteSheet
from graph import ElevatorData

# controls the building sprite and the elevator sprites
# eventually have the person sprite interact with the elevator
# to enter the elevator and give a desired floor #

# elevator sprite location
# x location, y location, width, hieght
E = (0,0,50,50)

ELEVS = constants.ELEVS
FLOORS = constants.FLOORS

class building(pygame.sprite.Sprite):
  """build a building """
  def __init__(self, sprite_sheet_data):
    pygame.sprite.Sprite.__init__(self)
    sprite_sheet = SpriteSheet("BUILDING_.png")
    # grab the image for the elevator
    self.image = sprite_sheet.get_image(sprite_sheet_data[0], sprite_sheet_data[1], sprite_sheet_data[2], sprite_sheet_data[3])
    self.rect = self.image.get_rect()


class elevator(pygame.sprite.Sprite):
  """Elevator a person can travel on"""
  change_y = -1
  current_floor = 1
  goto_floor = 1

  def __init__(self, sprite_sheet_data):
    pygame.sprite.Sprite.__init__(self)
    sprite_sheet = SpriteSheet("elevator.png")
    # grab the image for the elevator
    self.image = sprite_sheet.get_image(sprite_sheet_data[0], sprite_sheet_data[1], sprite_sheet_data[2], sprite_sheet_data[3])
    self.rect = self.image.get_rect()
    self.router = ElevatorData(FLOORS)
    self.path = []
    self.wait = 0

  def update(self):
    #check which way to go
    self.direction()
    # go up or down
    self.rect.y += self.change_y


  def floor(self):
    # check current floor
    if ( self.rect.y == 400):
      self.current_floor = 1
    elif ( self.rect.y == 350 ):
      self.current_floor = 2
    elif ( self.rect.y == 300 ):
      self.current_floor = 3
    elif ( self.rect.y == 250 ):
      self.current_floor = 4
    elif ( self.rect.y == 200 ):
      self.current_floor = 5
    elif ( self.rect.y == 150 ):
      self.current_floor = 6
    elif ( self.rect.y == 100 ):
      self.current_floor = 7
    elif ( self.rect.y == 50 ):
      self.current_floor = 8

  def direction(self):
    # check to see where we should go
    # IMPORTANT !!
    # for now it generates a random floor to go to
    # from the giving floors
    # eventually have the person sprite give the elevator
    # a command to go to a floor
    self.floor()
    if self.wait > 0:
      self.wait -= 1
      return

    if ( self.goto_floor == 0):
      self.change_y = 0
    elif ( self.current_floor == self.goto_floor):
      self.wait = 60
      if not self.path:
        self.path = self.router.gen_scenario(int((FLOORS / 4) * 3))
        self.path = self.router.find_route(self.current_floor, self.path)
      dest = self.path[0]
      self.path = self.path[1:]
      self.change_y = 0
      self.goto_floor = dest.id
      # get rid of passenger // get new passenger
    elif ( self.current_floor < self.goto_floor):
      # Go up
      self.change_y = -1
    elif (self.current_floor > self.goto_floor):
      # Go Down
      self.change_y = 1
