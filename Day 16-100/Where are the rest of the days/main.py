from turtle import Turtle, Screen
tuty = Turtle()
print(tuty)
tuty.shape("turtle")
tuty.color("green")
tuty.forward(100)
tuty.left(90)
tuty.forward(150)
tuty.left(90)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu", "Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
print(table)