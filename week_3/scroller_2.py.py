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
BLACK = (50, 50, 50)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (50, 100, 120)
GREY = (129, 129, 129)
colors = [BLACK, GREY, BLUE, WHITE]

def random_color():
    return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

width = random.randint(20, 60)

class Building():

    def __init__(self, x_point, y_point, width, height, color):
        self.x_point = x_point
        self.y_point = y_point
        self.color = color
        self.width = width

        self.height = height
        

    """
    This class will be used to create the building objects.

    It takes:
      x_point - an integer that represents where along the x-axis the building will be drawn
      y_point - an integer that represents where along the y-axis the building will be drawn
      Together the x_point and y_point represent the top, left corner of the building

      width - an integer that represents how wide the building will be in pixels.
            A positive integer draws the building right to left(->).
            A negative integer draws the building left to right (<-).
      height - an integer that represents how tall the building will be in pixels
            A positive integer draws the building up 
            A negative integer draws the building down 
      color - a tuple of three elements which represents the color of the building
            Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.

    It depends on:
        pygame being initialized in the environment.
        It depends on a "screen" global variable that represents the surface where the buildings will be drawn

    """
    
    def draw(self):
        #width = random.randint(20, 60)
        pygame.draw.rect(screen, self.color, (self.x_point, self.y_point, self.width, self.height))
        """
        uses pygame and the global screen variable to draw the building on the screen
        """

    def move(self, speed):
        """
        Takes in an integer that represents the speed at which the building is moving
            A positive integer moves the building to the right ->
            A negative integer moves the building to the left  <-
        Moves the building horizontally across the screen by changing the position of the
        x_point by the speed
        """
        self.x_point += speed
        if self.x_point >= 800:
            self.x_point = -self.width



class Scroller(object):


    """
    Scroller object will create the group of buildings to fill the screen and scroll

    It takes:
        width - an integer that represents in pixels the width of the scroller
            This should only be a positive integer because a negative integer will draw buildings outside of the screen
        height - an integer that represents in pixels the height scroller
            A negative integer here will draw the buildings upside down.
        base - an integer that represents where along the y-axis to start drawing buildings for this
            A negative integer will draw the buildings off the screen
            A smaller number means the buildings will be drawn higher up on the screen
            A larger number means the buildings will be drawn further down the screen
            To start drawing the buildings on the bottom of the screen this should be the height of the screen
        color - a tuple of three elements which represents the color of the building
              Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.
        speed - An integer that represents how fast the buildings will scroll

    It depends on:
        A Building class being available to create the building obecjts.
        The building objects should have "draw" and "move" methods.

    Other info:
        It has an instance variable "buildings" which is a list of buildings for the scroller
    """

    def __init__(self, width, height, base, color, speed):
        self.width = width
        self.height = height
        self.base = base
        self.color = color
        self.speed = speed
        self.building_list = []
        self.combined_width = 0

        
    def add_buildings(self, ran1, ran2, build_color):
        self.ran1 = ran1
        self.ran2 = ran2
        self.build_color = build_color
        while self.combined_width < self.width:
            self.add_building(self.combined_width, self.ran1, self.ran2, build_color)

        """
        Will call add_building until there the buildings fill up the width of the
        scroller.
        """

    def add_building(self, x_location, rand1, rand2, build_color):
        y_location = 471
        self.x_location = x_location
        self.rand1 = rand1
        self.rand2 = rand2
        self.build_color = build_color
        width = random.randint(10, 60)

        building1 = Building(x_location, y_location, width, random.randint(self.rand1, self.rand2), self.build_color)
        self.building_list.append(building1)
        self.combined_width += width
        """
        takes in an x_location, an integer, that represents where along the x-axis to
        put a buildng.
        Adds a building to list of buildings.
        """

    def draw_buildings(self):
        for current_building in self.building_list:
            current_building.draw()
        """
        This calls the draw method on each building.
        """

    def move_buildings(self, speed):
        self.speed = speed
        for current_building in self.building_list:
            current_building.move(self.speed)

        """
        This calls the move method on each building passing in the speed variable
        As the buildings move off the screen a new one is added.
        """

class Moon():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coverage = 40

    def draw_moon(self):
        pygame.draw.ellipse(screen, GREY, (self.x, self.y, 50, 50))
        pygame.draw.ellipse(screen, BACKGROUND_COLOR, (self.x + self.coverage, self.y, 50, 50))


    def move_moon(self, speed):
        y_speed = .1
        self.speed = speed
        self.coverage -= .03
        self.x += self.speed
        if self.x > 0 and self.x < 400:
            self.y -= y_speed
        elif self.x > 400 and self.x < 800:
            self.y += y_speed
        if self.x > 800:
            self.x = -25
            self.coverage = 40

class Sprite():

    def __init__(self, x_position):
        self.x_position = x_position

    def draw_sprite(self):
        def right_leg():
            pygame.draw.rect(screen, BLACK, (self.x_position + 12, 510, 5, 20))
        def left_leg():
            pygame.draw.rect(screen, BLACK, (self.x_position + 12, 510, 5, 20))
        
        right_leg()
        left_leg()

        #pygame.transform.rotate(right_leg, 10)

        pygame.draw.ellipse(screen, RED, (self.x_position, 490, 30, 30))
        pygame.draw.ellipse(screen, BLACK, (self.x_position + 18, 498, 5, 5))

    def move_sprite(self):
        speed = 2
        if self.x_position >= 400:
            speed = 0
        else:
            self.x_position += speed
        


ball1 = Sprite(-20)

luna = Moon(-10, 160)

FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 79, 89)

front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)


front_scroller.add_buildings(-100, -50, WHITE)
middle_scroller.add_buildings(-150, -100, GREY)
back_scroller.add_buildings(-200, -150, BLACK)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BACKGROUND_COLOR)

    # --- Drawing code should go here
    luna.draw_moon()
    luna.move_moon(.3)

    pygame.draw.rect(screen, (100, 100, 100), (0, 471, 800, 150))

    ball1.draw_sprite()
    ball1.move_sprite()

    back_scroller.draw_buildings()
    back_scroller.move_buildings(1)
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings(2)
    front_scroller.draw_buildings()
    front_scroller.move_buildings(3)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
