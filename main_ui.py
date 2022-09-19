# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainkqcEFX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.5
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(600, 600))
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionRegenerate_Table = QAction(MainWindow)
        self.actionRegenerate_Table.setObjectName(u"actionRegenerate_Table")
        self.actionNormalize = QAction(MainWindow)
        self.actionNormalize.setObjectName(u"actionNormalize")
        self.actionReset_Normalization = QAction(MainWindow)
        self.actionReset_Normalization.setObjectName(u"actionReset_Normalization")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(400, 400))
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.treeWidget = QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout.addWidget(self.treeWidget)

        self.coords = QLabel(self.centralwidget)
        self.coords.setObjectName(u"coords")
        self.coords.setMaximumSize(QSize(300, 16777215))
        self.coords.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.coords)

        self.formWidget = QWidget(self.centralwidget)
        self.formWidget.setObjectName(u"formWidget")
        self.formWidget.setMaximumSize(QSize(300, 16777215))
        self.gridLayout = QGridLayout(self.formWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 1, 5, 1)
        self.label_4 = QLabel(self.formWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"border:2px #212121 solid;")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_3 = QLabel(self.formWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border:2px #212121 solid;")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.intensity = QLabel(self.formWidget)
        self.intensity.setObjectName(u"intensity")
        self.intensity.setStyleSheet(u"border:2px #212121 solid;")
        self.intensity.setAlignment(Qt.AlignCenter)
        self.intensity.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.intensity, 2, 1, 1, 1)

        self.area = QLabel(self.formWidget)
        self.area.setObjectName(u"area")
        self.area.setStyleSheet(u"border:2px #212121 solid;")
        self.area.setAlignment(Qt.AlignCenter)
        self.area.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.area, 3, 1, 1, 1)

        self.label_5 = QLabel(self.formWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"border:2px #212121 solid;")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label = QLabel(self.formWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border:2px #212121 solid;")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.tf2 = QLabel(self.formWidget)
        self.tf2.setObjectName(u"tf2")
        self.tf2.setStyleSheet(u"border:2px #212121 solid;")
        self.tf2.setAlignment(Qt.AlignCenter)
        self.tf2.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.tf2, 1, 1, 1, 1)

        self.tf1 = QLabel(self.formWidget)
        self.tf1.setObjectName(u"tf1")
        self.tf1.setStyleSheet(u"border:2px #212121 solid;")
        self.tf1.setAlignment(Qt.AlignCenter)
        self.tf1.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.tf1, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout.addWidget(self.formWidget)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout.addItem(self.verticalSpacer)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Table = QWidget()
        self.Table.setObjectName(u"Table")
        sizePolicy.setHeightForWidth(self.Table.sizePolicy().hasHeightForWidth())
        self.Table.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.Table)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.tableView = QTableView(self.Table)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableView.setShowGrid(True)
        self.tableView.setSortingEnabled(False)
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView.horizontalHeader().setMinimumSectionSize(100)
        self.tableView.horizontalHeader().setDefaultSectionSize(200)
        self.tableView.verticalHeader().setMinimumSectionSize(50)
        self.tableView.verticalHeader().setDefaultSectionSize(50)

        self.verticalLayout_4.addWidget(self.tableView)

        self.tabWidget.addTab(self.Table, "")
        self.Image = QWidget()
        self.Image.setObjectName(u"Image")
        self.verticalLayout_3 = QVBoxLayout(self.Image)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tf1_filter = QLineEdit(self.Image)
        self.tf1_filter.setObjectName(u"tf1_filter")
        self.tf1_filter.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.tf1_filter)

        self.tf2_filter = QLineEdit(self.Image)
        self.tf2_filter.setObjectName(u"tf2_filter")
        self.tf2_filter.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.tf2_filter)

        self.filterButton = QPushButton(self.Image)
        self.filterButton.setObjectName(u"filterButton")

        self.horizontalLayout_3.addWidget(self.filterButton)

        self.resetButton = QPushButton(self.Image)
        self.resetButton.setObjectName(u"resetButton")

        self.horizontalLayout_3.addWidget(self.resetButton)

        self.showSegmentation = QCheckBox(self.Image)
        self.showSegmentation.setObjectName(u"showSegmentation")

        self.horizontalLayout_3.addWidget(self.showSegmentation)

        self.resetView = QPushButton(self.Image)
        self.resetView.setObjectName(u"resetView")

        self.horizontalLayout_3.addWidget(self.resetView)

        self.horizontalLayout_3.setStretch(0, 3)
        self.horizontalLayout_3.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.widget = QWidget(self.Image)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.imageContainer = QVBoxLayout()
        self.imageContainer.setObjectName(u"imageContainer")

        self.verticalLayout_5.addLayout(self.imageContainer)


        self.verticalLayout_3.addWidget(self.widget)

        self.verticalLayout_3.setStretch(1, 2)
        self.tabWidget.addTab(self.Image, "")
        self.plots = QWidget()
        self.plots.setObjectName(u"plots")
        self.gridLayout_4 = QGridLayout(self.plots)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_2 = QSpacerItem(4, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 1, 1, 2, 1)

        self.groupBox = QGroupBox(self.plots)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.file_list = QVBoxLayout()
        self.file_list.setObjectName(u"file_list")

        self.verticalLayout_6.addLayout(self.file_list)


        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.generate_plot = QPushButton(self.plots)
        self.generate_plot.setObjectName(u"generate_plot")

        self.horizontalLayout_2.addWidget(self.generate_plot)

        self.save_plot = QPushButton(self.plots)
        self.save_plot.setObjectName(u"save_plot")

        self.horizontalLayout_2.addWidget(self.save_plot)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.scrollArea = QScrollArea(self.plots)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMinimumSize(QSize(600, 600))
        self.scrollArea.setWidgetResizable(True)
        self.plot_container = QWidget()
        self.plot_container.setObjectName(u"plot_container")
        self.plot_container.setGeometry(QRect(0, 0, 596, 596))
        self.verticalLayout_7 = QVBoxLayout(self.plot_container)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea.setWidget(self.plot_container)

        self.gridLayout_4.addWidget(self.scrollArea, 1, 2, 2, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(2, 2)
        self.gridLayout_4.setColumnMinimumWidth(2, 600)
        self.tabWidget.addTab(self.plots, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 4)

        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuTools.addAction(self.actionRegenerate_Table)
        self.menuTools.addAction(self.actionNormalize)
        self.menuTools.addAction(self.actionReset_Normalization)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DHY1H Viewer", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionRegenerate_Table.setText(QCoreApplication.translate("MainWindow", u"Regenerate Table", None))
        self.actionNormalize.setText(QCoreApplication.translate("MainWindow", u"Normalize", None))
        self.actionReset_Normalization.setText(QCoreApplication.translate("MainWindow", u"Reset Normalization", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Experiment", None));
        self.coords.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\"\n"
"                                                font-size:12pt; font-weight:600;\">Details</span></p></body></html>\n"
"                                            ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span\n"
"                                                            style=\" font-size:14pt; font-weight:600;\">TF1</span></p></body></html>\n"
"                                                        ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span\n"
"                                                            style=\" font-size:14pt; font-weight:600;\">Intensity</span></p></body></html>\n"
"                                                        ", None))
        self.intensity.setText("")
        self.area.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span\n"
"                                                            style=\" font-size:14pt; font-weight:600;\">Area</span></p></body></html>\n"
"                                                        ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span\n"
"                                                            style=\" font-size:14pt; font-weight:600;\">TF2</span></p></body></html>\n"
"                                                        ", None))
        self.tf2.setText("")
        self.tf1.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Table), QCoreApplication.translate("MainWindow", u"Table", None))
        self.tf1_filter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TF1", None))
        self.tf2_filter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TF2", None))
        self.filterButton.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.showSegmentation.setText(QCoreApplication.translate("MainWindow", u"Show Segmentation", None))
        self.resetView.setText(QCoreApplication.translate("MainWindow", u"Reset View", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Image), QCoreApplication.translate("MainWindow", u"Image", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Select Files", None))
        self.generate_plot.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.save_plot.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.plots), QCoreApplication.translate("MainWindow", u"Plots", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

