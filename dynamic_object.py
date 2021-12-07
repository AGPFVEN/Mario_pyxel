from collisionable_object import Collisionable_object
from collisionManager import Collision_manager

class Dinamic_object(Collisionable_object):
    #Child of Basic_object (have coordinates and a sprite)
    def __init__(self, x: int, y: int, sprite: tuple):
        #Using the init of the parent
        super().__init__(x, y, sprite)

        #Using new variables in object
        self.acceleration_x = 0
        self.acceleration_y = 0

    #Reaction of object if colliding
    def dynamic_collision(self, collision_manager: Collision_manager):
        self.colliding_with(collision_manager)

        if (len(self.collading_down) == 1 and self.acceleration_y  == 0):
            self.y += 1

        if (len(self.collading_up) > 1):
            self.acceleration_y = 0

        if (len(self.collading_right) > 1):
            if(self.acceleration_x > 0):
                self.acceleration_x = 0

        if (len(self.collading_left) > 1): 
            if(self.acceleration_x <= 0):
                self.acceleration_x = 0
        