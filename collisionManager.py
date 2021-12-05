from abc import abstractproperty
from basic_object import Basic_object

#This object is aimed to been used by non-static objects
class Collision_manager:
    def __init__(self):
        #List of all the objects present in the actual scene in x axis
        #self.objects_list_x = []
        self.on_scene_objects = []

        #Final list with the most relevant information for the x axis
        #self.collision_list_x = []
        self.all_objects = []

    #This function is used to add collidable objects to the list which conyains al the objects of the scene
#    def add_collider_x(self, info):
        #self.objects_list_x.append(info)

    def update_on_scene_objects(self, x_screen):
        self.on_scene_objects = []

        for i in self.all_objects:
            if i.x > 0 and i.x + i.sprite[3] < x_screen:
                self.on_scene_objects.append(i)