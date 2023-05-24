® By Soumalya Mondal ®

from PyQt5 import QtCore, QtGui, QtWidgets
from math import ceil, floor


class Ui_mainWindow(object):

    # custom function start
    def calculateEnergy(self):
        # taking value from entry widget
        t1= self.hotWaterVal.value()
        t2= self.coldWaterVal.value()
        M= self.waterNeedVal.value()
        T= self.waterNeedTempVal.value()

        # checking the inout value is corret or not
        if t1==t2 or t1<T or t2>T:
            # setting wrong input field visibility to on and display to zero
            self.wrongInputLbl.setVisible(True)
            self.hotWaterLcdVal.display(0)
            self.coldWaterLcdVal.display(0)
            
        else:
            # setting wrong input visibility to off
            self.wrongInputLbl.setVisible(False)

            # doing calculation regarding input
            hot_water_need= ceil((M*T-M*t2)/(t1-t2))
            cold_water_need= floor(M- hot_water_need)

            # displaying value to lcd display
            self.hotWaterLcdVal.display(hot_water_need)
            self.coldWaterLcdVal.display(cold_water_need)
    # custom function end

    def setupUi(self, mainWindow):

        # main window start
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(600, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(600, 350))
        mainWindow.setMaximumSize(QtCore.QSize(600, 350))
        mainWindow.setBaseSize(QtCore.QSize(600, 400))
        font = QtGui.QFont()
        font.setPointSize(14)
        mainWindow.setFont(font)
        mainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        mainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        mainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        # main window end

        # main widget start
        self.mainWidget = QtWidgets.QWidget(mainWindow)
        self.mainWidget.setObjectName("mainWidget")
        # main widget end

        # hot water temp label start
        self.hotWaterLbl = QtWidgets.QLabel(self.mainWidget)
        self.hotWaterLbl.setGeometry(QtCore.QRect(80, 20, 230, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.hotWaterLbl.setFont(font)
        self.hotWaterLbl.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hotWaterLbl.setObjectName("hotWaterLbl")
        # hot water temp label end

        # hot water temp in degree label start
        self.hotWaterDeg = QtWidgets.QLabel(self.mainWidget)
        self.hotWaterDeg.setGeometry(QtCore.QRect(500, 20, 20, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.hotWaterDeg.setFont(font)
        self.hotWaterDeg.setObjectName("hotWaterDeg")
        # hot water temp in degree label start

        # cold water temp label start
        self.coldWaterLbl = QtWidgets.QLabel(self.mainWidget)
        self.coldWaterLbl.setGeometry(QtCore.QRect(80, 60, 240, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.coldWaterLbl.setFont(font)
        self.coldWaterLbl.setObjectName("coldWaterLbl")
        # cold water label end

        # cold water temp in degree start
        self.coldWaterDeg = QtWidgets.QLabel(self.mainWidget)
        self.coldWaterDeg.setGeometry(QtCore.QRect(500, 60, 20, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.coldWaterDeg.setFont(font)
        self.coldWaterDeg.setObjectName("coldWaterDeg")
        # cold water temp in degree label end

        # water need label start
        self.waterNeedLbl = QtWidgets.QLabel(self.mainWidget)
        self.waterNeedLbl.setGeometry(QtCore.QRect(80, 100, 265, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.waterNeedLbl.setFont(font)
        self.waterNeedLbl.setObjectName("waterNeedLbl")
        # water need lable end

        # water need in liter label start
        self.waterNeedLtr = QtWidgets.QLabel(self.mainWidget)
        self.waterNeedLtr.setGeometry(QtCore.QRect(500, 100, 30, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.waterNeedLtr.setFont(font)
        self.waterNeedLtr.setObjectName("waterNeedLtr")
        # water need in liter lable end

        # water need temp label start
        self.waterNeedTempLbl = QtWidgets.QLabel(self.mainWidget)
        self.waterNeedTempLbl.setGeometry(QtCore.QRect(80, 140, 250, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.waterNeedTempLbl.setFont(font)
        self.waterNeedTempLbl.setObjectName("waterNeedTempLbl")
        # water need temp label end

        # water need temp in degree lable start
        self.waterNeedTempDeg = QtWidgets.QLabel(self.mainWidget)
        self.waterNeedTempDeg.setGeometry(QtCore.QRect(500, 140, 20, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.waterNeedTempDeg.setFont(font)
        self.waterNeedTempDeg.setObjectName("waterNeedTempDeg")
        # water need temp in degree label end

        # calculate push button start
        self.calculateWater = QtWidgets.QPushButton(self.mainWidget)
        self.calculateWater.setGeometry(QtCore.QRect(75, 190, 450, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.calculateWater.setFont(font)
        self.calculateWater.setAutoDefault(False)
        self.calculateWater.setDefault(False)
        self.calculateWater.setFlat(False)
        self.calculateWater.setObjectName("calculateWater")
        self.calculateWater.clicked.connect(self.calculateEnergy)
        # calculate push button end

        # hot water lcd display label start
        self.hotWaterLcdLbl = QtWidgets.QLabel(self.mainWidget)
        self.hotWaterLcdLbl.setGeometry(QtCore.QRect(30, 280, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.hotWaterLcdLbl.setFont(font)
        self.hotWaterLcdLbl.setObjectName("hotWaterLcdLbl")
        # hot water lcd display label end

        # hot water lcd display value start
        self.hotWaterLcdVal = QtWidgets.QLCDNumber(self.mainWidget)
        self.hotWaterLcdVal.setGeometry(QtCore.QRect(140, 280, 70, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.hotWaterLcdVal.setFont(font)
        self.hotWaterLcdVal.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.hotWaterLcdVal.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hotWaterLcdVal.setDigitCount(3)
        self.hotWaterLcdVal.setMode(QtWidgets.QLCDNumber.Dec)
        self.hotWaterLcdVal.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.hotWaterLcdVal.setProperty("value", 0.0)
        self.hotWaterLcdVal.setProperty("intValue", 0)
        self.hotWaterLcdVal.setObjectName("hotWaterLcdVal")
        # hot water lcd display valu end

        # hot water lcd display in liter start
        self.hotWaterLcdLtr = QtWidgets.QLabel(self.mainWidget)
        self.hotWaterLcdLtr.setGeometry(QtCore.QRect(220, 280, 30, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.hotWaterLcdLtr.setFont(font)
        self.hotWaterLcdLtr.setObjectName("hotWaterLcdLtr")
        # hot water lcd display in liter end

        # cold water lcd display label start
        self.coldWaterLcdLbl = QtWidgets.QLabel(self.mainWidget)
        self.coldWaterLcdLbl.setGeometry(QtCore.QRect(330, 280, 110, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.coldWaterLcdLbl.setFont(font)
        self.coldWaterLcdLbl.setObjectName("coldWaterLcdLbl")
        # cold water lcd display label end

        # cold water lcd display value start
        self.coldWaterLcdVal = QtWidgets.QLCDNumber(self.mainWidget)
        self.coldWaterLcdVal.setGeometry(QtCore.QRect(450, 280, 70, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.coldWaterLcdVal.setFont(font)
        self.coldWaterLcdVal.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.coldWaterLcdVal.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.coldWaterLcdVal.setDigitCount(3)
        self.coldWaterLcdVal.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.coldWaterLcdVal.setProperty("value", 0.0)
        self.coldWaterLcdVal.setProperty("intValue", 0)
        self.coldWaterLcdVal.setObjectName("coldWaterLcdVal")
        # cold water lcd display value end

        # cold water lcd display in liter start
        self.coldWaterLcdLtr = QtWidgets.QLabel(self.mainWidget)
        self.coldWaterLcdLtr.setGeometry(QtCore.QRect(530, 280, 30, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.coldWaterLcdLtr.setFont(font)
        self.coldWaterLcdLtr.setObjectName("coldWaterLcdLtr")
        # cold water lcd display in liter end

        # hot water temp entry start
        self.hotWaterVal = QtWidgets.QDoubleSpinBox(self.mainWidget)
        self.hotWaterVal.setGeometry(QtCore.QRect(420, 20, 70, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.hotWaterVal.setFont(font)
        self.hotWaterVal.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.hotWaterVal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.hotWaterVal.setAutoFillBackground(False)
        self.hotWaterVal.setDecimals(1)
        self.hotWaterVal.setMaximum(250.0)
        self.hotWaterVal.setSingleStep(0.5)
        self.hotWaterVal.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.hotWaterVal.setObjectName("hotWaterVal")
        # hot water temp entry end

        # cold water temp enty start
        self.coldWaterVal = QtWidgets.QDoubleSpinBox(self.mainWidget)
        self.coldWaterVal.setGeometry(QtCore.QRect(420, 60, 70, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.coldWaterVal.setFont(font)
        self.coldWaterVal.setDecimals(1)
        self.coldWaterVal.setMinimum(-50.0)
        self.coldWaterVal.setSingleStep(0.5)
        self.coldWaterVal.setObjectName("coldWaterVal")
        # cold water temp entry end

        # water need entry start
        self.waterNeedVal = QtWidgets.QSpinBox(self.mainWidget)
        self.waterNeedVal.setGeometry(QtCore.QRect(420, 100, 70, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.waterNeedVal.setFont(font)
        self.waterNeedVal.setMaximum(999)
        self.waterNeedVal.setProperty("value", 0)
        self.waterNeedVal.setObjectName("waterNeedVal")
        # water need entry end

        # water need in temp entry start
        self.waterNeedTempVal = QtWidgets.QDoubleSpinBox(self.mainWidget)
        self.waterNeedTempVal.setGeometry(QtCore.QRect(420, 140, 70, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.waterNeedTempVal.setFont(font)
        self.waterNeedTempVal.setDecimals(1)
        self.waterNeedTempVal.setMinimum(-10.0)
        self.waterNeedTempVal.setSingleStep(0.5)
        self.waterNeedTempVal.setObjectName("waterNeedTempVal")
        # water need in temp entry end
        
        # wrong input label start
        self.wrongInputLbl = QtWidgets.QLabel(self.mainWidget)
        self.wrongInputLbl.setEnabled(True)
        self.wrongInputLbl.setGeometry(QtCore.QRect(240, 230, 120, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.wrongInputLbl.setFont(font)
        self.wrongInputLbl.setStyleSheet("background-color: rgb(255, 0, 0);\n"
        "color: rgb(255, 255, 255);")
        self.wrongInputLbl.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.wrongInputLbl.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.wrongInputLbl.setObjectName("wrongInputLbl")
        self.wrongInputLbl.setVisible(False)
        # wrong input label end

        mainWindow.setCentralWidget(self.mainWidget)
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Water Energy Calculator"))
        self.hotWaterLbl.setText(_translate("mainWindow", "Hot Water Temperature"))
        self.hotWaterDeg.setText(_translate("mainWindow", "°C"))
        self.coldWaterLbl.setText(_translate("mainWindow", "Cold Water Temperature"))
        self.coldWaterDeg.setText(_translate("mainWindow", "°C"))
        self.waterNeedLbl.setText(_translate("mainWindow", "How Much Water You Need"))
        self.waterNeedLtr.setText(_translate("mainWindow", "Ltr."))
        self.waterNeedTempLbl.setText(_translate("mainWindow", "Temp. Of Water You Need"))
        self.waterNeedTempDeg.setText(_translate("mainWindow", "°C"))
        self.calculateWater.setText(_translate("mainWindow", "Calculate The Amount Of Water You Need"))
        self.hotWaterLcdLbl.setText(_translate("mainWindow", "Hot Water"))
        self.hotWaterLcdLtr.setText(_translate("mainWindow", "Ltr."))
        self.coldWaterLcdLbl.setText(_translate("mainWindow", "Cold Water"))
        self.coldWaterLcdLtr.setText(_translate("mainWindow", "Ltr."))
        self.wrongInputLbl.setText(_translate("mainWindow", "Wrong Input"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
