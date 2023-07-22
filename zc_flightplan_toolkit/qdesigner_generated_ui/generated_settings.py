# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
    QAbstractButton,
    QApplication,
    QDialog,
    QDialogButtonBox,
    QGridLayout,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QWidget,
)


class Ui_preferences_dialog(object):
    def setupUi(self, preferences_dialog):
        if not preferences_dialog.objectName():
            preferences_dialog.setObjectName("preferences_dialog")
        preferences_dialog.setWindowModality(Qt.NonModal)
        preferences_dialog.resize(506, 99)
        preferences_dialog.setModal(False)
        self.gridLayout = QGridLayout(preferences_dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.checkwx_api_key_lineedit = QLineEdit(preferences_dialog)
        self.checkwx_api_key_lineedit.setObjectName("checkwx_api_key_lineedit")

        self.gridLayout.addWidget(self.checkwx_api_key_lineedit, 3, 0, 1, 1)

        self.aero_api_key_lineedit = QLineEdit(preferences_dialog)
        self.aero_api_key_lineedit.setObjectName("aero_api_key_lineedit")

        self.gridLayout.addWidget(self.aero_api_key_lineedit, 1, 0, 1, 1)

        self.aero_api_key_label = QLabel(preferences_dialog)
        self.aero_api_key_label.setObjectName("aero_api_key_label")

        self.gridLayout.addWidget(self.aero_api_key_label, 0, 0, 1, 1)

        self.check_wx_api_key_label = QLabel(preferences_dialog)
        self.check_wx_api_key_label.setObjectName("check_wx_api_key_label")

        self.gridLayout.addWidget(self.check_wx_api_key_label, 2, 0, 1, 1)

        self.save_cancel_button_box = QDialogButtonBox(preferences_dialog)
        self.save_cancel_button_box.setObjectName("save_cancel_button_box")
        self.save_cancel_button_box.setOrientation(Qt.Vertical)
        self.save_cancel_button_box.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Save
        )

        self.gridLayout.addWidget(self.save_cancel_button_box, 1, 1, 3, 1)

        self.retranslateUi(preferences_dialog)
        self.save_cancel_button_box.accepted.connect(preferences_dialog.accept)
        self.save_cancel_button_box.rejected.connect(preferences_dialog.reject)

        QMetaObject.connectSlotsByName(preferences_dialog)

    # setupUi

    def retranslateUi(self, preferences_dialog):
        preferences_dialog.setWindowTitle(
            QCoreApplication.translate("preferences_dialog", "Preferences", None)
        )
        self.aero_api_key_label.setText(
            QCoreApplication.translate("preferences_dialog", "Aero API Key", None)
        )
        self.check_wx_api_key_label.setText(
            QCoreApplication.translate("preferences_dialog", "Check WX API Key", None)
        )

    # retranslateUi
