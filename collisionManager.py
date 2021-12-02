from basic_object import Basic_object

class Collision_manager:
    def __init__(self, x_screen, y_screen):
        #List of all the objects present in the actual scene in x axis
        #self.objects_list_x = []
        self.on_scene_objects = []

        #Final list with the most relevant information for the x axis
        #self.collision_list_x = []
        self.all_objects = []

        #Use the screensize to selec which blocks to process
        self.x_screen = x_screen
        self.y_screen = y_screen

    #This function is used to add collidable objects to the list which conyains al the objects of the scene
#    def add_collider_x(self, info):
        #self.objects_list_x.append(info)

    def update_on_scene_objects(self):
