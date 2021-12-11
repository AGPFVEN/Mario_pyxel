#This object is the base of the individual objects as mario, koopas, etc
#As this is the most basic block this will be the floor

class Basic_object:
    def __init__(self, x, y,  sprite:tuple):
        #Position of te object
        self.x = x
        self.y = y
        
        #The sprites that all the elements will have
        self.sprite = sprite

        #This index is to iedntify the object in the scene
        #This is done to optimize (is better to search than to loop)
        self.index = 0