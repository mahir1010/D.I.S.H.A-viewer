# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rowDMIwYU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1340, 142)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.isSelected = QCheckBox(Form)
        self.isSelected.setObjectName(u"isSelected")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.isSelected.sizePolicy().hasHeightForWidth())
        self.isSelected.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.isSelected)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.tf1tf2 = QGraphicsView(Form)
        self.tf1tf2.setObjectName(u"tf1tf2")
        self.tf1tf2.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tf1tf2.sizePolicy().hasHeightForWidth())
        self.tf1tf2.setSizePolicy(sizePolicy2)
        self.tf1tf2.setMinimumSize(QSize(128, 128))
        self.tf1tf2.setMaximumSize(QSize(128, 128))

        self.horizontalLayout.addWidget(self.tf1tf2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_7)

        self.tf1E = QGraphicsView(Form)
        self.tf1E.setObjectName(u"tf1E")
        sizePolicy2.setHeightForWidth(self.tf1E.sizePolicy().hasHeightForWidth())
        self.tf1E.setSizePolicy(sizePolicy2)
        self.tf1E.setMinimumSize(QSize(128, 128))
        self.tf1E.setMaximumSize(QSize(128, 128))

        self.horizontalLayout.addWidget(self.tf1E, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_8)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_9)

        self.tf2E = QGraphicsView(Form)
        self.tf2E.setObjectName(u"tf2E")
        sizePolicy2.setHeightForWidth(self.tf2E.sizePolicy().hasHeightForWidth())
        self.tf2E.setSizePolicy(sizePolicy2)
        self.tf2E.setMaximumSize(QSize(128, 128))

        self.horizontalLayout.addWidget(self.tf2E)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_10)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_11)

        self.ee = QGraphicsView(Form)
        self.ee.setObjectName(u"ee")
        sizePolicy2.setHeightForWidth(self.ee.sizePolicy().hasHeightForWidth())
        self.ee.setSizePolicy(sizePolicy2)
        self.ee.setMinimumSize(QSize(128, 128))
        self.ee.setMaximumSize(QSize(128, 128))

        self.horizontalLayout.addWidget(self.ee, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 1)
        self.horizontalLayout.setStretch(5, 1)
        self.horizontalLayout.setStretch(6, 2)
        self.horizontalLayout.setStretch(7, 1)
        self.horizontalLayout.setStretch(8, 1)
        self.horizontalLayout.setStretch(9, 2)
        self.horizontalLayout.setStretch(10, 1)
        self.horizontalLayout.setStretch(11, 1)
        self.horizontalLayout.setStretch(12, 2)
        self.horizontalLayout.setStretch(13, 1)
        self.horizontalLayout.setStretch(14, 1)
        self.horizontalLayout.setStretch(15, 2)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.isSelected.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

