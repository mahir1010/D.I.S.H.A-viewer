from PySide2.QtCore import QAbstractTableModel,Qt,QSize
from PySide2.QtGui import QPixmap
from Image import Image
from pathlib import Path
import numpy as np
from PIL import Image as PIL_Image
from PIL.ImageQt import ImageQt

class TableModel(QAbstractTableModel):
    columns=['Activated','Coordinate','TF1','TF2','Intensity','Area','Image',
                         'tf1empty_intensity','tf1empty_area','tf1empty_image',
                         'tf2empty_intensity','tf2empty_area','tf2empty_image',
                         'empty_empty_intensity','empty_empty_area','empty_empty_image']
    column_names=['Selected','Coordinate','TF1','TF2','Intensity','Area','Image',
                         'TF1-Empty\nIntensity','TF1-Empty\nArea','TF1-Empty\nImage',
                         'TF2-Empty\nIntensity','TF2-Empty\nArea','TF2-Empty\nImage',
                         'Empty-Empty\nIntensity','Empty-Empty\nArea','Empty-Empty\nImage']                  
    def __init__(self, image:Image):
        super().__init__()
        self.dataframe = image.display_dataframe[self.columns]
        self.image=image



    def rowCount(self, parent=None):
        return len(self.dataframe.values)

    def columnCount(self, parent=None):
        return len(self.columns)

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            row = index.row()
            if 0 <= row < self.rowCount():
                # print(role,index.row(),index.column())
                if role == Qt.DisplayRole and index.column() in [1,2,3,4,5,7,8,10,11,13,14]:
                    return str(self.dataframe.iloc[index.row()][index.column()])
                if role == Qt.CheckStateRole and index.column() == 0 :
                    return Qt.Checked if self.dataframe.iloc[index.row()][0] else Qt.Unchecked
                if role == Qt.DecorationRole and index.column() in [6,9,12,15]:
                    coords=self.dataframe.iloc[index.row()][index.column()]
                    index, colonies = self.image.getIndex(coords)
                    roi = (np.array(self.image.image)[index[1][0]:index[1][1],index[0][0]:index[0][1]])
                    return QPixmap.fromImage(ImageQt(PIL_Image.fromarray(roi)))
                if role == Qt.SizeHintRole:
                    if index.column() in [6,9,12,15]:
                        return QSize(150,150)
                    else:
                        return QSize(50,150)
                if role == Qt.TextAlignmentRole:
                    return int(Qt.AlignHCenter | Qt.AlignVCenter)
                    

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid():
            return False
        if role == Qt.CheckStateRole and index.column()==0:
            self.dataframe.iloc[index.row(),0]= value>0
            return True
        return False

    def flags(self, index):
        fl = QAbstractTableModel.flags(self, index)
        if index.column() == 0:
            fl |= Qt.ItemIsEditable | Qt.ItemIsUserCheckable
        return fl
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.column_names[section]
        # if orientation == Qt.Horizontal and role == Qt.SizeHintRole:
        #     if section in [6,9,12,15]:
        #         return QSize(200,50)
        #     elif section==0:
        #         return QSize(20,20)
        #     else:
        #         return QSize(50,50)

        return super().headerData(section, orientation, role)