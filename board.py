from basic_handler import Basic_handler
from collisionable_object import Collisionable_object
from mario import Mario
from collisionManager import Collision_manager
from basic_object import Basic_object
from enemy import Enemy
import pyxel

class Board:
    """ This class contains all the information needed to represent the
    board"""
    def __init__(self, w: int, h: int):
        #The parameters are the width and height of the board
        self.width = w
        self.height = h

        #These is the initial position of mario and its sprites
        initial_mario_x = self.width / 2 + .5
        initial_mario_y = self.height / 2 + 0.5
        self.mario_sprite = [0, 1, 112, 14, 16]
        self.super_mario_sprite = [0, 48, 64, 16, 32]
        self.mario_sprite_falling = [0, 16, 0, 16, 16]
        self.super_mario_sprite_falling = [0, 16, 136, 16, 32]

        #Creating the collision manager
        self.collision_manager = Collision_manager()

        # This creates a Mario at the middle of the screen in x and at y = 200
        # facing right
        self.mario = Mario(initial_mario_x, initial_mario_y, self.mario_sprite, self.mario_sprite, self.mario_sprite_falling, "right")
        #self.mario = Mario(0,0, True)

        #Creating a handler in order to create an object just with coordintes
        self.floor_handler = Basic_handler(Basic_object(0, 0, (0, 32, 0, 16, 16)), self.collision_manager)
        self.pipe_handler = Basic_handler(Basic_object(0, 0, (0, 0, 80, 16*2, 16*2)), self.collision_manager)
        self.cleared_handler = Basic_handler(Basic_object(0, 0, (0, 0, 16, 16, 16)), self.collision_manager)
        self.destroyable_block_handler = Basic_handler(Collisionable_object(0, 0, (0, 0, 32, 16, 16)), self.collision_manager)
        self.coin_handler = Basic_handler(Collisionable_object(0,0, (0, 2, 1, 10, 13)), self.collision_manager)
        self.mushroom_handler = Basic_handler(Enemy(0, 0, [0, 32, 80, 16, 16]), self.collision_manager)
        self.goomba_handler = Basic_handler(Enemy(0, 0, [0, 16, 32, 16, 16]), self.collision_manager)
        self.koopa_handler = Basic_handler(Enemy(0, 0, [0, 32, 112, 16, 24]), self.collision_manager)
        self.koopa_shell_handler = Basic_handler(Enemy(0, 0, [0, 48, 36, 16, 11]), self.collision_manager)
        #self.koopa_shell_handler = Basic_handler(Enemy(0,0, (0, )))

        #Floor sprite
        sprite_floor = self.floor_handler.original.sprite

        #Create all the floorhandler in the window
        self.floor_handler.create_basic(1, self.height - sprite_floor[4])
        self.floor_handler.create_basic(16 * 4, self.height - sprite_floor[4] * 2)
        self.floor_handler.create_basic(16 * 6, self.height - sprite_floor[4] * 4 - 5)
        self.floor_handler.create_basic(16 * 10, self.height - sprite_floor[4] * 2)

        #print(self.floor_handler.collision_manager.all_objects[2].x)
        #print(self.floor_handler.collision_manager.all_objects[2].y + 16)       

        #demo map
        for i in range(int((int(self.width / 16)) / 2)):
            self.floor_handler.create_basic(32 + 16 + (i * sprite_floor[3]), self.height - sprite_floor[4])
        self.floor_handler.create_basic(0, self.height - 2 * sprite_floor[3])

        self.mushroom_handler.create_basic(16 * 7, self.height - self.koopa_handler.original.sprite[4] * 2 - 4)

       # self.koopa_handler.create_basic(16* 10, self.height - self.koopa_handler.original.sprite[4] * 2 - 4)
        self.floor_handler.create_basic(16 * 13, self.height - self.koopa_handler.original.sprite[4] * 2 - 4)
        #self.mushroom_handler.create_basic(16 * 11, self.height - self.koopa_handler.original.sprite[4] * 2 - 4)

        #Time
        #TO DO: time left counter
        self.time_left = 300

        #Score
        #TO DO: Implement score in conditions
        self.score = 0

        #Coins
        self.coins = 0

        #Points
        self.points = 0
        
        #This list is done to create the level again
        self.all_objects_auxiliar = self.collision_manager.all_objects

        for i in range(50):
            self.floor_handler.create_basic(i * 10, self.height - sprite_floor[4])

    def update(self):

        #Move with Mario
        #if self.mario.x > self.width / 2:
            #self.mario.x = self.width/ 2
            #for i in self.collision_manager.all_objects:
                #i.x -= 1

        #Objects which are on the scene
        #print(self.collision_manager.all_objects)
        for i in self.collision_manager.all_objects:
            if(type(i) == type(self.mushroom_handler.original)): 
                i.dynamic_collision(self.collision_manager)
                i.movement()

        #Collision Manager refreshing
        self.collision_manager.update_on_scene_objects(self.width)
        self.objects_on_scene = self.collision_manager.on_scene_objects

        #Refreshing collider of Mario
        self.mario.dynamic_collision(self.collision_manager)

        #This will be the place where is declared how mario interacts with the rest of objects
        for i in self.mario.collading_all:

            #Mushroom behavior
            if i.sprite == self.mushroom_handler.original.sprite:
                old_size_y = self.mario.sprite[4]
                self.mario.sprite_original = self.super_mario_sprite
                self.mario.sprite_falling = self.super_mario_sprite_falling
                self.mario.y -= (self.mario.sprite_original[4] - old_size_y)
                i.delete_from_all(self.collision_manager.all_objects, self.mushroom_handler.container_of) 

            #Goomba, koopa troppa and koopa shell behaviors
            if (not (i in self.mario.collading_down)) and type(i) == type(self.goomba_handler.original):
                if (self.mario.sprite == self.super_mario_sprite):
                    self.mario.sprite = self.mario_sprite
            
                else:
                    print("exit")

            #Coin behavior
            if i.sprite == self.coin_handler.original.sprite:
                self.coins += 1  
                i.delete_from_all(self.collision_manager.all_objects, self.mushroom_handler.container_of) 

        for i in self.mario.collading_up:

            #Block behaviour
            if i.sprite == self.destroyable_block_handler.original.sprite:
                i.delete_from_all(self.collision_manager.all_objects, self.mushroom_handler.container_of)

        for i in self.mario.collading_down:

            #Goomba and koppa shell
            if i.sprite != self.mushroom_handler.original.sprite and type(i) == type(self.goomba_handler.original):
                i.delete_from_all(self.collision_manager.all_objects, self.mushroom_handler.container_of)

                if i.sprite == self.koopa_handler.original.sprite:
                    self.koopa_shell_handler.create_basic(i.x, i.y)

        for i in self.koopa_shell_handler.container_of:
            for k in i.collading_all:
                if (type(k) == Enemy or type(k) == Mario) and i.sprite != self.mushroom_handler.original.sprite:
                    i.delete_from_all

        #Movement of Mario
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.mario.accelerate('right', self.width, self.objects_on_scene)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.mario.accelerate('left', self.width, self.objects_on_scene)

        self.mario.jump(pyxel.btnr(pyxel.KEY_UP))
        
        self.mario.move()

        #Score processing
        self.score_array = []
        self.score_string = ""
        for i in str(self.score):
            self.score_array.append(i)

        for _ in range(5 - len(self.score_array)):
            self.score_array.insert(0, "0")

        for i in self.score_array:
            self.score_string += str(i)

    def draw(self):
        #This is done to delete the previous frame
        pyxel.cls(12)

        # Parameters are x, y, image bank, the starting x and y and the size
        if(self.mario.direction == "right"):
            pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0],
                    self.mario.sprite[1], self.mario.sprite[2], self.mario.sprite[3],
                    self.mario.sprite[4], 12)
        else:

            pyxel.blt(self.mario.x, self.mario.y, self.mario.sprite[0],
                    self.mario.sprite[1], self.mario.sprite[2], -self.mario.sprite[3],
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
        pyxel.text(0, 7, str(self.score_string), 7)
        pyxel.text(40, 0, "Coins x ", 7)
        pyxel.text(40, 7, str(self.coins), 7)
        pyxel.text(90, 0, "World", 7)
        pyxel.text(90, 7, "1x1", 7)
        pyxel.text(0, 32, str(str(self.mario.x) + " " + str(self.mario.y)), 7)

    #This could be done to implement checkpoints with merely implement a change in a list
    #def reset_level(list_of_check, collision_manager)