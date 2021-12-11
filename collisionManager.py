#This object is aimed to been used by non-static objects
class Collision_manager:
    def __init__(self):
        #List of all the objects that are actually in scene
        self.on_scene_objects = []

        #Final list with all the objects of the level
        self.all_objects = []

    #This method refresh the position of all the objects in the level
    #This could be optimazed, with a boolean variable to verify if the object has moved, but it is not worth it at all
    def update_on_scene_objects(self, x_screen):

        self.on_scene_objects = []

        for i in self.all_objects:
            if i.x > 0 and i.x + i.sprite[3] < x_screen:
                self.on_scene_objects.append(i)