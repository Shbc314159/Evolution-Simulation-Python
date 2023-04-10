from tkinter import ttk, Tk

window = Tk()
style = ttk.Style()
style.configure("TScale", background="#ffffff")
scale = ttk.Scale(window, from_=0, to=100, value=0,
                  orient="vertical", style="TScale")
scale.pack()

window.mainloop()
