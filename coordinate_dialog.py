# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'coordinate_dialogeyvJKG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_CoordinateDialog(object):
    def setupUi(self, CoordinateDialog):
        if not CoordinateDialog.objectName():
            CoordinateDialog.setObjectName(u"CoordinateDialog")
        CoordinateDialog.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(CoordinateDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.coordinate_entry = QLineEdit(CoordinateDialog)
        self.coordinate_entry.setObjectName(u"coordinate_entry")

        self.horizontalLayout.addWidget(self.coordinate_entry)

        self.load_coordinates = QPushButton(CoordinateDialog)
        self.load_coordinates.setObjectName(u"load_coordinates")

        self.horizontalLayout.addWidget(self.load_coordinates)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tf1_label = QLabel(CoordinateDialog)
        self.tf1_label.setObjectName(u"tf1_label")

        self.gridLayout.addWidget(self.tf1_label, 1, 0, 1, 1)

        self.label_4 = QLabel(CoordinateDialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)

        self.label_3 = QLabel(CoordinateDialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.label = QLabel(CoordinateDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_7 = QLabel(CoordinateDialog)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)

        self.area_label = QLabel(CoordinateDialog)
        self.area_label.setObjectName(u"area_label")

        self.gridLayout.addWidget(self.area_label, 1, 3, 1, 1)

        self.image_label = QLabel(CoordinateDialog)
        self.image_label.setObjectName(u"image_label")

        self.gridLayout.addWidget(self.image_label, 1, 4, 1, 1)

        self.label_8 = QLabel(CoordinateDialog)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)

        self.tf2_label = QLabel(CoordinateDialog)
        self.tf2_label.setObjectName(u"tf2_label")

        self.gridLayout.addWidget(self.tf2_label, 1, 1, 1, 1)

        self.intensity_label = QLabel(CoordinateDialog)
        self.intensity_label.setObjectName(u"intensity_label")

        self.gridLayout.addWidget(self.intensity_label, 1, 2, 1, 1)

        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setColumnMinimumWidth(4, 150)
        self.gridLayout.setRowMinimumHeight(1, 150)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.pushButton_2 = QPushButton(CoordinateDialog)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.verticalLayout_2.setStretch(1, 1)

        self.retranslateUi(CoordinateDialog)

        QMetaObject.connectSlotsByName(CoordinateDialog)
    # setupUi

    def retranslateUi(self, CoordinateDialog):
        CoordinateDialog.setWindowTitle(QCoreApplication.translate("CoordinateDialog", u"Dialog", None))
        self.load_coordinates.setText(QCoreApplication.translate("CoordinateDialog", u"Load Coordinates", None))
        self.tf1_label.setText("")
        self.label_4.setText(QCoreApplication.translate("CoordinateDialog", u"Image", None))
        self.label_3.setText(QCoreApplication.translate("CoordinateDialog", u"Area", None))
        self.label.setText(QCoreApplication.translate("CoordinateDialog", u"TF1", None))
        self.label_7.setText(QCoreApplication.translate("CoordinateDialog", u"TF2", None))
        self.area_label.setText("")
        self.image_label.setText("")
        self.label_8.setText(QCoreApplication.translate("CoordinateDialog", u"Intensity", None))
        self.tf2_label.setText("")
        self.intensity_label.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("CoordinateDialog", u"Confirm", None))
    # retranslateUi

