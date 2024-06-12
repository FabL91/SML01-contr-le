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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.WindowModality.NonModal)
        Form.resize(325, 296)
        Form.setMinimumSize(QSize(320, 295))
        Form.setMaximumSize(QSize(325, 296))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 304, 278))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox_PortDetect = QComboBox(self.widget)
        self.comboBox_PortDetect.setObjectName(u"comboBox_PortDetect")
        self.comboBox_PortDetect.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.comboBox_PortDetect, 0, 1, 1, 2)

        self.freq_label = QLabel(self.widget)
        self.freq_label.setObjectName(u"freq_label")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.freq_label.setFont(font1)

        self.gridLayout.addWidget(self.freq_label, 1, 0, 1, 1)

        self.freq = QLineEdit(self.widget)
        self.freq.setObjectName(u"freq")

        self.gridLayout.addWidget(self.freq, 1, 1, 1, 2)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.puiss = QLineEdit(self.widget)
        self.puiss.setObjectName(u"puiss")

        self.gridLayout.addWidget(self.puiss, 2, 2, 1, 1)

        self.information = QTextEdit(self.widget)
        self.information.setObjectName(u"information")

        self.gridLayout.addWidget(self.information, 3, 0, 1, 3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Signal Generator Control", None))
        self.label.setText(QCoreApplication.translate("Form", u"Port Com", None))
        self.freq_label.setText(QCoreApplication.translate("Form", u"Fr\u00e9quence", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Puissance(-140 \u00e0 13)", None))
        self.information.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">informations:</span></p></body></html>", None))
    # retranslateUi

