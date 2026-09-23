from tkinter import *

window = Tk()
window.title("3D map visualizer")
window.geometry("1000x1000")


# Theme
icon = PhotoImage(file= 'Assets/images.png')
window.iconphoto(True,icon)
window.config(background="black")




# main page
Hello = Label(window,
                   text ="Welcome to 3D-Coordinates Visializer", 
                   font =('Airal',40,'bold'),
                   fg='white',
                   bg='black',
                   bd = 10,
                   padx=20,
                   pady=40)


New_project= Button(window,
                    text="New Project",
                    font =('Airal',10,'bold'),
                    fg='white',
                    bg='black',)


Load_project= Button(window,
                    text="Load_Project",
                    font =('Airal',10,'bold'),
                    fg='white',
                    bg='black')


New_project.place(x=1000,y=200)
Load_project.place(x=1000,y=300)
Hello.place(x=50,y=500)
window.mainloop()
