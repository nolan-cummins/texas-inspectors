# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowaGVarX.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFrame,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 632)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1000, 632))
        MainWindow.setMaximumSize(QSize(1000, 632))
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon = QIcon(QIcon.fromTheme(u"document-save"))
        self.actionSave.setIcon(icon)
        self.actionLoad = QAction(MainWindow)
        self.actionLoad.setObjectName(u"actionLoad")
        icon1 = QIcon(QIcon.fromTheme(u"document-open"))
        self.actionLoad.setIcon(icon1)
        self.actionControls = QAction(MainWindow)
        self.actionControls.setObjectName(u"actionControls")
        self.actionControls.setCheckable(True)
        self.actionMask = QAction(MainWindow)
        self.actionMask.setObjectName(u"actionMask")
        self.actionMask.setCheckable(True)
        self.actionMask.setChecked(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 984, 566))
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_16)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_13)

        self.frame = QFrame(self.layoutWidget)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(640, 512))
        self.frame.setMaximumSize(QSize(640, 512))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.display = QLabel(self.frame)
        self.display.setObjectName(u"display")
        self.display.setGeometry(QRect(10, 10, 620, 491))

        self.horizontalLayout_12.addWidget(self.frame)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)


        self.verticalLayout_13.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.identifyButton = QPushButton(self.layoutWidget)
        self.identifyButton.setObjectName(u"identifyButton")
        sizePolicy.setHeightForWidth(self.identifyButton.sizePolicy().hasHeightForWidth())
        self.identifyButton.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        self.identifyButton.setFont(font)

        self.horizontalLayout_10.addWidget(self.identifyButton)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_10.addWidget(self.line)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)

        self.models = QComboBox(self.layoutWidget)
        self.models.addItem("")
        self.models.addItem("")
        self.models.addItem("")
        self.models.addItem("")
        self.models.addItem("")
        self.models.addItem("")
        self.models.addItem("")
        self.models.addItem("")
        self.models.addItem("")
        self.models.addItem("")
        self.models.addItem("")
        self.models.addItem("")
        self.models.addItem("")
        self.models.addItem("")
        self.models.addItem("")
        self.models.setObjectName(u"models")

        self.horizontalLayout_10.addWidget(self.models)

        self.line_2 = QFrame(self.layoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_10.addWidget(self.line_2)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.threshold = QDoubleSpinBox(self.layoutWidget)
        self.threshold.setObjectName(u"threshold")
        self.threshold.setMinimumSize(QSize(90, 0))
        self.threshold.setMaximum(1.000000000000000)
        self.threshold.setValue(0.750000000000000)

        self.horizontalLayout_10.addWidget(self.threshold)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)


        self.verticalLayout_13.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)


        self.horizontalLayout_11.addLayout(self.verticalLayout_13)

        self.controlLayout = QVBoxLayout()
        self.controlLayout.setObjectName(u"controlLayout")
        self.XYZFrame = QFrame(self.layoutWidget)
        self.XYZFrame.setObjectName(u"XYZFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.XYZFrame.sizePolicy().hasHeightForWidth())
        self.XYZFrame.setSizePolicy(sizePolicy1)
        self.XYZFrame.setMinimumSize(QSize(300, 0))
        self.XYZFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.XYZFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.XYZFrame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.XYZFrame)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(19)
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.speedLabel = QLabel(self.XYZFrame)
        self.speedLabel.setObjectName(u"speedLabel")
        self.speedLabel.setMaximumSize(QSize(16777215, 16777215))
        self.speedLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.speedLabel)

        self.speedSlider = QSlider(self.XYZFrame)
        self.speedSlider.setObjectName(u"speedSlider")
        self.speedSlider.setMinimumSize(QSize(150, 0))
        self.speedSlider.setMaximum(100)
        self.speedSlider.setOrientation(Qt.Orientation.Horizontal)
        self.speedSlider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.speedSlider.setTickInterval(10)

        self.horizontalLayout.addWidget(self.speedSlider)

        self.speedBox = QSpinBox(self.XYZFrame)
        self.speedBox.setObjectName(u"speedBox")
        self.speedBox.setMinimumSize(QSize(80, 0))
        self.speedBox.setMaximum(100)

        self.horizontalLayout.addWidget(self.speedBox)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_11)


        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.XYZFrame)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_2.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_2)

        self.label_3 = QLabel(self.XYZFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_3)

        self.label_6 = QLabel(self.XYZFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.verticalLayout_8.addWidget(self.label_6)


        self.horizontalLayout_9.addLayout(self.verticalLayout_8)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.xBox = QDoubleSpinBox(self.XYZFrame)
        self.xBox.setObjectName(u"xBox")
        self.xBox.setMinimumSize(QSize(100, 0))
        self.xBox.setMaximum(100.000000000000000)

        self.verticalLayout_9.addWidget(self.xBox)

        self.yBox = QDoubleSpinBox(self.XYZFrame)
        self.yBox.setObjectName(u"yBox")
        self.yBox.setMinimumSize(QSize(100, 0))
        self.yBox.setMaximum(100.000000000000000)

        self.verticalLayout_9.addWidget(self.yBox)

        self.zBox = QDoubleSpinBox(self.XYZFrame)
        self.zBox.setObjectName(u"zBox")
        self.zBox.setMinimumSize(QSize(100, 0))
        self.zBox.setMaximum(100.000000000000000)

        self.verticalLayout_9.addWidget(self.zBox)


        self.horizontalLayout_8.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.xPosButton = QPushButton(self.XYZFrame)
        self.xPosButton.setObjectName(u"xPosButton")
        font3 = QFont()
        font3.setPointSize(16)
        self.xPosButton.setFont(font3)

        self.horizontalLayout_5.addWidget(self.xPosButton)

        self.xNegButton = QPushButton(self.XYZFrame)
        self.xNegButton.setObjectName(u"xNegButton")
        self.xNegButton.setFont(font3)

        self.horizontalLayout_5.addWidget(self.xNegButton)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.yPosButton = QPushButton(self.XYZFrame)
        self.yPosButton.setObjectName(u"yPosButton")
        self.yPosButton.setFont(font3)

        self.horizontalLayout_6.addWidget(self.yPosButton)

        self.yNegButton = QPushButton(self.XYZFrame)
        self.yNegButton.setObjectName(u"yNegButton")
        self.yNegButton.setFont(font3)

        self.horizontalLayout_6.addWidget(self.yNegButton)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.zPosButton = QPushButton(self.XYZFrame)
        self.zPosButton.setObjectName(u"zPosButton")
        self.zPosButton.setFont(font3)

        self.horizontalLayout_7.addWidget(self.zPosButton)

        self.zNegButton = QPushButton(self.XYZFrame)
        self.zNegButton.setObjectName(u"zNegButton")
        self.zNegButton.setFont(font3)

        self.horizontalLayout_7.addWidget(self.zNegButton)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_8.addLayout(self.verticalLayout_10)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)


        self.controlLayout.addWidget(self.XYZFrame)

        self.pedestalFrame = QFrame(self.layoutWidget)
        self.pedestalFrame.setObjectName(u"pedestalFrame")
        sizePolicy1.setHeightForWidth(self.pedestalFrame.sizePolicy().hasHeightForWidth())
        self.pedestalFrame.setSizePolicy(sizePolicy1)
        self.pedestalFrame.setMinimumSize(QSize(300, 0))
        self.pedestalFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.pedestalFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.pedestalFrame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.pedestalFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pos90Button = QPushButton(self.pedestalFrame)
        self.pos90Button.setObjectName(u"pos90Button")
        sizePolicy.setHeightForWidth(self.pos90Button.sizePolicy().hasHeightForWidth())
        self.pos90Button.setSizePolicy(sizePolicy)
        self.pos90Button.setFont(font3)

        self.verticalLayout_4.addWidget(self.pos90Button)

        self.neg90Button = QPushButton(self.pedestalFrame)
        self.neg90Button.setObjectName(u"neg90Button")
        sizePolicy.setHeightForWidth(self.neg90Button.sizePolicy().hasHeightForWidth())
        self.neg90Button.setSizePolicy(sizePolicy)
        self.neg90Button.setFont(font)

        self.verticalLayout_4.addWidget(self.neg90Button)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pos45Button = QPushButton(self.pedestalFrame)
        self.pos45Button.setObjectName(u"pos45Button")
        sizePolicy.setHeightForWidth(self.pos45Button.sizePolicy().hasHeightForWidth())
        self.pos45Button.setSizePolicy(sizePolicy)
        self.pos45Button.setFont(font3)

        self.verticalLayout_5.addWidget(self.pos45Button)

        self.neg45Button = QPushButton(self.pedestalFrame)
        self.neg45Button.setObjectName(u"neg45Button")
        sizePolicy.setHeightForWidth(self.neg45Button.sizePolicy().hasHeightForWidth())
        self.neg45Button.setSizePolicy(sizePolicy)
        self.neg45Button.setFont(font)

        self.verticalLayout_5.addWidget(self.neg45Button)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.posRotate = QPushButton(self.pedestalFrame)
        self.posRotate.setObjectName(u"posRotate")
        sizePolicy.setHeightForWidth(self.posRotate.sizePolicy().hasHeightForWidth())
        self.posRotate.setSizePolicy(sizePolicy)
        self.posRotate.setFont(font)
        icon2 = QIcon(QIcon.fromTheme(u"view-refresh"))
        self.posRotate.setIcon(icon2)
        self.posRotate.setIconSize(QSize(22, 22))

        self.verticalLayout_6.addWidget(self.posRotate)

        self.negRotateButton = QPushButton(self.pedestalFrame)
        self.negRotateButton.setObjectName(u"negRotateButton")
        sizePolicy.setHeightForWidth(self.negRotateButton.sizePolicy().hasHeightForWidth())
        self.negRotateButton.setSizePolicy(sizePolicy)
        self.negRotateButton.setFont(font)
        icon3 = QIcon(QIcon.fromTheme(u"view-restore"))
        self.negRotateButton.setIcon(icon3)
        self.negRotateButton.setIconSize(QSize(22, 22))

        self.verticalLayout_6.addWidget(self.negRotateButton)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_7.addLayout(self.verticalLayout_3)


        self.controlLayout.addWidget(self.pedestalFrame)

        self.grabberFrame = QFrame(self.layoutWidget)
        self.grabberFrame.setObjectName(u"grabberFrame")
        sizePolicy1.setHeightForWidth(self.grabberFrame.sizePolicy().hasHeightForWidth())
        self.grabberFrame.setSizePolicy(sizePolicy1)
        self.grabberFrame.setMinimumSize(QSize(300, 0))
        self.grabberFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.grabberFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.grabberFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.grabberFrame)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.grabberAngleLabel = QLabel(self.grabberFrame)
        self.grabberAngleLabel.setObjectName(u"grabberAngleLabel")
        self.grabberAngleLabel.setMaximumSize(QSize(16777215, 16777215))
        self.grabberAngleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.grabberAngleLabel)

        self.grabberAngleSlider = QSlider(self.grabberFrame)
        self.grabberAngleSlider.setObjectName(u"grabberAngleSlider")
        self.grabberAngleSlider.setMinimumSize(QSize(150, 0))
        self.grabberAngleSlider.setMinimum(-90)
        self.grabberAngleSlider.setMaximum(90)
        self.grabberAngleSlider.setOrientation(Qt.Orientation.Horizontal)
        self.grabberAngleSlider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.grabberAngleSlider.setTickInterval(10)

        self.horizontalLayout_2.addWidget(self.grabberAngleSlider)

        self.grabberAngleBox = QSpinBox(self.grabberFrame)
        self.grabberAngleBox.setObjectName(u"grabberAngleBox")
        self.grabberAngleBox.setMinimumSize(QSize(80, 0))
        self.grabberAngleBox.setMinimum(-90)
        self.grabberAngleBox.setMaximum(90)

        self.horizontalLayout_2.addWidget(self.grabberAngleBox)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_14)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.grabButton = QPushButton(self.grabberFrame)
        self.grabButton.setObjectName(u"grabButton")
        sizePolicy.setHeightForWidth(self.grabButton.sizePolicy().hasHeightForWidth())
        self.grabButton.setSizePolicy(sizePolicy)
        self.grabButton.setFont(font)

        self.horizontalLayout_3.addWidget(self.grabButton)

        self.releaseButton = QPushButton(self.grabberFrame)
        self.releaseButton.setObjectName(u"releaseButton")
        sizePolicy.setHeightForWidth(self.releaseButton.sizePolicy().hasHeightForWidth())
        self.releaseButton.setSizePolicy(sizePolicy)
        self.releaseButton.setFont(font)

        self.horizontalLayout_3.addWidget(self.releaseButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.controlLayout.addWidget(self.grabberFrame)


        self.horizontalLayout_11.addLayout(self.controlLayout)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_17)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_15)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 33))
        self.menuFIle = QMenu(self.menubar)
        self.menuFIle.setObjectName(u"menuFIle")
        self.menuSerial = QMenu(self.menubar)
        self.menuSerial.setObjectName(u"menuSerial")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuSerial.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menuFIle.addAction(self.actionSave)
        self.menuFIle.addAction(self.actionLoad)
        self.menuView.addAction(self.actionControls)

        self.retranslateUi(MainWindow)
        self.speedSlider.valueChanged.connect(self.speedBox.setValue)
        self.grabberAngleSlider.valueChanged.connect(self.grabberAngleBox.setValue)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionLoad.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.actionControls.setText(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.actionMask.setText(QCoreApplication.translate("MainWindow", u"Mask", None))
        self.display.setText("")
        self.identifyButton.setText(QCoreApplication.translate("MainWindow", u"Identify Defects", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Model:", None))
        self.models.setItemText(0, QCoreApplication.translate("MainWindow", u"bottle", None))
        self.models.setItemText(1, QCoreApplication.translate("MainWindow", u"cable", None))
        self.models.setItemText(2, QCoreApplication.translate("MainWindow", u"capsule", None))
        self.models.setItemText(3, QCoreApplication.translate("MainWindow", u"carpet", None))
        self.models.setItemText(4, QCoreApplication.translate("MainWindow", u"grid", None))
        self.models.setItemText(5, QCoreApplication.translate("MainWindow", u"hazelnut", None))
        self.models.setItemText(6, QCoreApplication.translate("MainWindow", u"leather", None))
        self.models.setItemText(7, QCoreApplication.translate("MainWindow", u"metal nut", None))
        self.models.setItemText(8, QCoreApplication.translate("MainWindow", u"pill", None))
        self.models.setItemText(9, QCoreApplication.translate("MainWindow", u"screw", None))
        self.models.setItemText(10, QCoreApplication.translate("MainWindow", u"tile", None))
        self.models.setItemText(11, QCoreApplication.translate("MainWindow", u"toothbrush", None))
        self.models.setItemText(12, QCoreApplication.translate("MainWindow", u"transistor", None))
        self.models.setItemText(13, QCoreApplication.translate("MainWindow", u"wood", None))
        self.models.setItemText(14, QCoreApplication.translate("MainWindow", u"zipper", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Threshold", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"XYZ", None))
        self.speedLabel.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"X (mm)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Y (mm)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Z (mm)", None))
        self.xPosButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.xNegButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.yPosButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.yNegButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.zPosButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.zNegButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Pedestal", None))
        self.pos90Button.setText(QCoreApplication.translate("MainWindow", u"+90\u00b0", None))
        self.neg90Button.setText(QCoreApplication.translate("MainWindow", u"-90\u00b0", None))
        self.pos45Button.setText(QCoreApplication.translate("MainWindow", u"+45\u00b0", None))
        self.neg45Button.setText(QCoreApplication.translate("MainWindow", u"-45\u00b0", None))
        self.posRotate.setText("")
        self.negRotateButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Grabber", None))
        self.grabberAngleLabel.setText(QCoreApplication.translate("MainWindow", u"Angle", None))
        self.grabButton.setText(QCoreApplication.translate("MainWindow", u"Grab", None))
        self.releaseButton.setText(QCoreApplication.translate("MainWindow", u"Release", None))
        self.menuFIle.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSerial.setTitle(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

