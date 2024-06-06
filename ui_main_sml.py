# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sml.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(641, 307)
        self.information = QTextEdit(Form)
        self.information.setObjectName(u"information")
        self.information.setGeometry(QRect(30, 190, 321, 61))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 40, 331, 24))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(7, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setSizeIncrement(QSize(0, 0))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.comboBox_PortDetect = QComboBox(self.layoutWidget)
        self.comboBox_PortDetect.setObjectName(u"comboBox_PortDetect")
        self.comboBox_PortDetect.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.comboBox_PortDetect)

        self.layoutWidget_1 = QWidget(Form)
        self.layoutWidget_1.setObjectName(u"layoutWidget_1")
        self.layoutWidget_1.setGeometry(QRect(40, 90, 223, 24))
        self.horizontalLayout_1 = QHBoxLayout(self.layoutWidget_1)
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.freq_label = QLabel(self.layoutWidget_1)
        self.freq_label.setObjectName(u"freq_label")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.freq_label.setFont(font)

        self.horizontalLayout_1.addWidget(self.freq_label)

        self.freq = QLineEdit(self.layoutWidget_1)
        self.freq.setObjectName(u"freq")

        self.horizontalLayout_1.addWidget(self.freq)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.information.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">informations:</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"Port Com", None))
        self.freq_label.setText(QCoreApplication.translate("Form", u"Fr\u00e9quence", None))
    # retranslateUi

