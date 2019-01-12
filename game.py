import pygame
from variables import Variable as v
from render import Render as r
from controls import Controls as c
from update import Update as u


# Initialize the game
pygame.init()

# All game variables here
variable = v()
# Responsible for rendering
render = r()
# Update world variables based on input
update = u()
# Player control
controls = c()
screen = pygame.display.set_mode((variable.width, variable.height))
# Player input 0 - W, 1 - A, 2 - S, 3 - D
keys = [False, False, False, False]

# Start game loop
while 1:
    # Update the world variables based on player input
    update.fixTimeStep(variable, keys)
    
    # Draw and update the screen
    render.loadScreen(screen, variable.sky, variable.hills, variable.trees)
    render.loadRoad(variable, screen)
    # Actually render the image
    pygame.display.flip()

    # Register player input
    for event in pygame.event.get():
        controls.inputs(event, keys)
    # Deals with all input that doesn't affect the gameplay; escape, etc...
    controls.output(event)
