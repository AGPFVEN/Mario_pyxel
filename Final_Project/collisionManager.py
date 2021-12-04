from basic_object import Basic_object

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