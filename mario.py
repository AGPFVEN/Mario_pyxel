from dynamic_object import Dinamic_object
import common_values

class Mario(Dinamic_object):
    def __init__(self, x: int, y: int, sprite: tuple, dir:str):
        super().__init__(x, y, sprite)

        #Initial direction of Mario
        self.direction = dir

        #Initial lives of Mario
        self.lives = 3

    def accelerate(self, direction: str, size: int, prohibited_zones: list):
        """ This is an example of a method that moves Mario, it receives the
        direction and the size of the board"""
        # Checking the current horizontal size of Mario to stop him before
        # he reaches the right border
        if direction.lower() == 'right' and self.x < size - self.sprite[3] and ([self.x + 1, self.y] not in prohibited_zones):
            if self.acceleration_x <= 1:
                self.acceleration_x += .5

        elif direction.lower() == 'left' and self.x > 0 and ([self.x -1, self.y] not in prohibited_zones):
            # I am assuming that if it is not right it will be left
            if self.acceleration_x <= 1:
                self.acceleration_x -= 0.5

    #The movement is done to move in the x axis
    def move(self):
       # if(self.acceleration_x != 0):
            #self.x += (self.acceleration_x)

        if self.acceleration_x > 0 and len(self.collading_right) == 1:
            self.x += 0.5
            self.acceleration_x -= 0.5
        
        if self.acceleration_x < 0 and len(self.collading_left) == 1:
            self.x -= 0.5
            self.acceleration_x += 0.5

        if(self.acceleration_y != 0):
            self.y -= common_values.gravity

        if(self.acceleration_y > 0):
            self.acceleration_y -= 0.5
        
        if(self.acceleration_y < 0):
            self.acceleration_y += 0.5

    #The jump is done to
    def jump(self, user_input):
        if (user_input and len(self.collading_down) > 1):
            self.acceleration_y -= 10