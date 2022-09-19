from PySide2.QtWidgets import QDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class Canvas(FigureCanvasQTAgg):

    def __init__(self, row=1, column=2, width=20, height=10, dpi=100):
        self.fig_width= width
        self.fig_height = height
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.subplots(nrows=row, ncols=column)
        super(Canvas, self).__init__(self.fig)

    def save_figure(self,name):
        self.fig.set_size_inches(self.fig_width, self.fig_height)
        self.fig.savefig(f'./{name}.png',dpi=100)

def render_heatmap(label_y,label_x, intensity_heatmap, area_heatmap):
    canvas = Canvas(height=len(label_y)//2,width=len(label_x)//2)
    canvas.axes[0].imshow(intensity_heatmap)
    canvas.axes[1].imshow(area_heatmap)
    canvas.axes[0].set_title('Intensity')
    canvas.axes[1].set_title('Area')
    canvas.setMinimumHeight(400)
    for i,ax in enumerate(canvas.axes):
        ax.set_xticks(range(len(label_x)),labels=label_x,rotation=90)
        if i==0:
            ax.set_yticks(range(len(label_y)), labels=label_y)
        else:
            ax.set_yticks([])
    canvas.fig.tight_layout()
    return canvas
