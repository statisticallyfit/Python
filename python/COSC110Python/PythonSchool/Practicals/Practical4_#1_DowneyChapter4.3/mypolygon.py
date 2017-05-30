
import turtle
import tkinter

bob = turtle.Turtle()
print(bob)


# the program
for i in range(4):
    bob.fd(100)
    bob.lt(90) # turning left 90 degrees

# end program

turtle.mainloop()