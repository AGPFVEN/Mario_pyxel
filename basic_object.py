#This object is the base of the individual objects as mario, koopas, etc
#As this is the most basic block this will be the floor

class Basic_object:
    def __init__(self, x:int , y:int , sprite:tuple):
        #Posotion of te object
        self.x = x
        self.y = y
        
        #The sprites that all the elements will have
        self.sprite = sprite