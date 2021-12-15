import random
import arcade
SCREAN_WIDTH =500
SCREAN_HEIGHT =500

class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.width = 16
        self.height = 16
        self.color_1 = arcade.color.GREEN
        self.color_2 =arcade.color.DARK_LAVENDER
        self.change_x = 0
        self.change_y = 0
        self.score = 0
        self.center_x = SCREAN_WIDTH //2
        self.center_y =SCREAN_HEIGHT //2
        self.speed = 3
        self.body = []
        
    def move(self):
        self.body.append([self.center_x ,self.center_y])
        if len(self.body)> self.score:
            self.body.pop(0)

        if self.change_x > 0:
            self.center_x += self.speed
        elif self.change_x <0:
            self.center_x -= self.speed
        if self.change_y > 0:
            self.center_y += self.speed
        elif self.change_y <0:
            self.center_y -= self.speed

    def eat(self):
        self.score +=1
    def draw (self):
        arcade.draw_rectangle_filled(self.center_x ,self.center_y ,self.width ,self.height ,self.color_1)
        for i in range(len(self.body)):
            if i %2 == 0:
                arcade.draw_rectangle_filled(self.body[i][0],self.body[i][1],self.width ,self.height ,self.color_2)
            else:
                arcade.draw_rectangle_filled(self.body[i][0],self.body[i][1],self.width ,self.height ,self.color_1)

        

class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height =16
        self.color = arcade.color.RED
        self.r = 8
        self.center_x = random.randint(0 , SCREAN_WIDTH)
        self.center_y = random.randint(0 , SCREAN_HEIGHT)
    
    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)


        pass
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = SCREAN_WIDTH , height = SCREAN_HEIGHT , title ="snaks game ")
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake()
        self.apple = Apple()

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()

        #tamam mantegh
    def on_update(self, delta_time: float):
        self.snake.move()
        if arcade.check_for_collision(self.snake , self.apple):
            self.snake.eat()
            self.apple = Apple()
            print(self.snake.score)

        



    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif key == arcade.key.LEFT:
            self.snake.change_x  = -1
            self.snake.change_y = 0
        elif key == arcade.key.UP:
            self.snake.change_y = 1
            self.snake.change_x = 0
        elif key == arcade.key.DOWN:
            self.snake.change_y = -1
            self.snake.change_x = 0
            


my_game = Game()
arcade.run()