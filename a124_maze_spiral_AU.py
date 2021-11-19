# a124_maze_spiral_[studentinitials].py
import turtle as trtl 

size = 10

spiral = trtl.Turtle()
spiral.speed(0)

for i in range(size * 4):
    spiral.forward(i * 10)
    spiral.left(90)

wn = trtl.Screen()
wn.mainloop()