from tkinter import *
from main import perimeter_F,area, add_point_rtk, add_point_gps, get_gps, get_rtk, add_to_graph_gps
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = Tk()


def update_lists():
    Gps_list.delete(0, END)
    Rtk_list.delete(0, END)
    for i in range(0, len(get_gps())):
        Gps_list.insert(END, "Point " + str(i+1) + " :" + str(get_gps()[i]))
    for i in range(0, len(get_rtk())):
        Rtk_list.insert(END, "Point " + str(i+1) + " :" + str(get_rtk()[i]))

    gps_total_perimeter.config(state="normal")
    gps_total_area.config(state="normal")
    rtk_total_area.config(state="normal")
    rtk_total_perimeter.config(state="normal")

    gps_total_perimeter.delete(0,END)
    gps_total_area.delete(0,END)
    rtk_total_area.delete(0,END)
    rtk_total_perimeter.delete(0,END)

    gps_total_perimeter.insert(0,perimeter_F(get_gps()))
    gps_total_area.insert(0,area(get_gps()))
    rtk_total_area.insert(0,area(get_rtk()))
    rtk_total_perimeter.insert(0,perimeter_F(get_rtk()))








def save_rtk():
    try:
        point = [float(x.get()), float(y.get()), float(z.get())]
        add_point_rtk(point)
        x.delete(0, END)
        y.delete(0, END)
        z.delete(0, END)
        update_lists()
    except ValueError:
        print("Please enter valid numeric coordinates")


def save_gps():
    try:
        point = [float(x.get()), float(y.get()), float(z.get())]
        add_point_gps(point)
        x.delete(0, END)
        y.delete(0, END)
        z.delete(0, END)
        update_lists()
    except ValueError:
        print("Please enter valid numeric coordinates")


def generate_plot():
    add_to_graph_gps(get_gps(), get_rtk(), fig, canvas)


window.title("Project_name")
window.geometry("1100x1000")
window.config(background="black")

add_point = Button(
    window,
    text="Add to GPS",
    command=save_gps,
    bg="black",
    fg="white"
)
add_point2 = Button(
    window,
    text="Add to RTK",
    command=save_rtk,
    bg="black",
    fg="white"
)

Generate_plot = Button(
    window,
    text="Generate Plot",
    command=generate_plot,
    bg="black",
    fg="white"
)


Label(window,
      text="X Coordinate:",
      fg="white",
      bg="black").place(x=30, y=25)
x = Entry(window, font=("Arial", 12))

Label(window,
      text="Y Coordinate:",
      fg="white",
      bg="black").place(x=30, y=75)
y = Entry(window, font=("Arial", 12))

Label(window,
      text="Z Coordinate:",
      fg="white",
      bg="black").place(x=30, y=125)
z = Entry(window, font=("Arial", 12))

x.place(x=30, y=50)
y.place(x=30, y=100)
z.place(x=30, y=150)

Label(window,
      text="RTK area:",
      fg="white",
      bg="black").place(x=930, y=470)
rtk_total_area = Entry(
    window,
    font=("Arial", 12),
    state="readonly"
)
Label(window,
      text="RTK Perimeter:",
      fg="white",
      bg="black").place(x=900, y=500)
rtk_total_perimeter = Entry(
    window,
    font=("Arial", 12),
    state="readonly"
)
Label(window,
      text="GPS Area:",
      fg="white",
      bg="black").place(x=630, y=470)
gps_total_area = Entry(
    window,
    font=("Arial", 12),
    state="readonly"
)

Label(window,
      text="GPS Perimeter:",
      fg="white",
      bg="black").place(x=600, y=500)
gps_total_perimeter = Entry(
    window,
    font=("Arial", 12),
    state="readonly"
)


Gps_list = Listbox(window)
Rtk_list = Listbox(window)
point_error = Listbox(window)

gps_total_perimeter.place(x=700, y=500)
gps_total_area.place(x=700, y=470)

rtk_total_area.place(x=1000, y=470)
rtk_total_perimeter.place(x=1000, y=500)


fig = Figure(figsize=(6, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=window)
canvas_widget = canvas.get_tk_widget()


Gps_list.place(x=30, y=275)
point_error.place(x=230, y=275)
Rtk_list.place(x=430, y=275)

Generate_plot.place(x=1000, y=600)
add_point.place(x=300, y=50)
add_point2.place(x=300, y=100)
canvas_widget.place(x=650, y=50)
window.mainloop()