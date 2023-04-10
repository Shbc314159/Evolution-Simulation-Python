import tkinter as tk
from tkinter import ttk
import globalvars
import pygame
pygame.init()
from PIL import Image, ImageTk
import time
import ctypes
import Amoeba as amoebaclass
import GraphWin1 as graphwin1
import GraphWin2 as graphwin2
import PieChartWin as piechartwin
import PygameWin as pygamewin
from LeftFrameComponents import LeftFrameComponents as leftframecomponents
myappid = u'evogenesis.app'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class Application(tk.Tk):
    def __init__(self, root):
        self.step_counter = 0
        self.total = 0
        self.avg = 0

        self.root = root
        self.root.title("EvoGenesis Simulation")
        self.root.iconbitmap("Icon.ico")
        self.root.geometry("2000x2000")
        self.root.state("zoomed")
        self.root.tk.call("source", "Azure-ttk-theme-main/azure.tcl")
        self.root.tk.call("set_theme", "dark")
        
        self.root.columnconfigure(0)
        self.root.columnconfigure(1,weight=1)
        
        self.leftFrame = ttk.Frame(self.root, height=1200, width=250)
        self.mainFrame = ttk.Frame(self.root, height=1200, width=2000)
        self.pieChartFrame = ttk.Frame(self.mainFrame, height=400, width=800)
        self.leftFrame.grid_propagate(False)
        self.mainFrame.grid_propagate(False)
        self.pieChartFrame.grid_propagate(False)
        
        self.leftFrame.grid(row=1, column=0)
        self.mainFrame.grid(row=1, column=1, sticky="nw")
        self.pieChartFrame.grid(row=2, column= 0, sticky="sw", padx=50)
        
        self.leftFrame.columnconfigure(0, weight=1)
        self.leftFrame.columnconfigure(1, weight=8)
        self.leftFrame.columnconfigure(2, weight=1)
        
        self.mainFrame.rowconfigure(0, pad=25)
        
        self.graph1button = ttk.Button(self.mainFrame, text="Graph 1", command=self.switchGraph1, padding=0)
        self.graph1button.grid(row=1, column=0, pady=(0, 25), padx=100, sticky="nw")
        
        self.graph2button = ttk.Button(self.mainFrame, text="Graph 2", command=self.switchGraph2, padding=0)
        self.graph2button.grid(row=1, column=0, pady=(0, 25), padx=200, sticky="nw")

        self.leftframewidgets = leftframecomponents(self.leftFrame, self.root, self)
        
        self.fpslabel = ttk.Label(self.leftFrame, text="Fps: 0", font=("", 12, "bold"))
        self.fpslabel.grid(row=9, column=1)
        
        self.othergraph = graphwin2.GraphWin2(self.mainFrame)
        self.graph = graphwin1.GraphWin1(self.mainFrame)
        self.pywin = pygamewin.PygameWin(self.mainFrame)
        self.chart = piechartwin.PieChartWin(self.pieChartFrame)
    
    def switchGraph1(self):
        self.othergraph.canvasGraph.get_tk_widget().grid_forget()
        self.graph.canvasGraph.get_tk_widget().grid(
            row=0, column=0, in_=self.mainFrame)

    def switchGraph2(self):
        self.graph.canvasGraph.get_tk_widget().grid_forget()
        self.othergraph.canvasGraph.get_tk_widget().grid(
            row=0, column=0, in_=self.mainFrame)
        
    def update_graphs(self):
        if self.step_counter % globalvars.simspeed == 0:
            self.total = 0
            self.numamoebas = 1
        
            for self.amoeba in globalvars.sprites:
                if isinstance(self.amoeba, amoebaclass.Amoeba):
                    self.total = self.total + self.amoeba.maturing_speed
            
            self.graph.update(self.step_counter, self.total/len(globalvars.amoebas),globalvars.num_collisions)
            self.othergraph.update(self.step_counter, globalvars.mutation_speed, globalvars.speed, globalvars.maxsprites)
            
            self.chart.update()
            
        
    def update_simulation(self):
        self.step_counter += 1
        self.start_time = time.time()
            
        self.pywin.update()
        self.update_graphs()
        
        if self.step_counter % 10 == 0:
            print("Number of plants: ", len(globalvars.plants))
            print("Number of amoebas: ", len(globalvars.amoebas))
            
        self.fps = int(1.0/(time.time()-self.start_time))
        self.fpslabel.config(text=f"FPS: {self.fps}")
        
        globalvars.num_collisions = 0
        
        if globalvars.running:
            root.after(1, self.update_simulation)
    
class LoadingWin:
    def __init__(self, root):
        self.root = root
        self.root.overrideredirect(True)
        self.root.geometry("400x200")
        self.root.configure(bg="black")
        self.root.eval("tk::PlaceWindow . center")
        self.canvas =  tk.Canvas(self.root, bg="black", height=200, width=400, highlightthickness=0)
        self.canvas.pack()
        self.image1 = Image.open("Logo.png")
        self.resizedimage = self.image1.resize((200,200), Image.LANCZOS)
        self.finalimg = ImageTk.PhotoImage(self.resizedimage)
        self.canvas.create_image(200,100, image=self.finalimg)
        self.root.after(200,self.kill)

    def kill(self):
        self.root.destroy()


root = tk.Tk()
loadingwin = LoadingWin(root)
root.mainloop()

root = tk.Tk()
app = Application(root)
app.update_simulation()
root.mainloop()