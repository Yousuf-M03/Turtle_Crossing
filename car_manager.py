import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 6


class CarManager(Turtle):
    def __init__(self):
        self.biler = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_cars(self):
        new_car = Turtle("square")
        s_p = random.randint(-250, 250)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.goto(y=s_p, x=300)
        self.biler.append(new_car)

    def drive(self):
        for cars in self.biler:
            cars.bk(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
