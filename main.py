import pygame
import sys
pygame.init()

size = width, height = 1280, 720
light_sky_blue = 135, 206, 250	 
screen = pygame.display.set_mode(size)

class Organ:

pancreas = {
	'height':120,
	'image':,
	'cut':,
	'error_margin':20,
	'description':,
	'movement': 
}

gall_bladder= {
	'height':50,
	'image':,
	'cut':,
	'error_margin':7,
	'description':,
	'movement': 
}

small_intestine = {
  'height':250
  'image':
  'cut':
  'error_margin':30
  'description':
  'movement':
}
large_intestine = {
  'height':350
  'image':
  'cut':
  'error_margin':10  
  'description':
  'movement':  
}
liver = {
  'height': 200
  'image':
  'cut':
  'error_margin':25
  'description':  
  'movement':
}    

stomach = {
  'height':150
  'image':
  'cut':
  'error_margin': 20
  'description':
  'movement':  
    
}

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	
	screen.fill (light_sky_blue)
	pygame.display.flip()