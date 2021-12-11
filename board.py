from basic_handler import Basic_handler
from mario import Mario
from collisionManager import Collision_manager
from basic_object import Basic_object
from mushroom import Mushroom
import pyxel

class Board:
    """ This class contains all the information needed to represent the
    board"""
    def __init__(self, w: int, h: int):
        #The parameters are the width and height of the board
        self.width = w
        self.height = h

        #These is the initial position of mario
        initial_mario_x = self.width / 2 + .5
        initial_mario_y = self.height / 2 + 0.5

        #Creating the collision manager
        self.collision_manager = Collision_manager()

        # This creates a Mario at the middle of the screen in x and at y = 200
        # facing right
        self.mario = Mario(initial_mario_x, initial_mario_y, (0, 1, 112, 14, 16), "right")
        #self.mario = Mario(0,0, True)

        #Creating a handler in order to create an object just with coordintes
        self.floor_handler = Basic_handler(Basic_object(0, 0, (0, 32, 0, 16, 16)), self.collision_manager)
        self.mushroom_handler = Basic_handler(Mushroom(0, 0, (0, 32, 80, 16, 16)), self.collision_manager)

        #Floor sprite
        sprite_floor = self.floor_handler.original.sprite

        #Create all the floorhandler in the window
        self.floor_handler.create_basic(1, self.height - sprite_floor[4])
        self.floor_handler.create_basic(16 * 4, self.height - sprite_floor[4] * 2)
        self.floor_handler.create_basic(16 * 6, self.height - sprite_floor[4] * 4)
        self.floor_handler.create_basic(16 * 10, self.height - sprite_floor[4] * 2)

        #print(self.floor_handler.collision_manager.all_objects[2].x)
        #print(self.floor_handler.collision_manager.all_objects[2].y + 16)       

        for i in range(int((int(self.width / 16)) / 2)):
            self.floor_handler.create_basic(32 + 16 + (i * sprite_floor[3]), self.height - sprite_floor[4])
        self.floor_handler.create_basic(0,self.height - 2 * sprite_floor[3])

        self.mushroom_handler.create_basic(16 * 5, self.height - self.mushroom_handler.original.sprite[4] * 2 - 4)


        #Time
        #TO DO: time left counter
        self.time_left = 300

        #Score
        #TO DO: Implement score in conditions
        self.score = 0

        #print(self.floor_handler.floorhandler)
        #print(self.floor_handler.floor_not_fall)

    def update(self):
        #Objects which are on the scene
        #print(self.collision_manager.all_objects)
        for i in self.mushroom_handler.container_of:
            i.dynamic_collision(self.collision_manager)
            i.movement()

        #Collision Manager refreshing
        self.collision_manager.update_on_scene_objects(self.width)
        self.objects_on_scene = self.collision_manager.on_scene_objects

        #Refreshing collider of Mario
        self.mario.dynamic_collision(self.collision_manager)

        #Activate super Mario
        for i in self.mario.collading_all:
            old_size_x = self.mario.sprite[4]

            if (i == type(self.mushroom_handler.original)):
                self.mario.sprite = (0, 48, 64, 16, 32)

            self.mario.y -= (self.mario.sprite[4] - old_size_x)
            
            for k in self.collision_manager.all_objects:
                if k == i:
                    del k

        #Movement of Mario
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.mario.accelerate('right', self.width, self.objects_on_scene)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.mario.accelerate('left', self.width, self.objects_on_scene)

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
        for i in self.mario.collading_all:
            if (i == type(self.mushroom_handler.original)):
                self.mario.sprite = (0, 48, 64, 16, 32)# We draw Mario taking the values from the mario object
            
        # Parameters are x, y, image bank, the starting x and y and the size
        pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0],
                  self.mario.sprite[1], self.mario.sprite[2], self.mario.sprite[3],
                  self.mario.sprite[4], 12)

        #Drawing each block of floorhandler
        for i in self.collision_manager.on_scene_objects:
            pyxel.blt(
                #Position of each block
                i.x, i.y,

                #Image bank
                i.sprite[0],

                #Starting point
                i.sprite[1], i.sprite[2],

                #Size of the image in the bank
                i.sprite[3], i.sprite[4], 
                
                #Colkey (color del fondo)
                12
            )

        pyxel.text(0, 0, "MARIO", 7)
        #pyxel.text(0, 16, str(self.score_array))
        pyxel.text(0, 32, str(str(self.mario.x) + " " + str(self.mario.y)), 7)