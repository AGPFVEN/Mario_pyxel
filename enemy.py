from dynamic_object import Dynamic_object

class Enemy(Dynamic_object):
    pass

    def movement(self):
        if self.acceleration_x == 0:
            self.acceleration_x = 1

        if len(self.collading_left) > 0:
            self.acceleration_x = 1
        
        if len(self.collading_right) > 0:
            self.acceleration_x = -1

        self.x += self.acceleration_x