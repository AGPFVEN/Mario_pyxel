from basic_object import Basic_object
from collisionManager import Collision_manager

class Collisionable_object(Basic_object):
    def __init__(self, x, y, sprite: tuple):
        super().__init__(x, y, sprite)

    def colliding_with(self, collision_manager:Collision_manager):
        #Setting up the object which are going to collide with the object
        self.objects = collision_manager.on_scene_objects

        #This algorithm is done to establish the bounds where mario can collide
        self.collading_down = []
        self.collading_up = []
        self.collading_right = []
        self.collading_left = []
        self.collading_all = []

        #Colliders In a if all the conditions are checked ?? or as soon as it is false?????'
        for i in self.objects:
            #Down collider
            if self.y + self.sprite[4] == i.y and (self.x + self.sprite[3] > i.x) and self.x < i.x + i.sprite[3]:
                self.collading_down.append(i)
                self.collading_all.append(i)

            #Upper collider
            if self.y == i.y + i.sprite[4] and self.x + self.sprite[3] > i.x and self.x < i.x + i.sprite[3]:
                self.collading_up.append(i)
                self.collading_all.append(i)

            #Right collider
            if ((self.y + self.sprite[4] > i.y and self.y < i.y + i.sprite[3]) or 
                (self.y == i.y and self.y + self.sprite[4] == i.y + i.sprite[4])) and self.x + self.sprite[3] == i.x:

                    self.collading_right.append(i)
                    self.collading_all.append(i)

            #Left collider
            if ((self.y + self.sprite[4] > i.y and self.y < i.y + i.sprite[4]) or
                (self.y == i.y and self.y + self.sprite[4] == i.y + i.sprite[4])) and self.x == i.x + i.sprite[3]:

                    self.collading_left.append(i)
                    self.collading_all.append(i)

    def delete_from_all(self, collision_manager_list, handler_list):

        for i in range(len(collision_manager_list)): 
            if collision_manager_list[i].__dict__ == self.__dict__:
                del collision_manager_list[i]

        for k in range(len(handler_list)): 
            if handler_list[k].__dict__ == self.__dict__:
                del handler_list[k]