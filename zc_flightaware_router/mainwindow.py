# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QTableView,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1506, 930)
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.main_tabs = QTabWidget(self.centralwidget)
        self.main_tabs.setObjectName("main_tabs")
        self.route_info_tab = QWidget()
        self.route_info_tab.setObjectName("route_info_tab")
        self.gridLayout_3 = QGridLayout(self.route_info_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 1000, -1)
        self.start_airport_label = QLabel(self.route_info_tab)
        self.start_airport_label.setObjectName("start_airport_label")

        self.horizontalLayout_2.addWidget(self.start_airport_label)

        self.lineEdit_2 = QLineEdit(self.route_info_tab)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.end_airport_label = QLabel(self.route_info_tab)
        self.end_airport_label.setObjectName("end_airport_label")

        self.horizontalLayout_2.addWidget(self.end_airport_label)

        self.lineEdit = QLineEdit(self.route_info_tab)
        self.lineEdit.setObjectName("lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.get_route_info_button = QPushButton(self.route_info_tab)
        self.get_route_info_button.setObjectName("get_route_info_button")

        self.horizontalLayout_2.addWidget(self.get_route_info_button)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tableView_2 = QTableView(self.route_info_tab)
        self.tableView_2.setObjectName("tableView_2")

        self.verticalLayout_2.addWidget(self.tableView_2)

        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.main_tabs.addTab(self.route_info_tab, "")
        self.airport_info_tab = QWidget()
        self.airport_info_tab.setObjectName("airport_info_tab")
        self.gridLayout = QGridLayout(self.airport_info_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 1200, -1)
        self.enter_airport_id_label = QLabel(self.airport_info_tab)
        self.enter_airport_id_label.setObjectName("enter_airport_id_label")

        self.horizontalLayout.addWidget(self.enter_airport_id_label)

        self.airport_id_lineedit = QLineEdit(self.airport_info_tab)
        self.airport_id_lineedit.setObjectName("airport_id_lineedit")

        self.horizontalLayout.addWidget(self.airport_id_lineedit)

        self.get_airport_info_button = QPushButton(self.airport_info_tab)
        self.get_airport_info_button.setObjectName("get_airport_info_button")

        self.horizontalLayout.addWidget(self.get_airport_info_button)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableView = QTableView(self.airport_info_tab)
        self.tableView.setObjectName("tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.main_tabs.addTab(self.airport_info_tab, "")

        self.gridLayout_2.addWidget(self.main_tabs, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1506, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionPreferences)

        self.retranslateUi(MainWindow)

        self.main_tabs.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.actionPreferences.setText(
            QCoreApplication.translate("MainWindow", "Preferences", None)
        )
        self.start_airport_label.setText(
            QCoreApplication.translate("MainWindow", "Start Airport ID:", None)
        )
        self.end_airport_label.setText(
            QCoreApplication.translate("MainWindow", "End Airport ID:", None)
        )
        self.get_route_info_button.setText(
            QCoreApplication.translate("MainWindow", "Get Route Info", None)
        )
        self.main_tabs.setTabText(
            self.main_tabs.indexOf(self.route_info_tab),
            QCoreApplication.translate("MainWindow", "Route Information", None),
        )
        self.enter_airport_id_label.setText(
            QCoreApplication.translate("MainWindow", "Enter Airport ID:", None)
        )
        self.get_airport_info_button.setText(
            QCoreApplication.translate("MainWindow", "Get Airport Info", None)
        )
        self.main_tabs.setTabText(
            self.main_tabs.indexOf(self.airport_info_tab),
            QCoreApplication.translate("MainWindow", "Airport Information", None),
        )
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "File", None))

    # retranslateUi
