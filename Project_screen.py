from tkinter import *
# Import the helper functions alongside the add functions
from main import add_point_rtk, add_point_gps, get_gps, get_rtk, add_to_graph_gps

window = Tk()

# --- Small function to refresh your listboxes when buttons are clicked ---
def update_lists():
    Gps_list.delete(0, END)
    Rtk_list.delete(0, END)
    
    # Using your exact loop logic, just fixed the syntax!
    for i in range(0, len(get_gps())):
        Gps_list.insert(END, "Point " + str(i+1) + " :" + str(get_gps()[i]))
        
    for i in range(0, len(get_rtk())):
        Rtk_list.insert(END, "Point " + str(i+1) + " :" + str(get_rtk()[i]))

def save_rtk():
    try:
       
        point = [float(x.get()), float(y.get()), float(z.get())]
        add_point_rtk(point)
        
        x.delete(0, END)
        y.delete(0, END)
        z.delete(0, END)
        update_lists() # Updates listbox text
    except ValueError:
        print("Please enter valid numeric coordinates")

def save_gps():
    try:
        point = [float(x.get()), float(y.get()), float(z.get())]
        add_point_gps(point)
        x.delete(0, END)
        y.delete(0, END)
        z.delete(0, END)
        update_lists() # Updates listbox text
    except ValueError:
        print("Please enter valid numeric coordinates")

def generate_plot():
    add_to_graph_gps(get_gps(), get_rtk())


window.title("Project_name")
window.geometry("1100x1000") # Made slightly wider so the RTK button isn't cut off
window.config(background="black")

add_point = Button(
    text = "Add to GPS",
    command = save_gps,
    bg = "black",
    fg = "white"
)
add_point2 = Button(
    text = "Add to RTK",
    command = save_rtk,
    bg = "black",
    fg = "white"
)

Generate_plot = Button(
    text = "Generate Plot",
    command = generate_plot,
    bg = "black",
    fg = "white"
)




Label(window,
       text="X Coordinate:",
         fg="white",
           bg="black").place(x=30, y=25)
x = Entry(window, font = ("Arial", 12))

Label(window,
      text="Y Coordinate:",
      fg="white", 
      bg="black").place(x=30, y=75)
y = Entry(window, font = ("Arial", 12))

Label(window, 
      text="Z Coordinate:", 
      fg="white", 
      bg="black").place(x=30, y=125)
z = Entry(window, font = ("Arial", 12))

x.place(x=30, y=50)
y.place(x=30, y=100)
z.place(x=30, y=150)

Gps_list = Listbox(window)
Rtk_list = Listbox(window)
point_error = Listbox(window)

Gps_list.place(x = 30 , y = 275)
point_error.place(x=230,y=275)
Rtk_list.place(x = 430 , y = 275)

Generate_plot.place(x=850, y=500)
add_point.place(x=300, y=50)
add_point2.place(x=300, y=100)

window.mainloop()