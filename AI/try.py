from tkinter import PhotoImage
import tkinter as tk

color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}

root = tk.Tk()

root.title("Artificial Intelligence")

root.config(bg="gray17")
root.geometry ("400x600+850+50")

btnState = False

#navIcon = PhotoImage(file="menu.png")
#closeIcon = PhotoImage(file="close.png")

topFrame = tk.Frame(root, bg=color["orange"])
topFrame.pack(side="top", fill=tk.X)

homeLabel = tk.Label(topFrame, text="PE", font="Bahnschrift 15", bg=color["orange"], fg="gray17", height=2, padx=20)
homeLabel.pack(side="right")

brandLabel = tk.Label(root, text="Talking \n text", font= "System 30", bg="gray17", fg="green")
brandLabel.place(x=100, y=250)