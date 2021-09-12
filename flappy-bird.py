import pygame, sys

from pygame.constants import K_SPACE

def build_floor():
    screen.blit(floor_surface, (floor_xpos, 800))
    screen.blit(floor_surface, (floor_xpos + 500, 800))



#starting our game
pygame.init()
screen = pygame.display.set_mode((500, 1000))
clock = pygame.time.Clock()

#load and scale the background image to fit our game window
bg_surface = pygame.image.load('/home/pramitsingh0/Documents/sprites/background-day.png')
bg_surface = pygame.transform.scale2x(bg_surface).convert()

#load and scale the floor image
floor_surface = pygame.image.load('/home/pramitsingh0/Documents/sprites/base.png')
floor_surface = pygame.transform.scale2x(floor_surface).convert()
floor_xpos = 0

bird_surface = pygame.image.load('/home/pramitsingh0/Documents/sprites/bluebird-midflap.png')
bird_surface = pygame.transform.scale2x(bird_surface).convert()
bird_rect = bird_surface.get_rect(center = (100, 512))

#load and scale pipe
# pipe_surface = pygame.image.load("sprites/")

#gravity
gravity = 0.10
bird_movement = 0


#display surface
while True:
    #gets every event happening in your computer right now. and returns a list of it
    for event in pygame.event.get():
        #if the even is clicking on cross button, then it closes the game window
        if event.type == pygame.QUIT:
            pygame.quit()     #uninitialize pygame
            sys.exit(0)      #properly quit the program as a whole
        
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                bird_movement = 0
                bird_movement -= 5

    #put our surface on top of display surface
    screen.blit(bg_surface, (0, 0))

    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)

    build_floor()
    floor_xpos -= 1
    #loop the floor
    if floor_xpos < -500: floor_xpos = 0


    





    pygame.display.update()
    clock.tick(120)

