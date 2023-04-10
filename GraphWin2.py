import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class GraphWin2():
    def __init__(self, frame):
        self.fig = plt.figure(linewidth=3, edgecolor='black')
        self.ax = plt.subplot()
        self.xpoints = np.array([])
        self.ypoints3 = np.array([])
        self.ypoints4 = np.array([])
        self.ypoints5 = np.array([])
        self.line3, = self.ax.plot(
            self.xpoints, self.ypoints3, color="orange", label="Mutation Constant")
        self.line4, = self.ax.plot(
            self.xpoints, self.ypoints4, color="green", label="Speed")
        self.line5, = self.ax.plot(
            self.xpoints, self.ypoints5, color="purple", label="Maximum sprites")
        self.ax.legend(loc="upper left")

        self.canvasGraph = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvasGraph.draw()
        self.canvasGraph.get_tk_widget().grid(row=0, column=0, padx=50)

    def update(self, xpoint, ypoint3, ypoint4, ypoint5):
        self.ypoints5 = np.append(self.ypoints5, ypoint5)
        self.ypoints4 = np.append(self.ypoints4, ypoint4)
        self.ypoints3 = np.append(self.ypoints3, ypoint3)
        self.xpoints = np.append(self.xpoints, xpoint)
        
        sample_size = 1000  # Change this to adjust the level of downsampling
        if len(self.xpoints) > sample_size:
            indices = np.arange(0, len(self.xpoints), sample_size)
            self.ypoints3 = self.ypoints3[indices]
            self.ypoints4 = self.ypoints4[indices]
            self.ypoints5 = self.ypoints5[indices]
            
        self.line3.set_data(self.xpoints, self.ypoints3)
        self.line4.set_data(self.xpoints, self.ypoints4)
        self.line5.set_data(self.xpoints, self.ypoints5)
        self.ax.relim()
        self.ax.autoscale_view()
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
