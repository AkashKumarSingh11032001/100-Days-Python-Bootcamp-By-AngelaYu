from turtle import Turtle

STARTING_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DIS = 20

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        #self.move()

        def create_snake(self):
            for pos in STARTING_POS:
                snake_body = Turtle("square")
                snake_body.color("white")
                snake_body.penup()
                snake_body.goto(pos)
                self.snake.append(snake_body)

        def move(self):
            for seg_num in range(len(self.snake)-1,0,-1):
                new_x = self.snake[seg_num - 1].xcor()
                new_y = self.snake[seg_num - 1].ycor()
                self.snake[seg_num].goto(new_x,new_y)

            self.snake[0].forward(MOVE_DIS)
            
