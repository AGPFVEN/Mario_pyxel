from collisionManager import Collision_manager
from basic_object import Basic_object

#This object facilitates the coding because i won't need to declare the type of object in the board
class Basic_handler(Basic_object):
    def __init__(self, basic_object:Basic_object, collision_manager:Collision_manager):
        #Original object
        self.original = basic_object

        #Size of all the objects of x and y size
        self.object_size_X = basic_object.sprite[3]
        self.object_size_y = basic_object.sprite[4]

        #This object is added in order to add the objects of this type
        self.collision_manager = collision_manager

        #This list will contain all the objects of the same type
        self.container_of = []

    #This function creates blocks (by programing them in the board)
    #This is focused on facilitating the programming and setting up of the level
    #This approach would be very helpful if we actually wanted to create multiple levels of Mario
    def create_basic(self, new_x, new_y):

        #This part of the method tries to replicate how python works
        #Fistly creating a new object of variable type and then execute the init method
        aux_object = self.original.__new__(type(self.original))
        aux_object.__init__(new_x, new_y, self.original.sprite)
        
        #This will only append this object a list of all the objects in the level
        self.collision_manager.all_objects.append(aux_object)

        #This will append the object to the list which contains the objects of the same type
        self.container_of.append(aux_object)