from _typeshed import Self
from floorhandler import Floor_handler
from mario import Mario
from collisionManager import Collision_manager
from basic_object import Floor
import pyxel
import time

class Board:
    """ This class contains all the information needed to represent the
    board"""
    def __init__(self, w: int, h: int):
        """ The parameters are the width and height of the board"""
        self.width = w
        self.height = h

        self.collision_manager = Collision_manager()
        self.floor_handler = Floor_handler(16, 16, self.collision_manager)

        #Create all the floorhandler in the window
        self.all_objects = [
            Floor(0, )
        ]
        self.floor_handler.create_floor(0, self.height - self.floor_handler.sprite[4])
        self.floor_handler.create_floor(16 * 3, self.height - self.floor_handler.sprite[4] * 2)
        for i in range(int((int(self.width / 16)) / 2)):
            self.floor_handler.create_floor(32 + 16 + (i * self.floor_handler.sprite[3]), self.height - self.floor_handler.sprite[4])
        self.floor_handler.create_floor(0,self.height - 2 * self.floor_handler.sprite[3])

        #self.collision_manager.create_collider()

        # This creates a Mario at the middle of the screen in x and at y = 200
        # facing right
        self.mario = Mario(self.width / 2 + .5, self.height / 2 + 0.5, True, self.collision_manager)
        #self.mario = Mario(0,0, True)

        #Time
        #TO DO: time left counter
        self.time_left = 300

        #Score
        #TO DO: Implement score in conditions
        self.score = 0

        print(self.floor_handler.floorhandler)
        #print(self.floor_handler.floor_not_fall)

    def update(self):
        #Here will be th colliders summed in just one list----------REVIEW HOW TO COPY ARRAYS SAFELY
        #NEED TO PUT THE COLLIDERS IN A VARIABLE AND THEN USE IT IN THE INIT OF MARIO ??????
        self.mario.obstacles_updater(self.collision_manager)
        (self.mario.collisions())

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.mario.accelerate('right', self.width, self.collision_manager.collision_list_x)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.mario.accelerate('left', self.width, self.collision_manager.collision_list_x)

        self.mario.jump(pyxel.btnr(pyxel.KEY_UP))
        
        self.mario.move()

        #self.score_array = []
        #for i in str(self.score):
            #self.score_array.append(i)

        #while len(str() < 5):
            #self.score_array.insert(0, "0")

    def draw(self):
        pyxel.cls(12)

        pyxel.bltm(0, 0, 1, 0, 0, 32, 16) #Change the third number to 0 (now is 1)
        # We draw Mario taking the values from the mario object
        # Parameters are x, y, image bank, the starting x and y and the size
        pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0],
                  self.mario.sprite[1], self.mario.sprite[2], self.mario.sprite[3],
                  self.mario.sprite[4], 12)

        #Drawing each block of floorhandler
        for i in self.floor_handler.floorhandler:
            pyxel.blt(
                #Position of each block
                i[0], i[1],

                #Image bank
                self.floor_handler.sprite[0],

                #Starting point
                self.floor_handler.sprite[1], self.floor_handler.sprite[2],

                #Size of the image in the bank
                self.floor_handler.sprite[3], self.floor_handler.sprite[4]
            )

        #pyxel.text(0, 0, "MARIO", 7)
        #pyxel.text(0, 16, str(self.score_array))
        pyxel.text(0, 32, str(str(self.mario.x) + " " + str(self.mario.y)), 7)