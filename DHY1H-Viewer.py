import sys

sys.path.append('/home/mahirp/Projects/Heterodimer-Y1H-Analysis/')
from TableDataModel import TableModel

from PySide2.QtWidgets import QApplication, QFileDialog, QMainWindow, QTreeWidgetItem, QGraphicsScene, \
    QGraphicsPixmapItem, QCompleter, QHeaderView, QGraphicsView, QFrame
from PySide2.QtGui import QPixmap, QImage, Qt
from PySide2.QtCore import Signal, QObject, QRectF

from main_ui import Ui_MainWindow
from Experiment import *
from Image import *
import bz2
import pickle
import numpy as np
from PIL import Image
from PIL.ImageQt import ImageQt



class ImageViewer(QGraphicsView):
    ZOOM_IN_FACTOR = 1.25
    ZOOM_OUT_FACTOR = 0.8

    def __init__(self, scene,parent=None):
        super().__init__(parent)
        self.scene = scene
        self.pixmap_item = AssayPixMap()
        self.scene.addItem(self.pixmap_item)
        self.setScene(self.scene)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setFrameShape(QFrame.NoFrame)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setCursor(Qt.CrossCursor)
        self.zoom_flag = False
        self.zoom_times = 0

    def fitInView(self) -> None:
        rect = QRectF(self.pixmap_item.pixmap().rect())
        if not rect.isNull():
            self.setSceneRect(rect)
            unity = self.transform().mapRect(QRectF(0, 0, 1, 1))
            self.scale(1 / unity.width(), 1 / unity.height())
            viewrect = self.viewport().rect()
            scenerect = self.transform().mapRect(rect)
            factor = min(viewrect.width() / scenerect.width(),
                         viewrect.height() / scenerect.height())
            self.scale(factor, factor)

    def wheelEvent(self, event):
        if self.zoom_flag:
            if event.angleDelta().y() > 0:
                factor = 1.25
                self.zoom_times += 1
            else:
                factor = 0.8
                self.zoom_times = max(0, self.zoom_times - 1)
            if self.zoom_times > 0:
                self.scale(factor, factor)

    def mouseMoveEvent(self, event):
        point = event.localPos()
        self.setFocus()
        super().mouseMoveEvent(event)

    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key_Control:
            self.zoom_flag = True
            self.setDragMode(QGraphicsView.ScrollHandDrag)
        super().keyPressEvent(event)

    def keyReleaseEvent(self, event) -> None:
        if event.key() == Qt.Key_Control:
            self.zoom_flag = False
            self.setDragMode(QGraphicsView.NoDrag)
        super().keyReleaseEvent(event)

    def draw_frame(self,pixmap,imageObj):
        self.pixmap_item.draw_frame(pixmap,imageObj)
        self.update()


class QuadDetails:
    def __init__(self,coords,tf1,tf2,intensity,area) -> None:
        self.coords=coords
        self.tf1=tf1
        self.tf2=tf2
        self.intensity=intensity
        self.area=area

class AssayGraphicsScene(QGraphicsScene):
    quadDetails=Signal(QuadDetails)
    drawRect=Signal(str)
    def __init__(self) -> None:
        super().__init__()
        self.quad_highlight=None
        self.pixmapitem=None
        # self.drawRect.connect()

    # def addItem(self,item,pixmapitem=True):
    #     self.pixmapitem=item if pixmapitem else self.pixmapitem
    #     QGraphicsScene.addItem(self,item)
        

class AssayPixMap(QGraphicsPixmapItem):
    def __init__(self) -> None:
        super().__init__()
        self.assayImage = None
        self.last_quad = None
        self.zoom_flag=False
    
    def mousePressEvent(self,event):
        if self.assayImage is not None and not self.zoom_flag:
            quad=self.assayImage.get_coordinate(event.pos().x(),event.pos().y())
            if quad!=self.last_quad:
                self.last_quad=quad
                self.scene().quadDetails.emit(QuadDetails(quad,*self.assayImage.getDetails(quad)))
        super().mouseMoveEvent(event)

    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key_Control:
            self.zoom_flag = True
        super().keyPressEvent(event)

    def keyReleaseEvent(self, event) -> None:
        if event.key() == Qt.Key_Control:
            self.zoom_flag = False
        super().keyReleaseEvent(event)

    def draw_frame(self, pixmap,imageObj:Image) -> None:
        self.assayImage = imageObj
        self.setPixmap(pixmap)

class DHY1H_Viewer(QMainWindow):
    def __init__(self):
        super(DHY1H_Viewer, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave.triggered.connect(self.save_file)
        self.experiment=None
        self.fileName=None
        self.scene = AssayGraphicsScene()
        self.ui.imageView = ImageViewer(self.scene)
        self.scene.quadDetails.connect(self.setDetails)
        self.ui.imageContainer.addWidget(self.ui.imageView)
        self.currentImage=None
        self.imageObj=None
        self.ui.resetButton.clicked.connect(self.reset_image)
        self.image_filtered=False
        self.ui.filterButton.clicked.connect(self.filter_image)
        self.tf1List=[]
        self.tf2List=[]
        self.models=[]
        self.current_item=None
        self.ui.showSegmentation.stateChanged.connect(lambda state: self.load_image(self.current_item))
        self.ui.resetView.clicked.connect(lambda event:self.ui.imageView.fitInView())
        self.initialized=False

    def save_file(self):
        if self.initialized:
            for model,img in zip(self.models,self.experiment.images):
                img.display_dataframe.update(model.dataframe)
            pickle.dump(self.experiment,bz2.BZ2File(self.fileName,'wb'))

    def setDetails(self,quad:QuadDetails):
        self.ui.coords.setText(f'<html><head/><body><p><span style=" font-size:12pt; font-weight:600;">{quad.coords}</span></p></body></html>')
        self.ui.tf1.setText('<html><head/><body><p><span style=" font-size:14pt; font-weight:600;">{}</span></p></body></html>'.format(quad.tf1))
        self.ui.tf2.setText('<html><head/><body><p><span style=" font-size:14pt; font-weight:600;">{}</span></p></body></html>'.format(quad.tf2))
        self.ui.intensity.setText('<html><head/><body><p><span style=" font-size:14pt; font-weight:600;">{}</span></p></body></html>'.format(str(quad.intensity)))
        self.ui.area.setText('<html><head/><body><p><span style=" font-size:14pt; font-weight:600;">{}</span></p></body></html>'.format(str(quad.area)))
        if not self.image_filtered:
            self.currentImage.putalpha(128)
            img=np.array(self.currentImage)
            index, colonies = self.imageObj.getIndex(quad.coords)
            img[index[1][0]:index[1][1],index[0][0]:index[0][1]][:,:,-1]=255
            self.currentImage=Image.fromarray(img)
            self.set_image()
        
    def open_file(self):
        fileName = QFileDialog.getOpenFileName(self,"Open DHY1H File", None, "DHY1H (*.dhy1h)")[0]
        if fileName:
            self.fileName=fileName
            self.experiment=pickle.load(bz2.BZ2File(self.fileName,'rb'))
            self.load_data()
            self.initialized=True
            self.ui.actionOpen.setEnabled(False)
    
    def load_data(self):
        items=([QTreeWidgetItem(self.ui.treeWidget,[i.name]) for i in self.experiment.images if not i.exception_occured])
        self.models=[TableModel(imageObj) for imageObj in self.experiment.images if not imageObj.exception_occured ]
        for i in items:
            self.ui.treeWidget.addTopLevelItem(i)
        self.ui.treeWidget.itemDoubleClicked.connect(self.load_image)

    def load_image(self,item):
        if item is None:
            return
        for index,imageObj in enumerate(self.experiment.images):
            if imageObj.name==item.text(0):
                self.current_item = item
                self.ui.tableView.setModel(self.models[index])
                self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                self.ui.tableView.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                # display_image=Image.fromarray(imageObj.image.copy())
                # display_image.putalpha(255)
                # # self.pixMap=QPixmap.fromImage(QImage(display_image, display_image.shape[1], display_image.shape[0],display_image.shape[1]*3,QImage.Format_RGB888))
                # self.pixMap=QPixmap.fromImage(ImageQt(display_image))
                self.tf1List=imageObj.dataframe['TF1'].unique().tolist()
                self.tf2List=imageObj.dataframe['TF2'].unique().tolist()
                self.ui.tf1_filter.setCompleter(QCompleter(self.tf1List))
                self.ui.tf2_filter.setCompleter(QCompleter(self.tf2List))
                if self.ui.showSegmentation.isChecked():
                    image=Image.fromarray(imageObj.intensity_map).convert('RGBA')
                else:
                    image=Image.fromarray(imageObj.export_grid_image())
                image.putalpha(255)
                # self.gridPixMap= QPixmap.fromImage(QImage(gridimage, gridimage.shape[1], gridimage.shape[0],gridimage.shape[1]*3,QImage.Format_RGB888))
                self.currentImage=image
                self.imageObj=imageObj
                self.set_image()

    def reset_image(self):
        if self.currentImage:
            self.currentImage.putalpha(255)
            self.image_filtered=False
            self.set_image()

    def filter_image(self):
        tf1_filter=self.ui.tf1_filter.text()
        tf2_filter=self.ui.tf2_filter.text()
        if tf1_filter in self.tf1List or tf2_filter in self.tf2List:
            self.image_filtered=True
            df=self.imageObj.dataframe
            if tf1_filter:
                df=df[df['TF1']==tf1_filter]
            if tf2_filter:
                df=df[df['TF2']==tf2_filter]
            self.currentImage.putalpha(128)
            img=np.array(self.currentImage)
            for coords in df['Coordinate']:
                index, colonies = self.imageObj.getIndex(coords)
                img[index[1][0]:index[1][1],index[0][0]:index[0][1]][:,:,-1]=255
            self.currentImage=Image.fromarray(img)
            self.set_image()
        
    def set_image(self):
        pixmap=QPixmap.fromImage(ImageQt(self.currentImage))
        self.ui.imageView.draw_frame(pixmap,self.imageObj)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = DHY1H_Viewer()
    window.show()

    sys.exit(app.exec_())
