import pygame
import globalvars
import Plant as plantclass
import random
import Amoeba as amoebaclass
from PIL import Image, ImageTk
import tkinter as tk

class PygameWin():
    def __init__(self, frame):
        self.surface = pygame.Surface(
            (globalvars.screen_width, globalvars.screen_height))
        self.surface.fill((255, 255, 255))
        self.canvas = tk.Canvas(frame, height=globalvars.screen_height, width=globalvars.screen_width,
                                highlightthickness=4, highlightbackground='black', bg='white')

        for i in range(250):
            self.plant = plantclass.Plant(random.randint(
                0, globalvars.screen_width), random.randint(0, globalvars.screen_height))
            globalvars.sprites.add(self.plant)
            globalvars.plants.add(self.plant)

        for i in range(50):
            self.amoeba = amoebaclass.Amoeba(random.randint(25, 50), random.randint(
                0, globalvars.screen_width), random.randint(0, globalvars.screen_height), 500)
            globalvars.sprites.add(self.amoeba)
            globalvars.amoebas.add(self.amoeba)

    def update(self):
        amoebaclass.Amoeba.collide()
        amoebaclass.Amoeba.eat(amoebaclass.Amoeba)
        globalvars.sprites.update()

        self.surface.fill((255, 255, 255))
        globalvars.sprites.draw(self.surface)
        self.img = ImageTk.PhotoImage(Image.frombytes('RGB', (self.surface.get_width(
        ), self.surface.get_height()), pygame.image.tostring(self.surface, 'RGB')))

        self.canvas.create_image(0, 0, anchor="nw", image=self.img)
        self.canvas.grid(row=0, column=1, padx=100, pady=5)
