from collisionManager import Collision_manager
import common_values

class Mario:
    #This class stores all the information needed for Mario
    def __init__(self, x:int, y:int, dir:str, collision_manager:Collision_manager):
        #This method creates the Mario object
        #param x the starting x of Mario
        #param y the starting y of Mario
        #param dir a string to store the initial direction of Mario.
        self.x = x
        self.y = y

        #Acceleration will be the variable which makes possible the slip, this feature is not
        self.acceleration_x = 0
        self.acceleration_y = 0

        #Here we are assuming Mario will be always placed at the first
        #bank at first position and it will have fixed size
        self.sprite = (0, 1, 112, 14, 16, 10)
        self.direction = dir

        #We also assume that Mario will always start with 3 lives
        self.lives = 3

        #This is the size of mario in the x axis
        self.mario_x_size = self.sprite[3]
        self.mario_y_size = self.sprite[4]

        #This is are the obstales which mario can collide with
        self.objects = collision_manager.objects_list_x
    
    def obstacles_updater(self, collision_manager:Collision_manager):
        self.objects = collision_manager.objects_list_x

    def accelerate(self, direction: str, size: int, prohibited_zones: list):
        """ This is an example of a method that moves Mario, it receives the
        direction and the size of the board"""
        # Checking the current horizontal size of Mario to stop him before
        # he reaches the right border
        if direction.lower() == 'right' and self.x < size - self.mario_x_size and ([self.x + 1, self.y] not in prohibited_zones):
            if self.acceleration_x <= 1:
                self.acceleration_x += .5

        elif direction.lower() == 'left' and self.x > 0 and ([self.x -1, self.y] not in prohibited_zones):
            # I am assuming that if it is not right it will be left
            if self.acceleration_x <= 1:
                self.acceleration_x -= 0.5

    
    #Approach: Check if the exists a block  under mario
    def collisions(self):
        #This algorithm is done to establish the bounds where mario can collide--------------
        self.collading_with_mario_down = ["down"]
        self.collading_with_mario_up = ["up"]
        self.collading_with_mario_right = ["right"]
        self.collading_with_mario_left = ["left"]

        #Colliders In a if all the conditions are checked ?? or as soon as it is false?????'
        for i in self.objects:
            #Down collider
            if self.y + self.sprite[4] == i[1] and (self.x + self.sprite[3] > i[0]) and self.x < i[0] + i[3]:
                self.collading_with_mario_down.append(i[2])
                print(self.collading_with_mario_down)

            #Upper collider
            if self.y == i[1] + i[4] and self.x + self.sprite[3] >= i[0] and self.x <= i[0] + i[3]:
                self.collading_with_mario_up.append(i[2])

            #Right collider
            if ((self.y + self.sprite[4] > i[1] and self.y < i[1] + i[4]) or 
                (self.y == i[1] and self.y + self.sprite[4] == i[1] + i[4])) and self.x + self.sprite[3] == i[0]:

                self.collading_with_mario_right.append(i)

            #Left collider
            if ((self.y + self.sprite[4] > i[1] and self.y < i[1] + i[4]) or
                (self.y == i[1] and self.y + self.sprite[4] == i[1] + i[4])) and self.x == i[0] + i[4] in range(i[0] + i[4], i[0], -1):

                    self.collading_with_mario_left.append(i[2])
        
        if (len(self.collading_with_mario_down) == 1 and self.acceleration_y  == 0):
            self.y += 1

        if (len(self.collading_with_mario_up) > 1):
            self.acceleration_y = 0

        if (len(self.collading_with_mario_right) > 1):
            print(self.collading_with_mario_right)
            print([self.x, self.y])
            if(self.acceleration_x > 0):
                self.acceleration_x = 0

        if (len(self.collading_with_mario_left) > 1): 
            print(self.collading_with_mario_left)
            print([self.x, self.y])
            #if(self.acceleration_x <= 0):
            self.acceleration_x = 0
        #print(self.acceleration_x)
        #return self.collading_with_mario_down

    #The movement is done to move in the x axis
    def move(self):
       # if(self.acceleration_x != 0):
            #self.x += (self.acceleration_x)

        if self.acceleration_x > 0 and len(self.collading_with_mario_right) == 1:
            self.x += 0.5
            self.acceleration_x -= 0.5
        
        if self.acceleration_x < 0 and len(self.collading_with_mario_left) == 1:
            self.x -= 0.5
            self.acceleration_x += 0.5

        if(self.acceleration_y != 0):
            self.y -= common_values.gravity

        if(self.acceleration_y > 0):
            self.acceleration_y -= 0.5
        
        if(self.acceleration_y < 0):
            self.acceleration_y += 0.5

    #The jump is done to
    def jump(self, user_input):
        if (user_input and len(self.collading_with_mario_down) > 1):
            self.acceleration_y -= 3