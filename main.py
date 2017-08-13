import pygame
import sys
pygame.init()

size = width, height = 1280, 720


light_sky_blue = 135, 206, 250	 

screen = pygame.display.set_mode(size)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	screen.fill (light_sky_blue)

	pygame.display.flip()