from basic_object import Basic_object
from collisionManager import Collision_manager

class Collidable_object(Basic_object):
    #Child of Basic_object (have coordinates and a sprite)
    pass

    def colliding_with(self, collision_manger:Collision_manager):
        self.collision_manager = collision_manger

        self.collading_downside = ["down"]
        self.collading_topside = ["up"]
        self.collading_rightside = ["right"]
        self.collading_leftside = ["left"]

        #Colliders In a if all the conditions are checked ?? or as soon as it is false?????'
        for i in self.collision_manager.on_scene_objects:
            #Down collider
            if self.y + self.sprite[4] == i[1] and (self.x + self.sprite[3] > i[0]) and self.x < i[0] + i[3]:
                self.collading_downside.append(i[2])
                print(self.collading_downside)

            #Upper collider
            if self.y == i[1] + i[4] and self.x + self.sprite[3] >= i[0] and self.x <= i[0] + i[3]:
                self.collading_topside.append(i[2])

            #Right collider
            if ((self.y + self.sprite[4] > i[1] and self.y < i[1] + i[4]) or 
                (self.y == i[1] and self.y + self.sprite[4] == i[1] + i[4])) and self.x + self.sprite[3] == i[0]:

                self.collading_rightside.append(i)

            #Left collider
            if ((self.y + self.sprite[4] > i[1] and self.y < i[1] + i[4]) or
                (self.y == i[1] and self.y + self.sprite[4] == i[1] + i[4])) and self.x == i[0] + i[4] in range(i[0] + i[4], i[0], -1):

                    self.collading_leftside.append(i[3])
        
        if (len(self.collading_downside) == 1 and self.acceleration_y  == 0):
            self.y += 1

        if (len(self.collading_topside) > 1):
            self.acceleration_y = 0

        if (len(self.collading_rightside) > 1):
            print(self.collading_rightside)
            print([self.x, self.y])
            if(self.acceleration_x > 0):
                self.acceleration_x = 0

        if (len(self.collading_leftside) > 2): 
            print(self.collading_leftside)
            print([self.x, self.y])
            #if(self.acceleration_x <= 0):
            self.acceleration_x = 0
        #print(self.acceleration_x)
        #return self.collading_downside