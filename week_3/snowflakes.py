"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow")


class SnowFlake():
    '''
    This class will be used to create the SnowFlake Objects.
    It takes: 
        size - an integer that tells us how big we want the snowflake
        position - a 2 item list that tells us the coordinates of the snowflake (x,y) 
        wind - a boolean that lets us know if there is any wind or not.  
    '''

    def __init__(self, size, x_position, y_position, wind=False):
        self.size = size
        self.x_position = x_position
        self.y_position = y_position
        self.wind = wind
    
    
    def fall(self, speed, y_position, x_position, wind=False):
        self.speed = speed
        self.y_position += self.speed
        if wind == True:
            self.x_position += 1
        if self.y_position >= 700 or self.x_position >= 900:
            self.y_position = 0
            self.x_position = x_position
        """
        Take in a integer that represnts the speed at which the snowflake is falling in the y-direction.  
        A positive integer will have the snowflake falling down the screen. 
        A negative integer will have the snowflake falling up the screen. 
        
        If wind = True
            - the x direction of the snowflake changes
        """
        
    def draw(self, x_position, y_position):
        pygame.draw.circle(screen, WHITE, [self.x_position, self.y_position], self.size)
        """
        Uses pygame and the global screen variable to draw the snowflake on the screen
        """
        

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# Speed
speed = random.randint(1, 3)
size = random.randint(3, 9)
y_position = 100

screen.fill(GREEN)

#snowflake_num = ['Snowflake1', 'Snowflake2', 'Snowflake3', 'Snowflake4', 'Snowflake5']

#INITIALIZE YOUR SNOWFLAKE HERE! 
for i in range(5):
    x_position = random.randint(10, 400)
    snow_name = SnowFlake(size, x_position, y_position, False)


# Snow List
snow_list = []

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    

    # --- Game logic should go here

    # --- Screen-clearing code goes here
    screen.fill(GREEN)
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.


    # --- Drawing code should go here
    # Begin Snow

    for i in range(5):
        snow_name.draw(random.randint(100, 400), y_position)
        snow_name.fall(speed, y_position, x_position, True)
    


    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
