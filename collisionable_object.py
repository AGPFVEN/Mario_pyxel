from basic_object import Basic_object
from collisionManager import Collision_manager

class Collisionable_object(Basic_object):
    pass

    def colliding_with(self, collision_manager:Collision_manager):
        #Setting up the object which are going to collide with the object
        objects = collision_manager.on_scene_objects

        #This algorithm is done to establish the bounds where mario can collide
        self.collading_down = ["down"]
        self.collading_up = ["up"]
        self.collading_right = ["right"]
        self.collading_left = ["left"]
        self.collading_all = ["all"]

        #Colliders In a if all the conditions are checked ?? or as soon as it is false?????'
        for i in objects:
            #Down collider
            if self.y + self.sprite[4] == i.y and (self.x + self.sprite[3] > i.x) and self.x < i.x + i.sprite[3]:
                self.collading_down.append(type(i))
                self.collading_all.append(type(i))

            #Upper collider
            if self.y == i.y + i.sprite[4] and self.x + self.sprite[3] > i.x and self.x < i.x + i.sprite[3]:
                self.collading_up.append(type(i))
                self.collading_all.append(type(i))

            #Right collider
            if ((self.y + self.sprite[4] > i.y and self.y < i.y + i.sprite[3]) or 
                (self.y == i.y and self.y + self.sprite[4] == i.y + i.sprite[4])) and self.x + self.sprite[3] == i.x:

                    self.collading_right.append(type(i))
                    self.collading_all.append(type(i))

            #Left collider
            if ((self.y + self.sprite[4] > i.y and self.y < i.y + i.sprite[4]) or
                (self.y == i.y and self.y + self.sprite[4] == i.y + i.sprite[4])) and self.x == i.x + i.sprite[3]:

                    self.collading_left.append(type(i))
                    self.collading_all.append(type(i))