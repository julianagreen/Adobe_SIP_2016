import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (100, 255, 0)
RED = (255, 0, 0)
BLUE = (60, 155, 186)
GREY = (127, 127, 200)

color_list = [BLACK, WHITE, RED, BLUE, GREY]

x_ball = 350
y_ball = 250
radius = random.randint(20, 80)

random_x = random.randint(-10, 10)
random_y = random.randint(-10, 10)

pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# -------- Main Program Loop -----------

while not done:
    screen.fill(GREEN)
    random_color = random.randint(0, len(color_list) - 1)
    
    x_ball += random_x
    y_ball += random_y

    pygame.draw.circle(screen, color_list[random_color], (x_ball, y_ball), radius, 0)

    if x_ball >= 700-radius or x_ball <= 0+radius:
         random_x = -random_x

    if y_ball >= 500-radius or y_ball <= radius:
        random_y = -random_y

        #random_x = random.randint(-10, 10)
        #random_y = random.randint(-10, 10)
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
