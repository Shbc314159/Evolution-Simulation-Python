import globalvars
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class PieChartWin():
    def __init__(self, frame):
        self.fig = plt.figure(linewidth=3, edgecolor='black')
        self.ax = plt.subplot()
        self.fig.set_size_inches(6.4, 4)
        self.slices = [len(globalvars.plants), len(globalvars.amoebas)]
        self.labels = ["Number of Plants", "Number of Amoebas"]
        self.colors = ["green", "red"]
        self.ax.pie(self.slices, colors=self.colors, shadow=True)
        self.ax.legend(labels=self.labels, loc="upper left")
        self.chart = FigureCanvasTkAgg(self.fig, master=frame)
        self.chart.draw()
        self.chart.get_tk_widget().pack()

    def update(self):
        self.slices = [len(globalvars.plants), len(globalvars.amoebas)]
        self.ax.pie(self.slices, colors=self.colors, shadow=True)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
