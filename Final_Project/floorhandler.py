from collisionManager import Collision_manager
from basic_object import Basic_object

class Floor_handler(Basic_object):
    def __init__(self, basic_object:Basic_object, collision_manager:Collision_manager):
        #The sprites that all the elements will have
        self.object_sprite = basic_object.sprite

        #Size of all the objects of x and y size
        self.object_size_X = basic_object.sprite[3]
        self.object_size_y = basic_object.sprite[4]

        self.collision_manager = collision_manager

        #A list with all the object of this type
        #self.object_ls = []

        #Add the necessary info in the collision object
        #self.collision_manager = collision_manager

        ##Declaring the type of blockj
        #self.type = "floor"

    #This function creates blocks (by programing them)
    #It is used for the floor because it`s faster to develop with a loop

    def create_floor(self, new_x, new_y):
        self.collision_manager.all_objects.append(Basic_object(new_x, new_y, self.sprite))


        #information = [new_x, new_y, ]
        #self.floor.append(information)
        #self.collision_manager.add_collider_x(information)

    ##This function will create a list which contains the range of the floors
    #The approach is to check the upper corners so the player can't traspass them