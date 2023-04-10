import Plant as plantclass
import Amoeba as amoebaclass
import subprocess
import random
import pygame
import sys
import tkinter as tk
from tkinter import ttk 
import globalvars
pygame.init()

class LeftFrameComponents():
    def __init__(self, leftFrame, root, parent):
        self.leftFrame = leftFrame
        self.root = root
        self.parent = parent
        
        self.startbutton = self.create_button("Start", self.start, 0, 1, (0, 120), (25,0))
        self.startbutton.config(width=5)
        self.restartbutton = self.create_button("Restart", self.restart, 0, 1, (1, 1), (25,0))
        self.restartbutton.config(width=6)
        self.stopbutton = self.create_button("Stop", self.stop, 0, 1, (120, 0), (25,0))
        self.stopbutton.config(width=5)
        self.addplantsbutton = self.create_button("Add Plants", self.addplants, 12, 1, (0,118), (10, 0))
        self.addamoebasbutton = self.create_button("Add Amoebas", self.addamoebas, 12, 1, (120, 0), (10, 0))
        self.removeplantsbutton = self.create_button("Remove Plants", self.removeplants, 13, 1, (0, 120), (10, 0))
        self.removeamoebasbutton = self.create_button("Remove Amoebas", self.removeamoebas, 13, 1, (120, 0), (10, 0))
                
        self.mutationslider, self.mutationlabel = self.create_slider("Mutation Speed: 100", "Mutation Speed", 1, 1000, 100, 1, "mutation_speed")
        self.speedslider, self.speedlabel = self.create_slider("Amoeba Speed: 3", "Amoeba Speed", 0, 10, 3, 3, "speed")
        self.maxspritesslider, self.maxspriteslabel = self.create_slider("Maximum Organisms: 200", "Maximum Organisms", 0, 1000, 200, 5, "maxsprites")
        self.simspeedslider, self.simspeedlabel = self.create_slider("Simulation Speed: 1", "Simulation Speed", 1, 100, 1, 7, "simspeed")
        self.numslider, self.numlabel = self.create_slider("Add/Remove Organisms: 10", "Add/Remove Organisms", 0, 100, 10, 10, "numtochange")
        self.plantdeathageslider, self.plantdeathagelabel = self.create_slider("Plant Death Age: 50", "Plant Death Age", 1, 100, 50, 14, "plantdeathage")
        self.amoebadeathageslider, self.amoebadeathagelabel = self.create_slider("Amoeba Death Age: 100", "Amoeba Death Age", 1, 500, 100, 16, "amoebadeathage")
        
        
        self.toggle_button_var = tk.BooleanVar()
        self.togglebutton = ttk.Checkbutton(self.leftFrame, text="Light Mode", command=self.togglemode, variable=self.toggle_button_var)
        self.togglebutton.grid(row=18, column=1)
        
    def create_slider(self, labeltextstart, labeltext, min, max, default, row, variable):
        slider = ttk.Scale(self.leftFrame, from_=min, to_=max, orient=tk.HORIZONTAL, length=200, value=default)
        slider.grid(row=row, column=1, pady=(50, 0))
        label = ttk.Label(self.leftFrame, text=labeltextstart, font=("Cascadia", 11, "bold"))
        label.grid(row=(row+1), column=1)
        slider.configure(command= lambda val: setattr(globalvars, variable, self.sliderChanged(slider.get(), labeltext, label)))
        return slider, label

    def create_button(self, text, command, row, column, padx, pady):
        button = ttk.Button(self.leftFrame, text=text, command=command, padding=0)
        button.grid(row=row, column=column, padx=padx, pady=pady)
        return button

    def start(self):
        globalvars.running = True
        self.parent.update_simulation()
        
    def togglemode(self):
            if self.toggle_button_var.get():
                self.root.tk.call("set_theme", "light")
            else:
                self.root.tk.call("set_theme", "dark")

    def stop(self):
        globalvars.running = False

    def restart(self):
        python = sys.executable
        subprocess.call([python, __file__])
        sys.exit()
 
    def sliderChanged(self, sliderval, text, label):
        label.config(text=f"{text}: {int(sliderval)}")
        return int(sliderval)          

    def addplants(self):
        for i in range(globalvars.numtochange):
            self.plant = plantclass.Plant(random.randint(0, globalvars.screen_width), random.randint(0, globalvars.screen_height))
            globalvars.sprites.add(self.plant)
            globalvars.plants.add(self.plant)

    def addamoebas(self):
        for i in range(globalvars.numtochange):
            self.amoeba = amoebaclass.Amoeba(random.randint(0, 255), random.randint(0, globalvars.screen_width), random.randint(0, globalvars.screen_height), 200)
            globalvars.sprites.add(self.amoeba)
            globalvars.amoebas.add(self.amoeba)

    def removeplants(self):
        if len(globalvars.plants) - globalvars.numtochange > globalvars.maxsprites/4:
            i = globalvars.numtochange
            for sprite in globalvars.sprites:
                if isinstance(sprite, plantclass.Plant):
                    globalvars.sprites.remove(sprite)
                    sprite.kill()
                    i -= 1

                if i == 0:
                    break

    def removeamoebas(self):
        if len(globalvars.amoebas) - globalvars.numtochange > globalvars.maxsprites/4:
            i = globalvars.numtochange
            for sprite in globalvars.sprites:
                if isinstance(sprite, amoebaclass.Amoeba):
                    globalvars.sprites.remove(sprite)
                    sprite.kill()
                    i -= 1

                if i == 0:
                    break
