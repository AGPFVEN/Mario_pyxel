from collisionManager import Collision_manager
from dynamic_object import Dynamic_object
from mario import Mario

class Enemy(Dynamic_object):
    pass

    def movement(self):
        if self.acceleration_x == 0:
            self.acceleration_x = 1

        if len(self.collading_left) > 0:
            #self.sprite[3] *= -1
            self.acceleration_x = 1
        
        if len(self.collading_right) > 0:
            #self.sprite[3] *= -1
            self.acceleration_x = -1

        self.x += self.acceleration_x