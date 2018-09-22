from turtle import *
n = int(input("enter a number"))
for i in range(n):
    forward(100)
    left(360/n)
mainloop()