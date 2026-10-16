# day_21.py — Snake Game
# Note: in my local PyCharm project, the classes below are split into separate files
# (snake.py, food.py, scoreboard.py, main.py). Here they are combined into one file
# for easier viewing.

import time
import random
from turtle import Turtle, Screen


# ---------- Constants ----------
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

# ---------- Snake class ----------
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    # Creating the snake and the starting position
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    # Creating segments of the body
    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('DarkOliveGreen2')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Adding a new segment to its body
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Hiding the snake to restart the game
    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()

    # Making snake's movements
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

# ---------- Food class ----------
class Food(Turtle):  
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("DarkSlateBlue")
        self.penup()
        self.shapesize(stretch_len= 0.5, stretch_wid= 0.5)
        self.speed("fastest")
        self.refresh()

    # Food appears randomly on a screen after being eaten
    def refresh(self):
        random_x = random.randrange(-280, 280, 20)
        random_y = random.randrange(-280, 280, 20)
        self.goto(random_x, random_y)

# ---------- Scoreboard class ----------
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("DarkGreen")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    # Updating the scoreboard / written text
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Increasing the score when the food is eaten
    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    # Game over when collision (walls, tail) happens
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)
        self.goto(0, -40)
        self.write("Click anywhere to play again", align=ALIGNMENT, font=FONT)

    # Clearing the scoreboard to restart the game
    def reset(self):
        self.clear()
        self.score = 0
        self.goto(0, 270)
        self.update_scoreboard()

  # ---------- Main game ----------
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("cornsilk1")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

def restart_game():
    global game_is_on
    if not game_is_on:                 
        snake.reset()
        food.refresh()
        score.reset()
        game_is_on = True

screen.onclick(lambda x, y: restart_game())

while True:
    screen.update()
    time.sleep(0.1)

    if game_is_on:
        snake.move()

        # Eating / Collision with food
        if snake.segments[0].distance(food) < 15:
            food.refresh()
            snake.extend()
            score.increase_score()

        # Detect collision with walls
        if (abs(snake.segments[0].xcor()) > 275 or
                abs(snake.segments[0].ycor()) > 275):
            game_is_on = False
            score.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.segments[0].distance(segment) < 10:
                game_is_on = False
                score.game_over()
              
