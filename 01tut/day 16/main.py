# import turtle
#
# timmy = turtle.Turtle()
# timo = turtle.Turtle()
# my_screen = turtle.Screen()
#
# print(timmy)
# print(timo)
# timo.color("blue", "coral")
# timo.shape("turtle")
# timmy.shape("turtle")
# timmy.color("blue", "DarkOrange")
# timmy.forward(100)
# timmy.forward(200)
# # Object attribute
# # my_screen.canvheight
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)
