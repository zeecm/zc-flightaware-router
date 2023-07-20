# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableView, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1506, 930)
        self.actionPreferences = QAction(mainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.main_tabs = QTabWidget(self.centralwidget)
        self.main_tabs.setObjectName(u"main_tabs")
        self.route_info_tab = QWidget()
        self.route_info_tab.setObjectName(u"route_info_tab")
        self.gridLayout_3 = QGridLayout(self.route_info_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 1000, -1)
        self.start_airport_label = QLabel(self.route_info_tab)
        self.start_airport_label.setObjectName(u"start_airport_label")

        self.horizontalLayout_2.addWidget(self.start_airport_label)

        self.start_airport_lineedit = QLineEdit(self.route_info_tab)
        self.start_airport_lineedit.setObjectName(u"start_airport_lineedit")

        self.horizontalLayout_2.addWidget(self.start_airport_lineedit)

        self.end_airport_label = QLabel(self.route_info_tab)
        self.end_airport_label.setObjectName(u"end_airport_label")

        self.horizontalLayout_2.addWidget(self.end_airport_label)

        self.end_airport_lineedit = QLineEdit(self.route_info_tab)
        self.end_airport_lineedit.setObjectName(u"end_airport_lineedit")

        self.horizontalLayout_2.addWidget(self.end_airport_lineedit)

        self.get_route_info_button = QPushButton(self.route_info_tab)
        self.get_route_info_button.setObjectName(u"get_route_info_button")
        self.get_route_info_button.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.get_route_info_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.route_info_table = QTableView(self.route_info_tab)
        self.route_info_table.setObjectName(u"route_info_table")

        self.verticalLayout_2.addWidget(self.route_info_table)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.main_tabs.addTab(self.route_info_tab, "")
        self.airport_info_tab = QWidget()
        self.airport_info_tab.setObjectName(u"airport_info_tab")
        self.gridLayout = QGridLayout(self.airport_info_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 1200, -1)
        self.enter_airport_id_label = QLabel(self.airport_info_tab)
        self.enter_airport_id_label.setObjectName(u"enter_airport_id_label")

        self.horizontalLayout.addWidget(self.enter_airport_id_label)

        self.airport_id_lineedit = QLineEdit(self.airport_info_tab)
        self.airport_id_lineedit.setObjectName(u"airport_id_lineedit")

        self.horizontalLayout.addWidget(self.airport_id_lineedit)

        self.get_airport_info_button = QPushButton(self.airport_info_tab)
        self.get_airport_info_button.setObjectName(u"get_airport_info_button")
        self.get_airport_info_button.setAutoDefault(True)

        self.horizontalLayout.addWidget(self.get_airport_info_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.airport_info_table = QTableView(self.airport_info_tab)
        self.airport_info_table.setObjectName(u"airport_info_table")

        self.verticalLayout.addWidget(self.airport_info_table)


        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.main_tabs.addTab(self.airport_info_tab, "")

        self.gridLayout_2.addWidget(self.main_tabs, 0, 0, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1506, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionPreferences)

        self.retranslateUi(mainWindow)

        self.main_tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"ZhaoCong's FlightAware Router", None))
        self.actionPreferences.setText(QCoreApplication.translate("mainWindow", u"Preferences", None))
        self.start_airport_label.setText(QCoreApplication.translate("mainWindow", u"Start Airport ID:", None))
        self.end_airport_label.setText(QCoreApplication.translate("mainWindow", u"End Airport ID:", None))
        self.get_route_info_button.setText(QCoreApplication.translate("mainWindow", u"Get Route Info", None))
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.route_info_tab), QCoreApplication.translate("mainWindow", u"Route Information", None))
        self.enter_airport_id_label.setText(QCoreApplication.translate("mainWindow", u"Enter Airport ID:", None))
        self.get_airport_info_button.setText(QCoreApplication.translate("mainWindow", u"Get Airport Info", None))
        self.main_tabs.setTabText(self.main_tabs.indexOf(self.airport_info_tab), QCoreApplication.translate("mainWindow", u"Airport Information", None))
        self.menuFile.setTitle(QCoreApplication.translate("mainWindow", u"File", None))
    # retranslateUi

