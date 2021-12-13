from dynamic_object import Dynamic_object
from collisionManager import Collision_manager

class Mario(Dynamic_object):
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
        self.direction = direction.lower()

        if self.direction == 'right' and self.x < size - self.sprite[3] and ([self.x + 1, self.y] not in prohibited_zones):
                if self.acceleration_x <= 1:
                    self.acceleration_x += .5

        elif self.direction == 'left' and self.x > 0 and ([self.x -1, self.y] not in prohibited_zones):
                # I am assuming that if it is not right it will be left
                if self.acceleration_x <= 1:
                    self.acceleration_x -= 0.5

    #The movement is done to move in the x axis
    def move(self):
       # if(self.acceleration_x != 0):
            #self.x += (self.acceleration_x)
        
        if (len(self.collading_right) > 0):
            if(self.acceleration_x > 0):
                self.acceleration_x = 0

        if (len(self.collading_left) > 0): 
            if(self.acceleration_x <= 0):
                self.acceleration_x = 0

        if self.acceleration_x > 0 and len(self.collading_right) == 0:
            self.x += 0.5
            self.acceleration_x -= 0.5
        
        if self.acceleration_x < 0 and len(self.collading_left) == 0:
            self.sprite[3]
            self.x -= 0.5
            self.acceleration_x += 0.5

        if(self.acceleration_y != 0):
            self.y -= 0.5

        if(self.acceleration_y > 0):
            self.acceleration_y -= 0.5
        
        if(self.acceleration_y < 0):
            self.acceleration_y += 0.5

    #The jump is done to
    def jump(self, user_input):
        if (user_input and len(self.collading_down) > 0):
            self.acceleration_y -= 30

    def dynamic_collision(self, collision_manager: Collision_manager):
        super().dynamic_collision(collision_manager)

        if (len(self.collading_down) == 0):
            self.sprite = [0, 1, 112, 14, 16]
        else:
            self.sprite = []