import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()

scoreboard = Scoreboard()

player = Player()
screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")


tæller = 0


car_manager.create_cars()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.02)

    if tæller == 6:
        car_manager.create_cars()
        tæller -= 7
    tæller +=1
    car_manager.drive()

    for cars in car_manager.biler:
        if player.distance(cars) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        scoreboard.lvl_up()
        player.respawn()
        car_manager.increase_speed()



screen.exitonclick()








