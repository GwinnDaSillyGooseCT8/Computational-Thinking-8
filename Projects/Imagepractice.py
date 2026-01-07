# Section 1 - Your code
from utils import *
set_background("garbybackround")

s1 = create_sprite("aliencat", 170, -220)
s2 = create_sprite("aliencat", 1, -220)
s2 = create_sprite("aliencat", -170, -220)

message1 = create_sprite("alien",-200,200)
message1.color("green")
message1.write("Alien convention!",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()