#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import json
import os
import subprocess
import sys
from urllib import request

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from lib.aestheticclock import aestclockProcess
from lib.burnmywindows import burnMyWindows
from lib.devel import develPackages
from lib.figma import figma_linux
from lib.mirrorlist import mirrorList
from lib.onedrive import OneDrive
from lib.onedrivegui import OneDriveGui
from lib.packagemanager import packageManager
from lib.purpleBitches import purpleBitches
from lib.simplestupidlauncher import simpleLauncher
from lib.systemMonitor import SystemMonitor


class Progress(QThread):
    _signal = Signal(int)
    def __init__(self):
        super(Progress, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        os.chdir('src')
        print(os.getcwd())
        with open('packages.txt', 'r') as f:
            for i in range(101):
                for line in f:
                    l = subprocess.run(f"yay -S --needed --noconfirm {line}", shell=True)  
                    l + 1 
                    self._signal.emit(i)

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.horizontalLayoutWidget = QWidget(self.page_1)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(-10, 0, 831, 101))
        self.HBL1 = QHBoxLayout(self.horizontalLayoutWidget)
        self.HBL1.setObjectName(u"HBL1")
        self.HBL1.setContentsMargins(0, 0, 0, 0)
        self.HS2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.HBL1.addItem(self.HS2)
        self.title_label = QLabel(self.horizontalLayoutWidget)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setStyleSheet(u"font: 62pt \"JK Abode\";")
        self.HBL1.addWidget(self.title_label)
        self.HS1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.HBL1.addItem(self.HS1)
        self.horizontalLayoutWidget_2 = QWidget(self.page_1)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(-10, 520, 831, 80))
        self.HBL2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.HBL2.setObjectName(u"HBL2")
        self.HBL2.setContentsMargins(0, 0, 0, 0)
        self.HS4 = QSpacerItem(550, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.HBL2.addItem(self.HS4)
        self.nextButton = QPushButton(self.horizontalLayoutWidget_2)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setEnabled(False)
        self.HBL2.addWidget(self.nextButton)
        self.cancelButton_1 = QPushButton(self.horizontalLayoutWidget_2)
        self.cancelButton_1.setObjectName(u"cancelButton_1")
        self.HBL2.addWidget(self.cancelButton_1)
        self.HS3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.HBL2.addItem(self.HS3)
        self.horizontalLayoutWidget_3 = QWidget(self.page_1)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(-1, 440, 801, 80))
        self.HBL3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.HBL3.setObjectName(u"HBL3")
        self.HBL3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget_4 = QWidget(self.page_1)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(200, 180, 401, 81))
        self.HBL4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.HBL4.setObjectName(u"HBL4")
        self.HBL4.setContentsMargins(0, 0, 0, 0)
        self.HS6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.HBL4.addItem(self.HS6)
        self.status_label = QLabel(self.horizontalLayoutWidget_4)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setEnabled(True)
        self.status_label.setFocusPolicy(Qt.NoFocus)
        self.status_label.setFrameShape(QFrame.NoFrame)
        self.status_label.setFrameShadow(QFrame.Plain)
        self.status_label.setScaledContents(False)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setTextInteractionFlags(Qt.NoTextInteraction)
        self.HBL4.addWidget(self.status_label)
        self.NetworkStatus = QLineEdit(self.horizontalLayoutWidget_4)
        self.NetworkStatus.setObjectName(u"NetworkStatus")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.NetworkStatus.sizePolicy().hasHeightForWidth())
        self.NetworkStatus.setSizePolicy(sizePolicy1)
        self.NetworkStatus.setMinimumSize(QSize(50, 0))
        self.NetworkStatus.setMaximumSize(QSize(50, 16777215))
        self.NetworkStatus.setFocusPolicy(Qt.NoFocus)
        self.NetworkStatus.setStyleSheet(u"QLineEdit#NetworkStatus {\n"
"	color: rgb(170, 0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.NetworkStatus.setFrame(False)
        self.NetworkStatus.setAlignment(Qt.AlignCenter)
        self.NetworkStatus.setReadOnly(True)
        self.HBL4.addWidget(self.NetworkStatus, 0, Qt.AlignLeft)
        self.HS5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.HBL4.addItem(self.HS5)
        self.verticalLayoutWidget = QWidget(self.page_1)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(300, 240, 144, 141))
        self.HBL5 = QVBoxLayout(self.verticalLayoutWidget)
        self.HBL5.setObjectName(u"HBL5")
        self.HBL5.setContentsMargins(0, 0, 0, 0)
        self.mirrorlist = QCheckBox(self.verticalLayoutWidget)
        self.mirrorlist.setObjectName(u"mirrorlist")
        self.mirrorlist.setFocusPolicy(Qt.NoFocus)
        self.mirrorlist.setContextMenuPolicy(Qt.NoContextMenu)
        self.mirrorlist.setLayoutDirection(Qt.RightToLeft)
        self.mirrorlist.setEnabled(False)
        self.mirrorlist.setCheckable(True)
        self.HBL5.addWidget(self.mirrorlist)
        self.baseDevel = QCheckBox(self.verticalLayoutWidget)
        self.baseDevel.setObjectName(u"baseDevel")
        self.baseDevel.setFocusPolicy(Qt.NoFocus)
        self.baseDevel.setContextMenuPolicy(Qt.NoContextMenu)
        self.baseDevel.setLayoutDirection(Qt.RightToLeft)
        self.baseDevel.setEnabled(False)
        self.baseDevel.setCheckable(True)
        self.HBL5.addWidget(self.baseDevel)
        self.yay = QCheckBox(self.verticalLayoutWidget)
        self.yay.setObjectName(u"yay")
        self.yay.setFocusPolicy(Qt.NoFocus)
        self.yay.setContextMenuPolicy(Qt.NoContextMenu)
        self.yay.setLayoutDirection(Qt.RightToLeft)
        self.yay.setEnabled(False)
        self.yay.setCheckable(True)
        self.HBL5.addWidget(self.yay)
        self.horizontalLayoutWidget_7 = QWidget(self.page_1)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(210, 400, 411, 42))
        self.HBL8 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.HBL8.setObjectName(u"HBL8")
        self.HBL8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.HBL8.addItem(self.horizontalSpacer_2)
        self.startButton = QPushButton(self.horizontalLayoutWidget_7)
        self.startButton.setObjectName(u"startButton")
        self.HBL8.addWidget(self.startButton)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.HBL8.addItem(self.horizontalSpacer)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayoutWidget_5 = QWidget(self.page_2)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(0, 440, 801, 80))
        self.HBL6 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.HBL6.setObjectName(u"HBL6")
        self.HBL6.setContentsMargins(0, 0, 0, 0)
        self.HS8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.HBL6.addItem(self.HS8)
        self.installButton = QPushButton(self.horizontalLayoutWidget_5)
        self.installButton.setObjectName(u"installButton")
        self.HBL6.addWidget(self.installButton)
        self.HS7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.HBL6.addItem(self.HS7)
        self.horizontalLayoutWidget_6 = QWidget(self.page_2)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(0, 520, 801, 80))
        self.HBL7 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.HBL7.setObjectName(u"HBL7")
        self.HBL7.setContentsMargins(0, 0, 0, 0)
        self.HS9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.HBL7.addItem(self.HS9)
        self.finishButton = QPushButton(self.horizontalLayoutWidget_6)
        self.finishButton.setObjectName(u"finishButton")
        self.finishButton.setEnabled(False)
        self.HBL7.addWidget(self.finishButton)
        self.cancelButton_2 = QPushButton(self.horizontalLayoutWidget_6)
        self.cancelButton_2.setObjectName(u"cancelButton_2")
        self.HBL7.addWidget(self.cancelButton_2)
        self.gridLayoutWidget = QWidget(self.page_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setEnabled(True)
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 801, 441))
        self.GL = QGridLayout(self.gridLayoutWidget)
        self.GL.setObjectName(u"GL")
        self.GL.setContentsMargins(0, 0, 0, 0)
        self.simpleStupidLauncher = QCheckBox(self.gridLayoutWidget)
        self.simpleStupidLauncher.setObjectName(u"simpleStupidLauncher")
        self.simpleStupidLauncher.setEnabled(False)
        self.simpleStupidLauncher.setFocusPolicy(Qt.NoFocus)
        self.simpleStupidLauncher.setLayoutDirection(Qt.RightToLeft)
        self.simpleStupidLauncher.setCheckable(True)
        self.GL.addWidget(self.simpleStupidLauncher, 1, 0, 1, 1, Qt.AlignHCenter)
        self.burnMyWindows = QCheckBox(self.gridLayoutWidget)
        self.burnMyWindows.setObjectName(u"burnMyWindows")
        self.burnMyWindows.setEnabled(False)
        self.burnMyWindows.setFocusPolicy(Qt.NoFocus)
        self.burnMyWindows.setLayoutDirection(Qt.RightToLeft)
        self.burnMyWindows.setCheckable(True)
        self.GL.addWidget(self.burnMyWindows, 2, 0, 1, 1, Qt.AlignHCenter)
        self.purpleBitchIcons = QCheckBox(self.gridLayoutWidget)
        self.purpleBitchIcons.setObjectName(u"purpleBitchIcons")
        self.purpleBitchIcons.setEnabled(False)
        self.purpleBitchIcons.setFocusPolicy(Qt.NoFocus)
        self.purpleBitchIcons.setLayoutDirection(Qt.RightToLeft)
        self.purpleBitchIcons.setCheckable(True)
        self.GL.addWidget(self.purpleBitchIcons, 1, 1, 1, 1, Qt.AlignHCenter)
        self.figmaLinux = QCheckBox(self.gridLayoutWidget)
        self.figmaLinux.setObjectName(u"figmaLinux")
        self.figmaLinux.setEnabled(False)
        self.figmaLinux.setFocusPolicy(Qt.NoFocus)
        self.figmaLinux.setLayoutDirection(Qt.RightToLeft)
        self.figmaLinux.setCheckable(True)
        self.GL.addWidget(self.figmaLinux, 0, 2, 1, 1, Qt.AlignHCenter)
        self.purpleBitchPlasma = QCheckBox(self.gridLayoutWidget)
        self.purpleBitchPlasma.setObjectName(u"purpleBitchPlasma")
        self.purpleBitchPlasma.setEnabled(False)
        self.purpleBitchPlasma.setFocusPolicy(Qt.NoFocus)
        self.purpleBitchPlasma.setLayoutDirection(Qt.RightToLeft)
        self.purpleBitchPlasma.setCheckable(True)
        self.GL.addWidget(self.purpleBitchPlasma, 0, 1, 1, 1, Qt.AlignHCenter)
        self.oneDrive = QCheckBox(self.gridLayoutWidget)
        self.oneDrive.setObjectName(u"oneDrive")
        self.oneDrive.setEnabled(False)
        self.oneDrive.setFocusPolicy(Qt.NoFocus)
        self.oneDrive.setLayoutDirection(Qt.RightToLeft)
        self.oneDrive.setCheckable(True)
        self.GL.addWidget(self.oneDrive, 1, 2, 1, 1, Qt.AlignHCenter)
        self.purpleBitchSddm = QCheckBox(self.gridLayoutWidget)
        self.purpleBitchSddm.setObjectName(u"purpleBitchSddm")
        self.purpleBitchSddm.setEnabled(False)
        self.purpleBitchSddm.setFocusPolicy(Qt.NoFocus)
        self.purpleBitchSddm.setLayoutDirection(Qt.RightToLeft)
        self.purpleBitchSddm.setCheckable(True)
        self.GL.addWidget(self.purpleBitchSddm, 2, 1, 1, 1, Qt.AlignHCenter)
        self.aestheticClock = QCheckBox(self.gridLayoutWidget)
        self.aestheticClock.setObjectName(u"aestheticClock")
        self.aestheticClock.setEnabled(False)
        self.aestheticClock.setFocusPolicy(Qt.NoFocus)
        self.aestheticClock.setLayoutDirection(Qt.RightToLeft)
        self.aestheticClock.setCheckable(True)
        self.GL.addWidget(self.aestheticClock, 0, 0, 1, 1, Qt.AlignHCenter)
        self.oneDriveGui = QCheckBox(self.gridLayoutWidget)
        self.oneDriveGui.setObjectName(u"oneDriveGui")
        self.oneDriveGui.setEnabled(False)
        self.oneDriveGui.setFocusPolicy(Qt.NoFocus)
        self.oneDriveGui.setLayoutDirection(Qt.RightToLeft)
        self.oneDriveGui.setCheckable(True)
        self.GL.addWidget(self.oneDriveGui, 2, 2, 1, 1, Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)


        self.retranslateUi()
        self.cancelButton_2.clicked.connect(self.close)
        self.cancelButton_1.clicked.connect(self.close)
        self.finishButton.clicked.connect(self.close)
        self.nextButton.clicked.connect(lambda: self.nextPage())
        self.startButton.clicked.connect(lambda: self.startConfigure())
        self.installButton.clicked.connect(lambda: self.startInstall())
        self.stackedWidget.setCurrentIndex(0)


        if connection == True:
            self.NetworkStatus.setText("Online")
            self.NetworkStatus.setStyleSheet("QLineEdit#NetworkStatus {\n"
                                            "   color: green;\n"
                                            "	background-color: transparent;\n"
                                            "}")
            
        elif connection == "offline":
            subprocess.run("echo '>>> ERROR: Can`t connect to Network'", shell=True)


        QMetaObject.connectSlotsByName(self)
    # setupUi




    def nextPage(self):
        self.stackedWidget.setCurrentIndex(1)

    def startConfigure(self):
        mirrorList(self)
        develPackages(self)
        packageManager(self)
        os.chdir('.')
        print(os.getcwd())
        f = open('src/packages.json')

        data = json.load(f)
        for i in data['packages']:
            subprocess.run(f"yay -S --needed --noconfirm {i}", shell=True)
        
        self.startButton.setEnabled(False)
        self.nextButton.setEnabled(True)
        
        
    def startInstall(self):
        aestclockProcess(self)
        burnMyWindows(self)
        figma_linux(self)
        OneDrive(self)
        OneDriveGui(self)
        purpleBitches(self)
        simpleLauncher(self)
        SystemMonitor(self)
        
        self.installButton.setEnabled(False)
        self.finishButton.setEnabled(True)
        self.cancelButton_2.setEnabled(False)
 
    
    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("self", u"self", None))
        self.title_label.setText(QCoreApplication.translate("self", u"install", None))
        self.nextButton.setText(QCoreApplication.translate("self", u"Next", None))
        self.cancelButton_1.setText(QCoreApplication.translate("self", u"Cancel", None))
        self.status_label.setText(QCoreApplication.translate("self", u"Network Status:", None))
        self.NetworkStatus.setText(QCoreApplication.translate("self", u"Offline", None))
        self.mirrorlist.setText(QCoreApplication.translate("self", u"Update Mirrorlist", None))
        self.baseDevel.setText(QCoreApplication.translate("self", u"Install Base[Devel]", None))
        self.yay.setText(QCoreApplication.translate("self", u"Install Yay", None))
        self.startButton.setText(QCoreApplication.translate("self", u"Start", None))
        self.installButton.setText(QCoreApplication.translate("self", u"Install", None))
        self.finishButton.setText(QCoreApplication.translate("self", u"Finish", None))
        self.cancelButton_2.setText(QCoreApplication.translate("self", u"Cancel", None))
        self.simpleStupidLauncher.setText(QCoreApplication.translate("self", u"Simple Stupid Launcher", None))
        self.burnMyWindows.setText(QCoreApplication.translate("self", u"Burn My Windows", None))
        self.purpleBitchIcons.setText(QCoreApplication.translate("self", u"Purple Bitch Icons", None))
        self.figmaLinux.setText(QCoreApplication.translate("self", u"Figma Linux", None))
        self.purpleBitchPlasma.setText(QCoreApplication.translate("self", u"Purple Bitch Plasma", None))
        self.oneDrive.setText(QCoreApplication.translate("self", u"OneDrive", None))
        self.purpleBitchSddm.setText(QCoreApplication.translate("self", u"Purple Bitch SDDM", None))
        self.aestheticClock.setText(QCoreApplication.translate("self", u"Aesthetic Clock", None))
        self.oneDriveGui.setText(QCoreApplication.translate("self", u"OneDrive GUI", None))
    # retranslateUi



def checkConnection():
    try:
        request.urlopen('http://google.com')
        return True
    except:
        return False

if __name__ == "__main__":
    global connection
    connection = checkConnection()

    
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec())

    