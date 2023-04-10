import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class GraphWin1():
    def __init__(self, frame):
        self.fig = plt.figure(linewidth=3, edgecolor='black')
        self.ax = plt.subplot()
        self.xpoints = np.array([])
        self.ypoints1 = np.array([])
        self.ypoints2 = np.array([])
        self.line1, = self.ax.plot(
            self.xpoints, self.ypoints1, color="blue", label="Average Maturing Speed")
        self.line2, = self.ax.plot(
            self.xpoints, self.ypoints2, color="red", label="Reproduction rate")
        self.ax.legend(loc="upper left")

        self.canvasGraph = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvasGraph.draw()
        self.canvasGraph.get_tk_widget().grid(row=0, column=0, padx=50)

    def update(self, xpoint, ypoint1, ypoint2):
        self.ypoints2 = np.append(self.ypoints2, ypoint2)
        self.ypoints1 = np.append(self.ypoints1, ypoint1)
        self.xpoints = np.append(self.xpoints, xpoint)
        
        sample_size = 1000  # Change this to adjust the level of downsampling
        if len(self.xpoints) > sample_size:
            indices = np.arange(0, len(self.xpoints), sample_size)
            self.xpoints = self.xpoints[indices]
            self.ypoints1 = self.ypoints1[indices]
            self.ypoints2 = self.ypoints2[indices]         
            
        self.line1.set_data(self.xpoints, self.ypoints1)
        self.line2.set_data(self.xpoints, self.ypoints2)
        self.ax.relim()
        self.ax.autoscale_view()
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
