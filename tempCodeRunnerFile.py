from tkinter import *
from functions import add_to_graph_gps

window = Tk()
def save():
    x1 = x.get()
    y1 = y.get()
    z1 = z.get()
    a = [x1,y1,z1]
    add_to_graph_gps(a)