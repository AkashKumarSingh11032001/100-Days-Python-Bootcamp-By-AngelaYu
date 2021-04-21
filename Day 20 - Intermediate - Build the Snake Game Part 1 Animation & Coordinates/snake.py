STARTING_POS = [(0,0),(-20,0),(-40,0)]


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()

        def create_snake(self):
            for pos in starting_pos:
                snake_body = Turtle("square")
                snake_body.color("white")
                snake_body.penup()
                snake_body.goto(pos)
                snake.append(snake_body)

        
