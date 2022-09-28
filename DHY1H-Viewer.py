import sys
from PySide2.QtUiTools import QUiLoader

from PlotCanvas import render_heatmap

sys.path.append('/home/mahirp/Projects/Heterodimer-Y1H-Analysis/')
from TableDataModel import TableModel

from PySide2.QtWidgets import QApplication, QFileDialog, QMainWindow, QTreeWidgetItem, QGraphicsScene, \
    QGraphicsPixmapItem, QCompleter, QHeaderView, QGraphicsView, QFrame, QDialog, QLabel, QHBoxLayout, QMessageBox, \
    QCheckBox
from PySide2.QtGui import QPixmap, Qt, QMovie
from PySide2.QtCore import Signal, QRectF, QThread

from main_ui import Ui_MainWindow
from Image import *
import bz2
import pickle
import numpy as np
from PIL import Image
from PIL.ImageQt import ImageQt
from coordinate_dialog import Ui_CoordinateDialog


class ImageViewer(QGraphicsView):
    ZOOM_IN_FACTOR = 1.25
    ZOOM_OUT_FACTOR = 0.8

    def __init__(self, scene, parent=None):
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

    def draw_frame(self, pixmap, imageObj):
        self.pixmap_item.draw_frame(pixmap, imageObj)
        self.update()


class QuadDetails:
    def __init__(self, coords, tf1, tf2, intensity, area) -> None:
        self.coords = coords
        self.tf1 = tf1
        self.tf2 = tf2
        self.intensity = intensity
        self.area = area


class AssayGraphicsScene(QGraphicsScene):
    quadDetails = Signal(QuadDetails)
    drawRect = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self.quad_highlight = None
        self.pixmapitem = None


class AssayPixMap(QGraphicsPixmapItem):
    def __init__(self) -> None:
        super().__init__()
        self.assayImage = None
        self.last_quad = None
        self.zoom_flag = False

    def mousePressEvent(self, event):
        if self.assayImage is not None and not self.zoom_flag:
            quad = self.assayImage.get_coordinate(event.pos().x(), event.pos().y())
            if quad != self.last_quad:
                self.last_quad = quad
                self.scene().quadDetails.emit(QuadDetails(quad, *self.assayImage.getDetails(quad)))
        super().mouseMoveEvent(event)

    def keyPressEvent(self, event) -> None:
        if event.key() == Qt.Key_Control:
            self.zoom_flag = True
        super().keyPressEvent(event)

    def keyReleaseEvent(self, event) -> None:
        if event.key() == Qt.Key_Control:
            self.zoom_flag = False
        super().keyReleaseEvent(event)

    def draw_frame(self, pixmap, imageObj: Image) -> None:
        self.assayImage = imageObj
        self.setPixmap(pixmap)


class FileLoader(QThread):
    file_read = Signal()

    def __init__(self, path):
        super(FileLoader, self).__init__()
        self.path = path
        self.experiment = None

    def run(self):
        self.experiment = pickle.load(bz2.BZ2File(self.path, 'rb'))
        self.file_read.emit()


class DHY1H_Viewer(QMainWindow):
    def __init__(self):
        super(DHY1H_Viewer, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionExport.triggered.connect(self.export_excel)
        self.experiment = None
        self.fileName = None
        self.scene = AssayGraphicsScene()
        self.ui.imageView = ImageViewer(self.scene)
        self.scene.quadDetails.connect(self.setDetails)
        self.ui.imageContainer.addWidget(self.ui.imageView)
        self.currentImage = None
        self.imageObj = None
        self.ui.resetButton.clicked.connect(self.reset_image)
        self.image_filtered = False
        self.ui.filterButton.clicked.connect(self.filter_image)
        self.tf1List = []
        self.tf2List = []
        self.models = []
        self.current_item = None
        self.ui.showSegmentation.stateChanged.connect(lambda state: self.load_image(self.current_item))
        self.ui.resetView.clicked.connect(lambda event: self.ui.imageView.fitInView())
        self.initialized = False
        self.dialog = QDialog(self)
        self.dialog.setModal(True)
        self.dialog.setFixedSize(256, 256)
        self.dialog.setWindowFlag(Qt.FramelessWindowHint)
        self.dialog.setAttribute(Qt.WA_TranslucentBackground)
        _loading_icon = QMovie('./resources/loading.gif')
        label = QLabel()
        label.setMovie(_loading_icon)
        label.setFixedSize(200, 200)
        label.setScaledContents(True)
        _loading_icon.start()
        vbox = QHBoxLayout()
        vbox.addWidget(label)
        self.dialog.setLayout(vbox)
        self.file_loader_thread = None
        self.ui.actionRegenerate_Table.triggered.connect(self.regenerate_current_table)
        self.ui.actionNormalize.triggered.connect(self.normalize_data)
        self.loader = QUiLoader()
        self.file_selection=[]
        self.ui.generate_plot.clicked.connect(self.generate_plot)
        self.plots={}
        self.ui.save_plot.clicked.connect(self.save_plots)
        self.ui.actionReset_Normalization.triggered.connect(self.reset_normalization)

    def export_excel(self):
        if self.experiment is not None:
            export_folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
            if export_folder:
                for image in self.experiment.images:
                    if not image.exception_occurred:
                        image.display_dataframe.to_csv(os.path.join(export_folder,(image.name.split('.')[0])+'.csv'),index=False)


    def reset_normalization(self):
        imgs = [img for img in self.experiment.images if not img.exception_occurred]
        for image, model in zip(imgs, self.models):
            image.dataframe.update(image.raw_dataframe)
            image.generate_evaluation_table(image.reference_coords)
            model.set_dataframe(image)


    def save_plots(self,event=None):
        for plot in self.plots:
            self.plots[plot].save_figure(plot)

    def generate_plot(self,event=None):
        if not len(self.file_selection):
            return
        target_files =[btn.text() for btn in self.file_selection if btn.isChecked()]
        self.plots.clear()
        while not self.ui.plot_container.layout().isEmpty():
            item = self.ui.plot_container.layout().takeAt(0)
        for target in target_files:
            canvas = render_heatmap(*self.experiment.generate_heatmap([target]))
            self.plots[target]=canvas
            self.ui.plot_container.layout().addWidget(canvas)

    def normalize_data(self):
        dialog = self.loader.load('./resources/normalization_dialog.ui', self)

        def normalize():
            self.experiment.normalize_data(normalization_type="Z-Score" if dialog.zscore.isChecked() else "Percent",
                                           ignore_zero_values=dialog.zeros.isChecked())
            dialog.close()
            imgs = [img for img in self.experiment.images if not img.exception_occurred]
            for image,model in zip(imgs,self.models):
                model.set_dataframe(image)

        dialog.buttonBox.accepted.connect(normalize)
        dialog.buttonBox.rejected.connect(lambda: dialog.close())
        dialog.open()

    def regenerate_current_table(self):
        if self.imageObj is None:
            return
        coordinates = self.imageObj.dataframe['Coordinate'].unique().tolist()
        dialog = self.loader.load('./resources/coordinate_dialog.ui', self)
        dialog.coordinate_entry.setCompleter(QCompleter(coordinates))

        def load_coordinate(event):
            coords = dialog.coordinate_entry.text()
            if coords not in coordinates:
                self.warning_dialog(dialog, 'Coordinate not found!')
                return
            info = self.imageObj.getDetails(coords)
            img = self.ui.tableView.model().image_buf[coords]
            dialog.tf1_label.setText(info[0])
            dialog.tf2_label.setText(info[1])
            dialog.intensity_label.setText(str(info[2]))
            dialog.area_label.setText(str(info[3]))
            dialog.image_label.setPixmap(img)
            dialog.confirm.setEnabled(True)

        dialog.load_coordinates.clicked.connect(load_coordinate)
        dialog.confirm.clicked.connect(lambda: dialog.close())
        dialog.exec()
        self.imageObj.generate_evaluation_table(dialog.coordinate_entry.text())
        self.ui.tableView.model().set_dataframe(self.imageObj)
        dialog.destroy()

    def warning_dialog(self, parent, text):
        dlg = QMessageBox(parent)
        dlg.setWindowTitle("Warning!")
        dlg.setText(text)
        return dlg.exec_()

    def save_file(self):
        if self.initialized:
            for model, img in zip(self.models, self.experiment.images):
                img.display_dataframe.update(model.dataframe)
            pickle.dump(self.experiment, bz2.BZ2File(self.fileName, 'wb'))

    def setDetails(self, quad: QuadDetails):
        self.ui.coords.setText(
            f'<html><head/><body><p><span style=" font-size:12pt; font-weight:600;">{quad.coords}</span></p></body></html>')
        self.ui.tf1.setText(
            '<html><head/><body><p><span style=" font-size:14pt; font-weight:600;">{}</span></p></body></html>'.format(
                quad.tf1))
        self.ui.tf2.setText(
            '<html><head/><body><p><span style=" font-size:14pt; font-weight:600;">{}</span></p></body></html>'.format(
                quad.tf2))
        self.ui.intensity.setText(
            '<html><head/><body><p><span style=" font-size:14pt; font-weight:600;">{}</span></p></body></html>'.format(
                str(quad.intensity)))
        self.ui.area.setText(
            '<html><head/><body><p><span style=" font-size:14pt; font-weight:600;">{}</span></p></body></html>'.format(
                str(quad.area)))
        if not self.image_filtered:
            self.currentImage.putalpha(128)
            img = np.array(self.currentImage)
            index, colonies = self.imageObj.getIndex(quad.coords)
            img[index[1][0]:index[1][1], index[0][0]:index[0][1]][:, :, -1] = 255
            self.currentImage = Image.fromarray(img)
            self.set_image()

    def open_file(self):
        fileName = QFileDialog.getOpenFileName(self, "Open DHY1H File", None, "DHY1H (*.dhy1h)")[0]
        if fileName:
            self.fileName = fileName
            self.dialog.open()
            self.file_loader_thread = FileLoader(self.fileName)
            self.file_loader_thread.file_read.connect(self.load_data)
            self.file_loader_thread.start()

    def update_data(self, row, val):
        self.imageObj.display_dataframe.iloc[row, 0] = val

    def load_data(self, event=None):
        try:
            self.experiment = self.file_loader_thread.experiment
            self.models=[]
            for image in self.experiment.images:
                if image.exception_occurred:
                    continue
                self.ui.treeWidget.addTopLevelItem(QTreeWidgetItem(self.ui.treeWidget, [image.name]))
                model = TableModel(image)
                model.data_update.connect(self.update_data)
                self.models.append(model)
                self.file_selection.append(QCheckBox(image.name))
                self.file_selection[-1].setChecked(True)
                self.ui.file_list.addWidget(self.file_selection[-1])
            self.ui.treeWidget.itemDoubleClicked.connect(self.load_image)
            self.initialized = True
            self.ui.actionOpen.setEnabled(False)
        except Exception as ex:
            print(ex)
        finally:
            self.dialog.done(1)

    def load_image(self, item):
        if item is None:
            return
        for index, imageObj in enumerate(self.experiment.images):
            if imageObj.name == item.text(0):
                self.current_item = item
                self.ui.tableView.setModel(self.models[index])
                self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                self.ui.tableView.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
                self.ui.tableView.verticalHeader().setDefaultSectionSize(TableModel.IMAGE_WIDTH)
                for column in [6, 9, 12, 15]:
                    self.ui.tableView.setColumnWidth(column, TableModel.IMAGE_WIDTH)
                # display_image=Image.fromarray(imageObj.image.copy())
                # display_image.putalpha(255)
                # # self.pixMap=QPixmap.fromImage(QImage(display_image, display_image.shape[1], display_image.shape[0],display_image.shape[1]*3,QImage.Format_RGB888))
                # self.pixMap=QPixmap.fromImage(ImageQt(display_image))
                self.tf1List = imageObj.dataframe['TF1'].unique().tolist()
                self.tf2List = imageObj.dataframe['TF2'].unique().tolist()
                self.ui.tf1_filter.setCompleter(QCompleter(self.tf1List))
                self.ui.tf2_filter.setCompleter(QCompleter(self.tf2List))
                if self.ui.showSegmentation.isChecked():
                    image = Image.fromarray(imageObj.intensity_map).convert('RGBA')
                else:
                    image = Image.fromarray(imageObj.export_grid_image())
                image.putalpha(255)
                # self.gridPixMap= QPixmap.fromImage(QImage(gridimage, gridimage.shape[1], gridimage.shape[0],gridimage.shape[1]*3,QImage.Format_RGB888))
                self.currentImage = image
                self.imageObj = imageObj
                self.set_image()

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        for column in [6, 9, 12, 15]:
            self.ui.tableView.setColumnWidth(column, TableModel.IMAGE_WIDTH)

    def reset_image(self):
        if self.currentImage:
            self.currentImage.putalpha(255)
            self.image_filtered = False
            self.set_image()

    def filter_image(self):
        tf1_filter = self.ui.tf1_filter.text()
        tf2_filter = self.ui.tf2_filter.text()
        if tf1_filter in self.tf1List or tf2_filter in self.tf2List:
            self.image_filtered = True
            df = self.imageObj.dataframe
            if tf1_filter:
                df = df[df['TF1'] == tf1_filter]
            if tf2_filter:
                df = df[df['TF2'] == tf2_filter]
            self.currentImage.putalpha(128)
            img = np.array(self.currentImage)
            for coords in df['Coordinate']:
                index, colonies = self.imageObj.getIndex(coords)
                img[index[1][0]:index[1][1], index[0][0]:index[0][1]][:, :, -1] = 255
            self.currentImage = Image.fromarray(img)
            self.set_image()

    def set_image(self):
        pixmap = QPixmap.fromImage(ImageQt(self.currentImage))
        self.ui.imageView.draw_frame(pixmap, self.imageObj)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = DHY1H_Viewer()
    window.show()

    sys.exit(app.exec_())
