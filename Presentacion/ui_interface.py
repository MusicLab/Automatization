# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacepVufQI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Presentacion.resources2_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1250, 770)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"border:none;\n"
"padding:0;\n"
"margin: 0;\n"
"background-color:transparent;\n"
"background:transparent;\n"
"}\n"
"\n"
"#centralwidget{\n"
"border-image: url(\"E:/Prog/socinpy/soccrate2/Presentacion/img/space.png\") 0 0 0 0 stretch stretch;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.FrameBar = QFrame(self.centralwidget)
        self.FrameBar.setObjectName(u"FrameBar")
        self.FrameBar.setMaximumSize(QSize(16777215, 40))
        self.FrameBar.setStyleSheet(u"#FrameBar{\n"
"	background-color: rgb(24, 24, 24);\n"
"}\n"
"\n"
"#FrameBar QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"#FrameBar QPushButton:hover{\n"
"background-color: rgb(97, 97, 97);\n"
"}\n"
"\n"
"#FrameBar QLabel{\n"
"color:White;\n"
"}\n"
"")
        self.FrameBar.setFrameShape(QFrame.StyledPanel)
        self.FrameBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.FrameBar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 1, 0, 1)
        self.bnt_menu = QToolButton(self.FrameBar)
        self.bnt_menu.setObjectName(u"bnt_menu")
        icon = QIcon()
        icon.addFile(u":/icons/feather/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bnt_menu.setIcon(icon)
        self.bnt_menu.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.bnt_menu)

        self.Menu = QLabel(self.FrameBar)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setMinimumSize(QSize(160, 0))
        self.Menu.setMaximumSize(QSize(160, 16777215))
        font = QFont()
        font.setFamily(u"Poppins")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Menu.setFont(font)

        self.horizontalLayout_2.addWidget(self.Menu)

        self.horizontalSpacer = QSpacerItem(483, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.bnt_min = QPushButton(self.FrameBar)
        self.bnt_min.setObjectName(u"bnt_min")
        icon1 = QIcon()
        icon1.addFile(u":/icons/feather/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bnt_min.setIcon(icon1)
        self.bnt_min.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.bnt_min)

        self.bnt_maximize = QPushButton(self.FrameBar)
        self.bnt_maximize.setObjectName(u"bnt_maximize")
        icon2 = QIcon()
        icon2.addFile(u":/icons/feather/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bnt_maximize.setIcon(icon2)
        self.bnt_maximize.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.bnt_maximize)

        self.bnt_minimize = QPushButton(self.FrameBar)
        self.bnt_minimize.setObjectName(u"bnt_minimize")
        icon3 = QIcon()
        icon3.addFile(u":/icons/feather/minimize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bnt_minimize.setIcon(icon3)
        self.bnt_minimize.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.bnt_minimize)

        self.bnt_close = QPushButton(self.FrameBar)
        self.bnt_close.setObjectName(u"bnt_close")
        icon4 = QIcon()
        icon4.addFile(u":/icons/feather/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bnt_close.setIcon(icon4)
        self.bnt_close.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.bnt_close)


        self.verticalLayout.addWidget(self.FrameBar)

        self.FrameInf = QFrame(self.centralwidget)
        self.FrameInf.setObjectName(u"FrameInf")
        self.FrameInf.setMinimumSize(QSize(0, 0))
        self.FrameInf.setFrameShape(QFrame.StyledPanel)
        self.FrameInf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.FrameInf)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.FrameMenu = QFrame(self.FrameInf)
        self.FrameMenu.setObjectName(u"FrameMenu")
        self.FrameMenu.setMinimumSize(QSize(0, 0))
        self.FrameMenu.setMaximumSize(QSize(0, 16777215))
        self.FrameMenu.setStyleSheet(u"#FrameMenu{\n"
"border-image: url(\"E:/Prog/socinpy/soccrate2/Presentacion/img/side.jpg\") 0 0 0 0 stretch stretch  ;\n"
"}\n"
"\n"
"#FrameMenu QPushButton{\n"
"color:white;\n"
"text-align:left;\n"
"padding-left:20px;\n"
"}\n"
"\n"
"#FrameMenu QPushButton:hover{\n"
"background-color:rgba(31, 31, 31, 0.7);\n"
"border-top-left-radius:20px;\n"
"}\n"
"\n"
"")
        self.FrameMenu.setFrameShape(QFrame.StyledPanel)
        self.FrameMenu.setFrameShadow(QFrame.Raised)
        self.FrameMenu.setLineWidth(1)
        self.verticalLayout_3 = QVBoxLayout(self.FrameMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.label_4 = QLabel(self.FrameMenu)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setFamily(u"Poppins")
        font1.setPointSize(17)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.SubFrameMenu = QFrame(self.FrameMenu)
        self.SubFrameMenu.setObjectName(u"SubFrameMenu")
        self.SubFrameMenu.setMinimumSize(QSize(250, 0))
        self.SubFrameMenu.setFrameShape(QFrame.StyledPanel)
        self.SubFrameMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.SubFrameMenu)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 20, 0, 0)
        self.btn_inicio = QPushButton(self.SubFrameMenu)
        self.btn_inicio.setObjectName(u"btn_inicio")
        self.btn_inicio.setMinimumSize(QSize(250, 40))
        font2 = QFont()
        font2.setFamily(u"Poppins")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.btn_inicio.setFont(font2)
        self.btn_inicio.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/feather/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_inicio.setIcon(icon5)
        self.btn_inicio.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.btn_inicio)

        self.btn_clientes = QPushButton(self.SubFrameMenu)
        self.btn_clientes.setObjectName(u"btn_clientes")
        self.btn_clientes.setMinimumSize(QSize(250, 40))
        self.btn_clientes.setFont(font2)
        icon6 = QIcon()
        icon6.addFile(u":/icons/feather/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clientes.setIcon(icon6)
        self.btn_clientes.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.btn_clientes)

        self.btn_graph = QPushButton(self.SubFrameMenu)
        self.btn_graph.setObjectName(u"btn_graph")
        self.btn_graph.setMinimumSize(QSize(250, 40))
        self.btn_graph.setFont(font2)
        icon7 = QIcon()
        icon7.addFile(u":/icons/feather/pie-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_graph.setIcon(icon7)
        self.btn_graph.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.btn_graph)

        self.btn_informes = QPushButton(self.SubFrameMenu)
        self.btn_informes.setObjectName(u"btn_informes")
        self.btn_informes.setMinimumSize(QSize(250, 40))
        font3 = QFont()
        font3.setFamily(u"Poppins")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.btn_informes.setFont(font3)
        icon8 = QIcon()
        icon8.addFile(u":/icons/feather/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_informes.setIcon(icon8)
        self.btn_informes.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.btn_informes)

        self.verticalSpacer = QSpacerItem(20, 308, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.btn_config = QPushButton(self.SubFrameMenu)
        self.btn_config.setObjectName(u"btn_config")
        self.btn_config.setMinimumSize(QSize(250, 40))
        self.btn_config.setFont(font2)
        self.btn_config.setLayoutDirection(Qt.LeftToRight)
        icon9 = QIcon()
        icon9.addFile(u":/icons/feather/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_config.setIcon(icon9)
        self.btn_config.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.btn_config, 0, Qt.AlignLeft)

        self.btn_help = QPushButton(self.SubFrameMenu)
        self.btn_help.setObjectName(u"btn_help")
        self.btn_help.setMinimumSize(QSize(250, 40))
        self.btn_help.setFont(font2)
        icon10 = QIcon()
        icon10.addFile(u":/icons/feather/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_help.setIcon(icon10)
        self.btn_help.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.btn_help, 0, Qt.AlignLeft)

        self.Footer = QFrame(self.SubFrameMenu)
        self.Footer.setObjectName(u"Footer")
        self.Footer.setMinimumSize(QSize(0, 100))
        self.Footer.setFrameShape(QFrame.StyledPanel)
        self.Footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.Footer)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_6)

        self.label_2 = QLabel(self.Footer)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setPixmap(QPixmap(u":/img/img/logo.png"))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_2, 0, Qt.AlignBottom)

        self.label = QLabel(self.Footer)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamily(u"Poppins")
        self.label.setFont(font4)
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_9.addWidget(self.label, 0, Qt.AlignBottom)


        self.verticalLayout_4.addWidget(self.Footer, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.SubFrameMenu, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.FrameMenu)

        self.FrameContent = QFrame(self.FrameInf)
        self.FrameContent.setObjectName(u"FrameContent")
        self.FrameContent.setMinimumSize(QSize(0, 0))
        self.FrameContent.setMaximumSize(QSize(16777215, 16777215))
        self.FrameContent.setStyleSheet(u"")
        self.FrameContent.setFrameShape(QFrame.StyledPanel)
        self.FrameContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.FrameContent)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.FrameSubMenu = QFrame(self.FrameContent)
        self.FrameSubMenu.setObjectName(u"FrameSubMenu")
        self.FrameSubMenu.setMinimumSize(QSize(0, 0))
        self.FrameSubMenu.setFrameShape(QFrame.StyledPanel)
        self.FrameSubMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.FrameSubMenu)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.FrameClientes = QFrame(self.FrameSubMenu)
        self.FrameClientes.setObjectName(u"FrameClientes")
        self.FrameClientes.setMinimumSize(QSize(0, 260))
        self.FrameClientes.setMaximumSize(QSize(0, 260))
        self.FrameClientes.setStyleSheet(u"#FrameClientes{\n"
"background-color:rgb(61, 61, 61);\n"
"border-bottom-left-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"}\n"
"\n"
"#FrameTittle{\n"
"background-color:#ed4124;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#FrameTittle QLabel{\n"
"color:white;\n"
"}\n"
"\n"
"#FrameButtons QPushButton{\n"
"color:white;\n"
"background-color:rgb(45, 45, 45);\n"
"border-top-right-radius:20px;\n"
"border-top-left-radius:20px;\n"
"}\n"
"\n"
"#FrameButtons QPushButton:hover{\n"
"background-color: white;\n"
"color:black;\n"
"}")
        self.FrameClientes.setFrameShape(QFrame.StyledPanel)
        self.FrameClientes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.FrameClientes)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 0)
        self.FrameTittle = QFrame(self.FrameClientes)
        self.FrameTittle.setObjectName(u"FrameTittle")
        self.FrameTittle.setMinimumSize(QSize(0, 40))
        self.FrameTittle.setMaximumSize(QSize(16777215, 40))
        self.FrameTittle.setFrameShape(QFrame.StyledPanel)
        self.FrameTittle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.FrameTittle)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.label_9 = QLabel(self.FrameTittle)
        self.label_9.setObjectName(u"label_9")
        font5 = QFont()
        font5.setFamily(u"Poppins")
        font5.setPointSize(14)
        self.label_9.setFont(font5)
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_9)

        self.btn_closecli = QPushButton(self.FrameTittle)
        self.btn_closecli.setObjectName(u"btn_closecli")
        icon11 = QIcon()
        icon11.addFile(u":/icons/feather/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_closecli.setIcon(icon11)
        self.btn_closecli.setIconSize(QSize(28, 28))

        self.horizontalLayout_4.addWidget(self.btn_closecli, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.FrameTittle)

        self.FrameButtons = QFrame(self.FrameClientes)
        self.FrameButtons.setObjectName(u"FrameButtons")
        self.FrameButtons.setMinimumSize(QSize(0, 40))
        self.FrameButtons.setMaximumSize(QSize(16777215, 16777215))
        self.FrameButtons.setFont(font5)
        self.FrameButtons.setFrameShape(QFrame.StyledPanel)
        self.FrameButtons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.FrameButtons)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.btn_addcli = QPushButton(self.FrameButtons)
        self.btn_addcli.setObjectName(u"btn_addcli")
        self.btn_addcli.setFont(font5)

        self.verticalLayout_6.addWidget(self.btn_addcli)

        self.btn_listcli = QPushButton(self.FrameButtons)
        self.btn_listcli.setObjectName(u"btn_listcli")
        self.btn_listcli.setFont(font5)

        self.verticalLayout_6.addWidget(self.btn_listcli)

        self.btn_hashes = QPushButton(self.FrameButtons)
        self.btn_hashes.setObjectName(u"btn_hashes")
        self.btn_hashes.setFont(font5)

        self.verticalLayout_6.addWidget(self.btn_hashes)


        self.verticalLayout_2.addWidget(self.FrameButtons)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.verticalLayout_10.addWidget(self.FrameClientes, 0, Qt.AlignTop)

        self.FrameInformes = QFrame(self.FrameSubMenu)
        self.FrameInformes.setObjectName(u"FrameInformes")
        self.FrameInformes.setMinimumSize(QSize(0, 200))
        self.FrameInformes.setMaximumSize(QSize(0, 200))
        self.FrameInformes.setStyleSheet(u"#FrameInformes{\n"
"background-color:rgb(61, 61, 61);\n"
"border-bottom-left-radius:15px;\n"
"border-bottom-right-radius:15px;\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:15px;\n"
"}\n"
"\n"
"#FrameTittle_3{\n"
"background-color:#ed4124;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#FrameTittle_3 QLabel{\n"
"color:white;\n"
"}\n"
"\n"
"#FrameButtons_4 QPushButton{\n"
"color:white;\n"
"background-color:rgb(45, 45, 45);\n"
"border-top-right-radius:20px;\n"
"border-top-left-radius:20px;\n"
"}\n"
"\n"
"#FrameButtons_4 QPushButton:hover{\n"
"background-color: white;\n"
"color:black;\n"
"}")
        self.FrameInformes.setFrameShape(QFrame.StyledPanel)
        self.FrameInformes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.FrameInformes)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(5, 5, 5, 0)
        self.FrameTittle_3 = QFrame(self.FrameInformes)
        self.FrameTittle_3.setObjectName(u"FrameTittle_3")
        self.FrameTittle_3.setMinimumSize(QSize(0, 40))
        self.FrameTittle_3.setFrameShape(QFrame.StyledPanel)
        self.FrameTittle_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.FrameTittle_3)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(10, 0, 10, 0)
        self.label_53 = QLabel(self.FrameTittle_3)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font5)

        self.horizontalLayout_62.addWidget(self.label_53)

        self.btn_closeinf = QPushButton(self.FrameTittle_3)
        self.btn_closeinf.setObjectName(u"btn_closeinf")
        self.btn_closeinf.setIcon(icon11)
        self.btn_closeinf.setIconSize(QSize(28, 28))

        self.horizontalLayout_62.addWidget(self.btn_closeinf, 0, Qt.AlignRight)


        self.verticalLayout_54.addWidget(self.FrameTittle_3)

        self.verticalSpacer_43 = QSpacerItem(20, 29, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_54.addItem(self.verticalSpacer_43)

        self.FrameButtons_4 = QWidget(self.FrameInformes)
        self.FrameButtons_4.setObjectName(u"FrameButtons_4")
        self.verticalLayout_47 = QVBoxLayout(self.FrameButtons_4)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.btn_crear_infor = QPushButton(self.FrameButtons_4)
        self.btn_crear_infor.setObjectName(u"btn_crear_infor")
        self.btn_crear_infor.setFont(font5)

        self.verticalLayout_47.addWidget(self.btn_crear_infor)

        self.btn_abrir_infor = QPushButton(self.FrameButtons_4)
        self.btn_abrir_infor.setObjectName(u"btn_abrir_infor")
        self.btn_abrir_infor.setFont(font5)

        self.verticalLayout_47.addWidget(self.btn_abrir_infor)

        self.btn_abrir_csv_2 = QPushButton(self.FrameButtons_4)
        self.btn_abrir_csv_2.setObjectName(u"btn_abrir_csv_2")
        self.btn_abrir_csv_2.setFont(font5)

        self.verticalLayout_47.addWidget(self.btn_abrir_csv_2)


        self.verticalLayout_54.addWidget(self.FrameButtons_4)

        self.verticalSpacer_44 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_54.addItem(self.verticalSpacer_44)

        self.FrameButtons_4.raise_()
        self.FrameTittle_3.raise_()

        self.verticalLayout_10.addWidget(self.FrameInformes, 0, Qt.AlignVCenter)

        self.FrameConfig = QFrame(self.FrameSubMenu)
        self.FrameConfig.setObjectName(u"FrameConfig")
        self.FrameConfig.setMinimumSize(QSize(0, 275))
        self.FrameConfig.setMaximumSize(QSize(0, 275))
        self.FrameConfig.setStyleSheet(u"#FrameConfig{\n"
"background-color:rgb(61, 61, 61);\n"
"border-top-left-radius:15px;\n"
"border-top-right-radius:15px;\n"
"}\n"
"\n"
"#FrameTittle_2{\n"
"background-color:#ed4124;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#FrameTittle_2 QLabel{\n"
"color:white;\n"
"}\n"
"\n"
"#FrameButtons_2 QPushButton{\n"
"color:white;\n"
"background-color:rgb(45, 45, 45);\n"
"border-top-right-radius:20px;\n"
"border-top-left-radius:20px;\n"
"}\n"
"\n"
"#FrameButtons_2 QPushButton:hover{\n"
"background-color: white;\n"
"color:black;\n"
"}")
        self.FrameConfig.setFrameShape(QFrame.StyledPanel)
        self.FrameConfig.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.FrameConfig)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 0)
        self.FrameTittle_2 = QFrame(self.FrameConfig)
        self.FrameTittle_2.setObjectName(u"FrameTittle_2")
        self.FrameTittle_2.setMinimumSize(QSize(0, 40))
        self.FrameTittle_2.setMaximumSize(QSize(16777215, 40))
        self.FrameTittle_2.setFrameShape(QFrame.StyledPanel)
        self.FrameTittle_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.FrameTittle_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 10, 0)
        self.label_12 = QLabel(self.FrameTittle_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font5)
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_12)

        self.btn_closeconf = QPushButton(self.FrameTittle_2)
        self.btn_closeconf.setObjectName(u"btn_closeconf")
        self.btn_closeconf.setIcon(icon11)
        self.btn_closeconf.setIconSize(QSize(28, 28))

        self.horizontalLayout_5.addWidget(self.btn_closeconf, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.FrameTittle_2)

        self.verticalSpacer_5 = QSpacerItem(20, 64, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)

        self.FrameButtons_2 = QFrame(self.FrameConfig)
        self.FrameButtons_2.setObjectName(u"FrameButtons_2")
        self.FrameButtons_2.setMinimumSize(QSize(0, 40))
        self.FrameButtons_2.setMaximumSize(QSize(16777215, 16777215))
        self.FrameButtons_2.setFont(font5)
        self.FrameButtons_2.setFrameShape(QFrame.StyledPanel)
        self.FrameButtons_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.FrameButtons_2)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_abrir_logs_2 = QPushButton(self.FrameButtons_2)
        self.btn_abrir_logs_2.setObjectName(u"btn_abrir_logs_2")
        self.btn_abrir_logs_2.setFont(font5)

        self.verticalLayout_7.addWidget(self.btn_abrir_logs_2)

        self.btn_schedule = QPushButton(self.FrameButtons_2)
        self.btn_schedule.setObjectName(u"btn_schedule")
        self.btn_schedule.setFont(font5)

        self.verticalLayout_7.addWidget(self.btn_schedule)

        self.btn_conexion = QPushButton(self.FrameButtons_2)
        self.btn_conexion.setObjectName(u"btn_conexion")
        self.btn_conexion.setFont(font5)

        self.verticalLayout_7.addWidget(self.btn_conexion)

        self.btn_email = QPushButton(self.FrameButtons_2)
        self.btn_email.setObjectName(u"btn_email")
        self.btn_email.setFont(font5)

        self.verticalLayout_7.addWidget(self.btn_email)


        self.verticalLayout_8.addWidget(self.FrameButtons_2)

        self.verticalSpacer_4 = QSpacerItem(20, 63, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)


        self.verticalLayout_10.addWidget(self.FrameConfig, 0, Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.FrameSubMenu)

        self.FrameStacked = QFrame(self.FrameContent)
        self.FrameStacked.setObjectName(u"FrameStacked")
        self.FrameStacked.setFrameShape(QFrame.StyledPanel)
        self.FrameStacked.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.FrameStacked)
        self.horizontalLayout_88.setSpacing(0)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.FrameStacked)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget.setStyleSheet(u"#FrameContent{\n"
"border-image: url(\"E:/Prog/socinpy/soccrate2/Presentacion/img/side.jpg\") 0 0 0 0 stretch stretch  ;\n"
"}")
        self.version = QWidget()
        self.version.setObjectName(u"version")
        self.gridLayout = QGridLayout(self.version)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_7 = QSpacerItem(20, 230, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(317, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.tittlesoc = QWidget(self.version)
        self.tittlesoc.setObjectName(u"tittlesoc")
        self.tittlesoc.setStyleSheet(u"#tittle1{\n"
"background-color: rgba(58, 58, 58, 0.8);\n"
"}\n"
"\n"
"#subtittlever{\n"
"background-color: rgba(77, 77, 77, 0.8);\n"
"}\n"
"\n"
"#tittle1 QLabel {\n"
"color:white;\n"
"}\n"
"\n"
"#subtittlever QLabel {\n"
"color:white;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.tittlesoc)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 0, 0, 0)
        self.tittle1 = QFrame(self.tittlesoc)
        self.tittle1.setObjectName(u"tittle1")
        self.tittle1.setFrameShape(QFrame.StyledPanel)
        self.tittle1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.tittle1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.tittle1)
        self.label_3.setObjectName(u"label_3")
        font6 = QFont()
        font6.setFamily(u"Poppins")
        font6.setPointSize(45)
        self.label_3.setFont(font6)
        self.label_3.setStyleSheet(u"")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_3)


        self.verticalLayout_11.addWidget(self.tittle1)

        self.subtittlever = QFrame(self.tittlesoc)
        self.subtittlever.setObjectName(u"subtittlever")
        self.subtittlever.setFrameShape(QFrame.StyledPanel)
        self.subtittlever.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.subtittlever)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.subtittlever)
        self.label_5.setObjectName(u"label_5")
        font7 = QFont()
        font7.setFamily(u"Poppins")
        font7.setPointSize(30)
        self.label_5.setFont(font7)
        self.label_5.setStyleSheet(u"")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_5)


        self.verticalLayout_11.addWidget(self.subtittlever)


        self.gridLayout.addWidget(self.tittlesoc, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(317, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 229, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_8, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.version)
        self.inicio = QWidget()
        self.inicio.setObjectName(u"inicio")
        self.inicio.setMinimumSize(QSize(0, 0))
        self.gridLayout_2 = QGridLayout(self.inicio)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.FrameContent_Inicio = QWidget(self.inicio)
        self.FrameContent_Inicio.setObjectName(u"FrameContent_Inicio")
        self.FrameContent_Inicio.setMinimumSize(QSize(0, 0))
        self.FrameContent_Inicio.setStyleSheet(u"#FrameContent_Inicio_Sup{\n"
"background-color: rgba(51, 51, 51, 0.8);\n"
"}\n"
"\n"
"#FrameContent_Inicio_Inf{\n"
"background-color: rgba(255, 255, 255, 0.8);\n"
"}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"}\n"
"\n"
"#FrameContent_Inicio QPushButton{\n"
"color:white;\n"
"background-color: rgb(0, 161, 92);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#FrameContent_Inicio QPushButton:hover{\n"
"background-color:rgb(40, 209, 118);\n"
"color: rgb(26, 26, 26);\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.FrameContent_Inicio)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.FrameContent_Inicio_Sup = QFrame(self.FrameContent_Inicio)
        self.FrameContent_Inicio_Sup.setObjectName(u"FrameContent_Inicio_Sup")
        self.FrameContent_Inicio_Sup.setFrameShape(QFrame.StyledPanel)
        self.FrameContent_Inicio_Sup.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.FrameContent_Inicio_Sup)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(178, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.Label_Content_Inicio = QLabel(self.FrameContent_Inicio_Sup)
        self.Label_Content_Inicio.setObjectName(u"Label_Content_Inicio")
        font8 = QFont()
        font8.setFamily(u"Poppins")
        font8.setPointSize(12)
        self.Label_Content_Inicio.setFont(font8)

        self.horizontalLayout_8.addWidget(self.Label_Content_Inicio)

        self.horizontalSpacer_7 = QSpacerItem(177, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout_12.addWidget(self.FrameContent_Inicio_Sup)

        self.FrameContent_Inicio_Inf = QFrame(self.FrameContent_Inicio)
        self.FrameContent_Inicio_Inf.setObjectName(u"FrameContent_Inicio_Inf")
        self.FrameContent_Inicio_Inf.setMinimumSize(QSize(0, 100))
        self.FrameContent_Inicio_Inf.setFrameShape(QFrame.StyledPanel)
        self.FrameContent_Inicio_Inf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.FrameContent_Inicio_Inf)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)

        self.btn_abrir_logs = QPushButton(self.FrameContent_Inicio_Inf)
        self.btn_abrir_logs.setObjectName(u"btn_abrir_logs")
        font9 = QFont()
        font9.setFamily(u"Poppins")
        font9.setPointSize(12)
        font9.setUnderline(False)
        self.btn_abrir_logs.setFont(font9)

        self.horizontalLayout_9.addWidget(self.btn_abrir_logs)

        self.horizontalSpacer_9 = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.btn_abrir_informes = QPushButton(self.FrameContent_Inicio_Inf)
        self.btn_abrir_informes.setObjectName(u"btn_abrir_informes")
        self.btn_abrir_informes.setFont(font8)

        self.horizontalLayout_9.addWidget(self.btn_abrir_informes)

        self.horizontalSpacer_10 = QSpacerItem(64, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)

        self.btn_abrir_csv = QPushButton(self.FrameContent_Inicio_Inf)
        self.btn_abrir_csv.setObjectName(u"btn_abrir_csv")
        self.btn_abrir_csv.setFont(font8)

        self.horizontalLayout_9.addWidget(self.btn_abrir_csv)

        self.horizontalSpacer_11 = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_11)

        self.btn_dashboard = QPushButton(self.FrameContent_Inicio_Inf)
        self.btn_dashboard.setObjectName(u"btn_dashboard")
        self.btn_dashboard.setFont(font8)

        self.horizontalLayout_9.addWidget(self.btn_dashboard)

        self.horizontalSpacer_12 = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_12)


        self.verticalLayout_12.addWidget(self.FrameContent_Inicio_Inf)


        self.gridLayout_2.addWidget(self.FrameContent_Inicio, 2, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(169, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 2, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(168, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 2, 2, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 253, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_9, 1, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 253, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_10, 3, 1, 1, 1)

        self.Tittle_Inicio = QLabel(self.inicio)
        self.Tittle_Inicio.setObjectName(u"Tittle_Inicio")
        self.Tittle_Inicio.setMinimumSize(QSize(0, 45))
        font10 = QFont()
        font10.setFamily(u"Poppins")
        font10.setPointSize(16)
        self.Tittle_Inicio.setFont(font10)
        self.Tittle_Inicio.setStyleSheet(u"#Tittle_Inicio{\n"
"background-color: rgb(237, 65, 36);\n"
"color:white;\n"
"border: 1px solid black;\n"
"}\n"
"")
        self.Tittle_Inicio.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.Tittle_Inicio, 0, 0, 1, 3)

        self.stackedWidget.addWidget(self.inicio)
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.gridLayout_13 = QGridLayout(self.dashboard)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_37 = QSpacerItem(20, 51, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_37, 1, 2, 1, 1)

        self.scrollArea = QScrollArea(self.dashboard)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(1250, 600))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setStyleSheet(u"#ScrollContents_Dashboard{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#FrameDash_Tittle{\n"
"background-color: rgb(51, 51, 51);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"}\n"
"\n"
"#Barras_Tittle{\n"
"background-color: rgb(51, 51, 51);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"}\n"
"\n"
"#Barras_Tittle_2{\n"
"background-color: rgb(51, 51, 51);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"}\n"
"\n"
"#Torta_Tittle{\n"
"background-color: rgb(51, 51, 51);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"padding:5px;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: rgb(217, 217, 217);\n"
"    border: none;\n"
"    selection-background-color: rgba(51, 51, 51, 0.5);\n"
"    outline: no"
                        "ne;\n"
"}\n"
"\n"
"QPushButton{\n"
"color:white;\n"
"background-color: rgb(0, 161, 92);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(40, 209, 118);\n"
"color: rgb(26, 26, 26);\n"
"}\n"
"\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.ScrollContents_Dashboard = QWidget()
        self.ScrollContents_Dashboard.setObjectName(u"ScrollContents_Dashboard")
        self.ScrollContents_Dashboard.setGeometry(QRect(0, 0, 1233, 1093))
        self.verticalLayout_53 = QVBoxLayout(self.ScrollContents_Dashboard)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.FrameDashCont_Histo = QFrame(self.ScrollContents_Dashboard)
        self.FrameDashCont_Histo.setObjectName(u"FrameDashCont_Histo")
        self.FrameDashCont_Histo.setFrameShape(QFrame.StyledPanel)
        self.FrameDashCont_Histo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.FrameDashCont_Histo)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalSpacer_54 = QSpacerItem(135, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_54)

        self.FrameDash_Histo = QFrame(self.FrameDashCont_Histo)
        self.FrameDash_Histo.setObjectName(u"FrameDash_Histo")
        self.FrameDash_Histo.setStyleSheet(u"")
        self.FrameDash_Histo.setFrameShape(QFrame.StyledPanel)
        self.FrameDash_Histo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.FrameDash_Histo)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.FrameDash_Tittle = QFrame(self.FrameDash_Histo)
        self.FrameDash_Tittle.setObjectName(u"FrameDash_Tittle")
        self.FrameDash_Tittle.setMinimumSize(QSize(0, 40))
        self.FrameDash_Tittle.setFrameShape(QFrame.StyledPanel)
        self.FrameDash_Tittle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.FrameDash_Tittle)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_48 = QLabel(self.FrameDash_Tittle)
        self.label_48.setObjectName(u"label_48")
        font11 = QFont()
        font11.setFamily(u"Poppins")
        font11.setPointSize(11)
        self.label_48.setFont(font11)
        self.label_48.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.label_48)


        self.verticalLayout_41.addWidget(self.FrameDash_Tittle)

        self.FrameDash_ContentHisto = QFrame(self.FrameDash_Histo)
        self.FrameDash_ContentHisto.setObjectName(u"FrameDash_ContentHisto")
        self.FrameDash_ContentHisto.setFrameShape(QFrame.StyledPanel)
        self.FrameDash_ContentHisto.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.FrameDash_ContentHisto)
        self.horizontalLayout_53.setSpacing(10)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.FrameDash_Histo_Izq = QFrame(self.FrameDash_ContentHisto)
        self.FrameDash_Histo_Izq.setObjectName(u"FrameDash_Histo_Izq")
        self.FrameDash_Histo_Izq.setMinimumSize(QSize(0, 400))
        self.FrameDash_Histo_Izq.setMaximumSize(QSize(650, 400))
        self.FrameDash_Histo_Izq.setFrameShape(QFrame.StyledPanel)
        self.FrameDash_Histo_Izq.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.FrameDash_Histo_Izq)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.Frame_Histo = QFrame(self.FrameDash_Histo_Izq)
        self.Frame_Histo.setObjectName(u"Frame_Histo")
        self.Frame_Histo.setMinimumSize(QSize(600, 400))
        self.Frame_Histo.setMaximumSize(QSize(600, 400))
        self.Frame_Histo.setFrameShape(QFrame.StyledPanel)
        self.Frame_Histo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.Frame_Histo)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.Label_Histo = QLabel(self.Frame_Histo)
        self.Label_Histo.setObjectName(u"Label_Histo")
        self.Label_Histo.setMinimumSize(QSize(0, 400))
        self.Label_Histo.setMaximumSize(QSize(650, 400))
        self.Label_Histo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_40.addWidget(self.Label_Histo)


        self.horizontalLayout_52.addWidget(self.Frame_Histo)


        self.horizontalLayout_53.addWidget(self.FrameDash_Histo_Izq)

        self.FrameDash_Histo_Der = QFrame(self.FrameDash_ContentHisto)
        self.FrameDash_Histo_Der.setObjectName(u"FrameDash_Histo_Der")
        self.FrameDash_Histo_Der.setMinimumSize(QSize(300, 0))
        self.FrameDash_Histo_Der.setFrameShape(QFrame.StyledPanel)
        self.FrameDash_Histo_Der.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.FrameDash_Histo_Der)
        self.verticalLayout_39.setSpacing(10)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, -1, 0)
        self.verticalSpacer_40 = QSpacerItem(20, 21, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_40)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(-1, 10, -1, -1)
        self.label_52 = QLabel(self.FrameDash_Histo_Der)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font11)

        self.horizontalLayout_51.addWidget(self.label_52)

        self.histo_client_combo = QComboBox(self.FrameDash_Histo_Der)
        self.histo_client_combo.setObjectName(u"histo_client_combo")
        self.histo_client_combo.setMinimumSize(QSize(150, 0))
        font12 = QFont()
        font12.setFamily(u"Poppins")
        font12.setPointSize(10)
        self.histo_client_combo.setFont(font12)

        self.horizontalLayout_51.addWidget(self.histo_client_combo)


        self.verticalLayout_39.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_51 = QLabel(self.FrameDash_Histo_Der)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font11)

        self.horizontalLayout_50.addWidget(self.label_51)

        self.histo_tdato_combo = QComboBox(self.FrameDash_Histo_Der)
        self.histo_tdato_combo.addItem("")
        self.histo_tdato_combo.addItem("")
        self.histo_tdato_combo.addItem("")
        self.histo_tdato_combo.setObjectName(u"histo_tdato_combo")
        self.histo_tdato_combo.setMinimumSize(QSize(150, 0))
        self.histo_tdato_combo.setFont(font12)

        self.horizontalLayout_50.addWidget(self.histo_tdato_combo)


        self.verticalLayout_39.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setSpacing(6)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_50 = QLabel(self.FrameDash_Histo_Der)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font11)

        self.horizontalLayout_49.addWidget(self.label_50)

        self.histo_column_combo = QComboBox(self.FrameDash_Histo_Der)
        self.histo_column_combo.setObjectName(u"histo_column_combo")
        self.histo_column_combo.setMinimumSize(QSize(150, 0))
        self.histo_column_combo.setFont(font12)

        self.horizontalLayout_49.addWidget(self.histo_column_combo)


        self.verticalLayout_39.addLayout(self.horizontalLayout_49)

        self.fi_histo = QFrame(self.FrameDash_Histo_Der)
        self.fi_histo.setObjectName(u"fi_histo")
        self.fi_histo.setFrameShape(QFrame.StyledPanel)
        self.fi_histo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.fi_histo)
        self.horizontalLayout_80.setSpacing(0)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.label_59 = QLabel(self.fi_histo)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font11)

        self.horizontalLayout_80.addWidget(self.label_59)

        self.fi_dash_histo = QDateEdit(self.fi_histo)
        self.fi_dash_histo.setObjectName(u"fi_dash_histo")
        self.fi_dash_histo.setMinimumSize(QSize(150, 35))
        self.fi_dash_histo.setFont(font12)
        self.fi_dash_histo.setStyleSheet(u"QCalendarWidget {\n"
"    background-color: rgb(165, 165, 165);\n"
"}\n"
"\n"
"QCalendarWidget QTableView {\n"
"    background-color:rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: white;\n"
"	font-size: 12px;\n"
"	background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"	width: 150px;\n"
"	left: 20px;\n"
"	color: white;\n"
"	font-size: 15px;\n"
"	background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"	background-color:  rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"")
        self.fi_dash_histo.setCalendarPopup(True)
        self.fi_dash_histo.setDate(QDate(2023, 1, 1))

        self.horizontalLayout_80.addWidget(self.fi_dash_histo)


        self.verticalLayout_39.addWidget(self.fi_histo)

        self.ff_histo = QFrame(self.FrameDash_Histo_Der)
        self.ff_histo.setObjectName(u"ff_histo")
        self.ff_histo.setFrameShape(QFrame.StyledPanel)
        self.ff_histo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.ff_histo)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.label_60 = QLabel(self.ff_histo)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font11)

        self.horizontalLayout_81.addWidget(self.label_60)

        self.ff_dash_histo = QDateEdit(self.ff_histo)
        self.ff_dash_histo.setObjectName(u"ff_dash_histo")
        self.ff_dash_histo.setMinimumSize(QSize(150, 35))
        self.ff_dash_histo.setFont(font12)
        self.ff_dash_histo.setStyleSheet(u"QCalendarWidget {\n"
"    background-color: rgb(165, 165, 165);\n"
"}\n"
"\n"
"QCalendarWidget QTableView {\n"
"    background-color:rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: white;\n"
"	font-size: 12px;\n"
"	background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"	width: 150px;\n"
"	left: 20px;\n"
"	color: white;\n"
"	font-size: 15px;\n"
"	background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"	background-color:  rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"")
        self.ff_dash_histo.setCalendarPopup(True)
        self.ff_dash_histo.setDate(QDate(2023, 1, 1))

        self.horizontalLayout_81.addWidget(self.ff_dash_histo)


        self.verticalLayout_39.addWidget(self.ff_histo)

        self.TOCAME = QPushButton(self.FrameDash_Histo_Der)
        self.TOCAME.setObjectName(u"TOCAME")

        self.verticalLayout_39.addWidget(self.TOCAME)

        self.verticalSpacer_39 = QSpacerItem(20, 22, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_39.addItem(self.verticalSpacer_39)


        self.horizontalLayout_53.addWidget(self.FrameDash_Histo_Der)


        self.verticalLayout_41.addWidget(self.FrameDash_ContentHisto)

        self.FrameDash_ContentHisto.raise_()
        self.FrameDash_Tittle.raise_()

        self.horizontalLayout_59.addWidget(self.FrameDash_Histo)

        self.horizontalSpacer_55 = QSpacerItem(83, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_55)


        self.verticalLayout_53.addWidget(self.FrameDashCont_Histo)

        self.FrameDash_Barras = QFrame(self.ScrollContents_Dashboard)
        self.FrameDash_Barras.setObjectName(u"FrameDash_Barras")
        self.FrameDash_Barras.setFrameShape(QFrame.StyledPanel)
        self.FrameDash_Barras.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.FrameDash_Barras)
        self.horizontalLayout_64.setSpacing(0)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.Barras1 = QFrame(self.FrameDash_Barras)
        self.Barras1.setObjectName(u"Barras1")
        self.Barras1.setMinimumSize(QSize(600, 300))
        self.Barras1.setMaximumSize(QSize(600, 300))
        self.Barras1.setStyleSheet(u"")
        self.Barras1.setFrameShape(QFrame.StyledPanel)
        self.Barras1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.Barras1)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.Barras_Tittle = QFrame(self.Barras1)
        self.Barras_Tittle.setObjectName(u"Barras_Tittle")
        self.Barras_Tittle.setMinimumSize(QSize(0, 40))
        self.Barras_Tittle.setMaximumSize(QSize(16777215, 40))
        self.Barras_Tittle.setFrameShape(QFrame.StyledPanel)
        self.Barras_Tittle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.Barras_Tittle)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_49 = QLabel(self.Barras_Tittle)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font11)
        self.label_49.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_54.addWidget(self.label_49)


        self.verticalLayout_43.addWidget(self.Barras_Tittle)

        self.Barras1_Content = QFrame(self.Barras1)
        self.Barras1_Content.setObjectName(u"Barras1_Content")
        self.Barras1_Content.setMinimumSize(QSize(400, 0))
        self.Barras1_Content.setFrameShape(QFrame.StyledPanel)
        self.Barras1_Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.Barras1_Content)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.Barras1_Content_Izq = QFrame(self.Barras1_Content)
        self.Barras1_Content_Izq.setObjectName(u"Barras1_Content_Izq")
        self.Barras1_Content_Izq.setFrameShape(QFrame.StyledPanel)
        self.Barras1_Content_Izq.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.Barras1_Content_Izq)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.Label_Barras1 = QLabel(self.Barras1_Content_Izq)
        self.Label_Barras1.setObjectName(u"Label_Barras1")
        self.Label_Barras1.setMaximumSize(QSize(320, 300))
        self.Label_Barras1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_46.addWidget(self.Label_Barras1)


        self.horizontalLayout_63.addWidget(self.Barras1_Content_Izq)

        self.Barras1_Content_Der = QFrame(self.Barras1_Content)
        self.Barras1_Content_Der.setObjectName(u"Barras1_Content_Der")
        self.Barras1_Content_Der.setMaximumSize(QSize(280, 16777215))
        self.Barras1_Content_Der.setFrameShape(QFrame.StyledPanel)
        self.Barras1_Content_Der.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.Barras1_Content_Der)
        self.verticalLayout_42.setSpacing(10)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_42 = QSpacerItem(20, 55, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_42.addItem(self.verticalSpacer_42)

        self.f1_2 = QFrame(self.Barras1_Content_Der)
        self.f1_2.setObjectName(u"f1_2")
        self.f1_2.setFrameShape(QFrame.StyledPanel)
        self.f1_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.f1_2)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.f1_2)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMaximumSize(QSize(100, 16777215))
        self.label_54.setFont(font11)

        self.horizontalLayout_56.addWidget(self.label_54)

        self.barras1_client_combo = QComboBox(self.f1_2)
        self.barras1_client_combo.setObjectName(u"barras1_client_combo")
        self.barras1_client_combo.setMinimumSize(QSize(120, 0))
        self.barras1_client_combo.setMaximumSize(QSize(16777215, 16777215))
        self.barras1_client_combo.setFont(font12)

        self.horizontalLayout_56.addWidget(self.barras1_client_combo)


        self.verticalLayout_42.addWidget(self.f1_2)

        self.f2_2 = QFrame(self.Barras1_Content_Der)
        self.f2_2.setObjectName(u"f2_2")
        self.f2_2.setFrameShape(QFrame.StyledPanel)
        self.f2_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.f2_2)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_55 = QLabel(self.f2_2)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMaximumSize(QSize(100, 16777215))
        self.label_55.setFont(font11)

        self.horizontalLayout_57.addWidget(self.label_55)

        self.barras1_tdato_combo = QComboBox(self.f2_2)
        self.barras1_tdato_combo.setObjectName(u"barras1_tdato_combo")
        self.barras1_tdato_combo.setMinimumSize(QSize(120, 0))
        self.barras1_tdato_combo.setMaximumSize(QSize(16777215, 120))
        self.barras1_tdato_combo.setFont(font12)

        self.horizontalLayout_57.addWidget(self.barras1_tdato_combo)


        self.verticalLayout_42.addWidget(self.f2_2)

        self.f3_2 = QFrame(self.Barras1_Content_Der)
        self.f3_2.setObjectName(u"f3_2")
        self.f3_2.setFrameShape(QFrame.StyledPanel)
        self.f3_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.f3_2)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_56 = QLabel(self.f3_2)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMaximumSize(QSize(100, 16777215))
        self.label_56.setFont(font11)

        self.horizontalLayout_58.addWidget(self.label_56)

        self.barras1_column_combo = QComboBox(self.f3_2)
        self.barras1_column_combo.setObjectName(u"barras1_column_combo")
        self.barras1_column_combo.setMinimumSize(QSize(120, 0))
        self.barras1_column_combo.setMaximumSize(QSize(16777215, 120))
        self.barras1_column_combo.setFont(font12)

        self.horizontalLayout_58.addWidget(self.barras1_column_combo)


        self.verticalLayout_42.addWidget(self.f3_2)

        self.fi_bar_1 = QFrame(self.Barras1_Content_Der)
        self.fi_bar_1.setObjectName(u"fi_bar_1")
        self.fi_bar_1.setFrameShape(QFrame.StyledPanel)
        self.fi_bar_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.fi_bar_1)
        self.horizontalLayout_82.setSpacing(0)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.label_61 = QLabel(self.fi_bar_1)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMaximumSize(QSize(100, 16777215))
        self.label_61.setFont(font11)

        self.horizontalLayout_82.addWidget(self.label_61)

        self.fi_dash_bar1 = QDateEdit(self.fi_bar_1)
        self.fi_dash_bar1.setObjectName(u"fi_dash_bar1")
        self.fi_dash_bar1.setMinimumSize(QSize(120, 0))
        self.fi_dash_bar1.setFont(font12)
        self.fi_dash_bar1.setStyleSheet(u"QCalendarWidget {\n"
"    background-color: rgb(165, 165, 165);\n"
"}\n"
"\n"
"QCalendarWidget QTableView {\n"
"    background-color:rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: white;\n"
"	font-size: 12px;\n"
"	background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"	width: 150px;\n"
"	left: 20px;\n"
"	color: white;\n"
"	font-size: 15px;\n"
"	background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"	background-color:  rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}")
        self.fi_dash_bar1.setCalendarPopup(True)
        self.fi_dash_bar1.setDate(QDate(2023, 1, 1))

        self.horizontalLayout_82.addWidget(self.fi_dash_bar1)


        self.verticalLayout_42.addWidget(self.fi_bar_1)

        self.ff_bar1 = QFrame(self.Barras1_Content_Der)
        self.ff_bar1.setObjectName(u"ff_bar1")
        self.ff_bar1.setFrameShape(QFrame.StyledPanel)
        self.ff_bar1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.ff_bar1)
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.label_68 = QLabel(self.ff_bar1)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMaximumSize(QSize(100, 16777215))
        self.label_68.setFont(font11)

        self.horizontalLayout_83.addWidget(self.label_68)

        self.ff_dash_bar1 = QDateEdit(self.ff_bar1)
        self.ff_dash_bar1.setObjectName(u"ff_dash_bar1")
        self.ff_dash_bar1.setMinimumSize(QSize(120, 35))
        self.ff_dash_bar1.setFont(font12)
        self.ff_dash_bar1.setStyleSheet(u"QCalendarWidget {\n"
"    background-color: rgb(165, 165, 165);\n"
"}\n"
"\n"
"QCalendarWidget QTableView {\n"
"    background-color:rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: white;\n"
"	font-size: 12px;\n"
"	background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"	width: 150px;\n"
"	left: 20px;\n"
"	color: white;\n"
"	font-size: 15px;\n"
"	background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"	background-color:  rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"")
        self.ff_dash_bar1.setCalendarPopup(True)
        self.ff_dash_bar1.setDate(QDate(2023, 1, 1))

        self.horizontalLayout_83.addWidget(self.ff_dash_bar1)


        self.verticalLayout_42.addWidget(self.ff_bar1)

        self.barras1 = QPushButton(self.Barras1_Content_Der)
        self.barras1.setObjectName(u"barras1")

        self.verticalLayout_42.addWidget(self.barras1)

        self.verticalSpacer_41 = QSpacerItem(20, 54, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_42.addItem(self.verticalSpacer_41)


        self.horizontalLayout_63.addWidget(self.Barras1_Content_Der)


        self.verticalLayout_43.addWidget(self.Barras1_Content)


        self.horizontalLayout_64.addWidget(self.Barras1)

        self.Barras2 = QFrame(self.FrameDash_Barras)
        self.Barras2.setObjectName(u"Barras2")
        self.Barras2.setMinimumSize(QSize(600, 0))
        self.Barras2.setMaximumSize(QSize(600, 16777215))
        self.Barras2.setFrameShape(QFrame.StyledPanel)
        self.Barras2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.Barras2)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.Barras_Tittle_2 = QFrame(self.Barras2)
        self.Barras_Tittle_2.setObjectName(u"Barras_Tittle_2")
        self.Barras_Tittle_2.setMinimumSize(QSize(0, 40))
        self.Barras_Tittle_2.setMaximumSize(QSize(16777215, 40))
        self.Barras_Tittle_2.setFrameShape(QFrame.StyledPanel)
        self.Barras_Tittle_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.Barras_Tittle_2)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.Label_Barras = QLabel(self.Barras_Tittle_2)
        self.Label_Barras.setObjectName(u"Label_Barras")
        self.Label_Barras.setMaximumSize(QSize(16777215, 40))
        self.Label_Barras.setFont(font11)
        self.Label_Barras.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_55.addWidget(self.Label_Barras)


        self.verticalLayout_45.addWidget(self.Barras_Tittle_2)

        self.Barras2_Content = QFrame(self.Barras2)
        self.Barras2_Content.setObjectName(u"Barras2_Content")
        self.Barras2_Content.setFrameShape(QFrame.StyledPanel)
        self.Barras2_Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.Barras2_Content)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.Barras2_Content_Izq = QFrame(self.Barras2_Content)
        self.Barras2_Content_Izq.setObjectName(u"Barras2_Content_Izq")
        self.Barras2_Content_Izq.setFrameShape(QFrame.StyledPanel)
        self.Barras2_Content_Izq.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.Barras2_Content_Izq)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.Label_Barras2 = QLabel(self.Barras2_Content_Izq)
        self.Label_Barras2.setObjectName(u"Label_Barras2")
        self.Label_Barras2.setMaximumSize(QSize(320, 300))
        self.Label_Barras2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_48.addWidget(self.Label_Barras2)


        self.horizontalLayout_65.addWidget(self.Barras2_Content_Izq)

        self.Barras2_Content_Der = QFrame(self.Barras2_Content)
        self.Barras2_Content_Der.setObjectName(u"Barras2_Content_Der")
        self.Barras2_Content_Der.setMaximumSize(QSize(280, 16777215))
        self.Barras2_Content_Der.setStyleSheet(u"")
        self.Barras2_Content_Der.setFrameShape(QFrame.StyledPanel)
        self.Barras2_Content_Der.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.Barras2_Content_Der)
        self.verticalLayout_49.setSpacing(10)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_45 = QSpacerItem(20, 55, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_49.addItem(self.verticalSpacer_45)

        self.f1_4 = QFrame(self.Barras2_Content_Der)
        self.f1_4.setObjectName(u"f1_4")
        self.f1_4.setFrameShape(QFrame.StyledPanel)
        self.f1_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.f1_4)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.f1_4)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMaximumSize(QSize(100, 16777215))
        self.label_57.setFont(font11)

        self.horizontalLayout_66.addWidget(self.label_57)

        self.barras2_client_combo = QComboBox(self.f1_4)
        self.barras2_client_combo.setObjectName(u"barras2_client_combo")
        self.barras2_client_combo.setMinimumSize(QSize(120, 0))
        self.barras2_client_combo.setFont(font12)

        self.horizontalLayout_66.addWidget(self.barras2_client_combo)


        self.verticalLayout_49.addWidget(self.f1_4)

        self.f1_5 = QFrame(self.Barras2_Content_Der)
        self.f1_5.setObjectName(u"f1_5")
        self.f1_5.setFrameShape(QFrame.StyledPanel)
        self.f1_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.f1_5)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.label_62 = QLabel(self.f1_5)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMaximumSize(QSize(100, 16777215))
        self.label_62.setFont(font11)

        self.horizontalLayout_67.addWidget(self.label_62)

        self.barras2_tdato_combo = QComboBox(self.f1_5)
        self.barras2_tdato_combo.setObjectName(u"barras2_tdato_combo")
        self.barras2_tdato_combo.setMinimumSize(QSize(120, 0))
        self.barras2_tdato_combo.setFont(font12)

        self.horizontalLayout_67.addWidget(self.barras2_tdato_combo)


        self.verticalLayout_49.addWidget(self.f1_5)

        self.f1_6 = QFrame(self.Barras2_Content_Der)
        self.f1_6.setObjectName(u"f1_6")
        self.f1_6.setFrameShape(QFrame.StyledPanel)
        self.f1_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.f1_6)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.label_63 = QLabel(self.f1_6)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMaximumSize(QSize(100, 16777215))
        self.label_63.setFont(font11)

        self.horizontalLayout_68.addWidget(self.label_63)

        self.barras2_column_combo = QComboBox(self.f1_6)
        self.barras2_column_combo.setObjectName(u"barras2_column_combo")
        self.barras2_column_combo.setMinimumSize(QSize(120, 0))
        self.barras2_column_combo.setFont(font12)

        self.horizontalLayout_68.addWidget(self.barras2_column_combo)


        self.verticalLayout_49.addWidget(self.f1_6)

        self.fi_bar2 = QFrame(self.Barras2_Content_Der)
        self.fi_bar2.setObjectName(u"fi_bar2")
        self.fi_bar2.setFrameShape(QFrame.StyledPanel)
        self.fi_bar2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.fi_bar2)
        self.horizontalLayout_84.setSpacing(0)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.label_69 = QLabel(self.fi_bar2)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMaximumSize(QSize(100, 16777215))
        self.label_69.setFont(font11)

        self.horizontalLayout_84.addWidget(self.label_69)

        self.fi_dash_bar2 = QDateEdit(self.fi_bar2)
        self.fi_dash_bar2.setObjectName(u"fi_dash_bar2")
        self.fi_dash_bar2.setMinimumSize(QSize(120, 0))
        self.fi_dash_bar2.setFont(font12)
        self.fi_dash_bar2.setStyleSheet(u"QCalendarWidget {\n"
"    background-color: rgb(165, 165, 165);\n"
"}\n"
"\n"
"QCalendarWidget QTableView {\n"
"    background-color:rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: white;\n"
"	font-size: 12px;\n"
"	background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"	width: 150px;\n"
"	left: 20px;\n"
"	color: white;\n"
"	font-size: 15px;\n"
"	background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"	background-color:  rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}")
        self.fi_dash_bar2.setCalendarPopup(True)
        self.fi_dash_bar2.setDate(QDate(2023, 1, 1))

        self.horizontalLayout_84.addWidget(self.fi_dash_bar2)


        self.verticalLayout_49.addWidget(self.fi_bar2)

        self.ff_bar2 = QFrame(self.Barras2_Content_Der)
        self.ff_bar2.setObjectName(u"ff_bar2")
        self.ff_bar2.setFrameShape(QFrame.StyledPanel)
        self.ff_bar2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.ff_bar2)
        self.horizontalLayout_85.setSpacing(0)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.label_70 = QLabel(self.ff_bar2)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMaximumSize(QSize(100, 16777215))
        self.label_70.setFont(font11)

        self.horizontalLayout_85.addWidget(self.label_70)

        self.ff_dash_bar2 = QDateEdit(self.ff_bar2)
        self.ff_dash_bar2.setObjectName(u"ff_dash_bar2")
        self.ff_dash_bar2.setMinimumSize(QSize(120, 35))
        self.ff_dash_bar2.setFont(font12)
        self.ff_dash_bar2.setStyleSheet(u"QCalendarWidget {\n"
"    background-color: rgb(165, 165, 165);\n"
"}\n"
"\n"
"QCalendarWidget QTableView {\n"
"    background-color:rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: white;\n"
"	font-size: 12px;\n"
"	background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"	width: 150px;\n"
"	left: 20px;\n"
"	color: white;\n"
"	font-size: 15px;\n"
"	background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"	background-color:  rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"")
        self.ff_dash_bar2.setCalendarPopup(True)
        self.ff_dash_bar2.setDate(QDate(2023, 1, 1))

        self.horizontalLayout_85.addWidget(self.ff_dash_bar2)


        self.verticalLayout_49.addWidget(self.ff_bar2)

        self.verticalSpacer_46 = QSpacerItem(20, 54, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_49.addItem(self.verticalSpacer_46)


        self.horizontalLayout_65.addWidget(self.Barras2_Content_Der)


        self.verticalLayout_45.addWidget(self.Barras2_Content)


        self.horizontalLayout_64.addWidget(self.Barras2)


        self.verticalLayout_53.addWidget(self.FrameDash_Barras)

        self.FrameDashCont_Torta = QFrame(self.ScrollContents_Dashboard)
        self.FrameDashCont_Torta.setObjectName(u"FrameDashCont_Torta")
        self.FrameDashCont_Torta.setFrameShape(QFrame.StyledPanel)
        self.FrameDashCont_Torta.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.FrameDashCont_Torta)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_74.addItem(self.horizontalSpacer_56)

        self.FrameDash_Torta = QFrame(self.FrameDashCont_Torta)
        self.FrameDash_Torta.setObjectName(u"FrameDash_Torta")
        self.FrameDash_Torta.setFrameShape(QFrame.StyledPanel)
        self.FrameDash_Torta.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.FrameDash_Torta)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.Torta_Tittle = QFrame(self.FrameDash_Torta)
        self.Torta_Tittle.setObjectName(u"Torta_Tittle")
        self.Torta_Tittle.setMinimumSize(QSize(0, 40))
        self.Torta_Tittle.setMaximumSize(QSize(16777215, 40))
        self.Torta_Tittle.setFrameShape(QFrame.StyledPanel)
        self.Torta_Tittle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.Torta_Tittle)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.label_64 = QLabel(self.Torta_Tittle)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(16777215, 40))
        self.label_64.setFont(font11)
        self.label_64.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.label_64)


        self.verticalLayout_50.addWidget(self.Torta_Tittle)

        self.FrameDash_Content_Torta = QFrame(self.FrameDash_Torta)
        self.FrameDash_Content_Torta.setObjectName(u"FrameDash_Content_Torta")
        self.FrameDash_Content_Torta.setFrameShape(QFrame.StyledPanel)
        self.FrameDash_Content_Torta.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.FrameDash_Content_Torta)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.FrameTorta_Der = QFrame(self.FrameDash_Content_Torta)
        self.FrameTorta_Der.setObjectName(u"FrameTorta_Der")
        self.FrameTorta_Der.setMinimumSize(QSize(400, 0))
        self.FrameTorta_Der.setMaximumSize(QSize(400, 16777215))
        self.FrameTorta_Der.setFrameShape(QFrame.StyledPanel)
        self.FrameTorta_Der.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.FrameTorta_Der)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.Label_Torta = QLabel(self.FrameTorta_Der)
        self.Label_Torta.setObjectName(u"Label_Torta")
        self.Label_Torta.setMaximumSize(QSize(350, 350))

        self.verticalLayout_52.addWidget(self.Label_Torta)


        self.horizontalLayout_70.addWidget(self.FrameTorta_Der)

        self.FrameTorta_Izq = QFrame(self.FrameDash_Content_Torta)
        self.FrameTorta_Izq.setObjectName(u"FrameTorta_Izq")
        self.FrameTorta_Izq.setMaximumSize(QSize(325, 16777215))
        font13 = QFont()
        font13.setFamily(u"MS Serif")
        self.FrameTorta_Izq.setFont(font13)
        self.FrameTorta_Izq.setFrameShape(QFrame.StyledPanel)
        self.FrameTorta_Izq.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.FrameTorta_Izq)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalSpacer_47 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_51.addItem(self.verticalSpacer_47)

        self.f1_3 = QFrame(self.FrameTorta_Izq)
        self.f1_3.setObjectName(u"f1_3")
        self.f1_3.setFrameShape(QFrame.StyledPanel)
        self.f1_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.f1_3)
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.f1_3)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font11)

        self.horizontalLayout_71.addWidget(self.label_65)

        self.torta_client_combo = QComboBox(self.f1_3)
        self.torta_client_combo.setObjectName(u"torta_client_combo")
        self.torta_client_combo.setMinimumSize(QSize(150, 0))
        self.torta_client_combo.setFont(font12)

        self.horizontalLayout_71.addWidget(self.torta_client_combo)


        self.verticalLayout_51.addWidget(self.f1_3)

        self.f2_3 = QFrame(self.FrameTorta_Izq)
        self.f2_3.setObjectName(u"f2_3")
        self.f2_3.setFrameShape(QFrame.StyledPanel)
        self.f2_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.f2_3)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.label_66 = QLabel(self.f2_3)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font11)

        self.horizontalLayout_73.addWidget(self.label_66)

        self.torta_tdato_combo = QComboBox(self.f2_3)
        self.torta_tdato_combo.setObjectName(u"torta_tdato_combo")
        self.torta_tdato_combo.setMinimumSize(QSize(150, 0))
        self.torta_tdato_combo.setFont(font12)

        self.horizontalLayout_73.addWidget(self.torta_tdato_combo)


        self.verticalLayout_51.addWidget(self.f2_3)

        self.f3_3 = QFrame(self.FrameTorta_Izq)
        self.f3_3.setObjectName(u"f3_3")
        self.f3_3.setFrameShape(QFrame.StyledPanel)
        self.f3_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.f3_3)
        self.horizontalLayout_72.setSpacing(0)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.label_67 = QLabel(self.f3_3)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font11)

        self.horizontalLayout_72.addWidget(self.label_67)

        self.torta_column_combo = QComboBox(self.f3_3)
        self.torta_column_combo.setObjectName(u"torta_column_combo")
        self.torta_column_combo.setMinimumSize(QSize(150, 0))
        self.torta_column_combo.setFont(font12)

        self.horizontalLayout_72.addWidget(self.torta_column_combo)


        self.verticalLayout_51.addWidget(self.f3_3)

        self.fi_torta = QFrame(self.FrameTorta_Izq)
        self.fi_torta.setObjectName(u"fi_torta")
        self.fi_torta.setFrameShape(QFrame.StyledPanel)
        self.fi_torta.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.fi_torta)
        self.horizontalLayout_86.setSpacing(0)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.label_71 = QLabel(self.fi_torta)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font11)

        self.horizontalLayout_86.addWidget(self.label_71)

        self.fi_dash_torta = QDateEdit(self.fi_torta)
        self.fi_dash_torta.setObjectName(u"fi_dash_torta")
        self.fi_dash_torta.setMinimumSize(QSize(150, 35))
        self.fi_dash_torta.setFont(font12)
        self.fi_dash_torta.setStyleSheet(u"QCalendarWidget {\n"
"    background-color: rgb(165, 165, 165);\n"
"}\n"
"\n"
"QCalendarWidget QTableView {\n"
"    background-color:rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: white;\n"
"	font-size: 12px;\n"
"	background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"	width: 150px;\n"
"	left: 20px;\n"
"	color: white;\n"
"	font-size: 15px;\n"
"	background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"	background-color:  rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"")
        self.fi_dash_torta.setCalendarPopup(True)
        self.fi_dash_torta.setDate(QDate(2023, 1, 1))

        self.horizontalLayout_86.addWidget(self.fi_dash_torta)


        self.verticalLayout_51.addWidget(self.fi_torta)

        self.ff_torta = QFrame(self.FrameTorta_Izq)
        self.ff_torta.setObjectName(u"ff_torta")
        self.ff_torta.setFrameShape(QFrame.StyledPanel)
        self.ff_torta.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.ff_torta)
        self.horizontalLayout_87.setSpacing(0)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.label_72 = QLabel(self.ff_torta)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font11)

        self.horizontalLayout_87.addWidget(self.label_72)

        self.ff_dash_torta = QDateEdit(self.ff_torta)
        self.ff_dash_torta.setObjectName(u"ff_dash_torta")
        self.ff_dash_torta.setMinimumSize(QSize(150, 35))
        self.ff_dash_torta.setFont(font12)
        self.ff_dash_torta.setStyleSheet(u"QCalendarWidget {\n"
"    background-color: rgb(165, 165, 165);\n"
"}\n"
"\n"
"QCalendarWidget QTableView {\n"
"    background-color:rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: white;\n"
"	font-size: 12px;\n"
"	background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"	width: 150px;\n"
"	left: 20px;\n"
"	color: white;\n"
"	font-size: 15px;\n"
"	background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"	background-color:  rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"")
        self.ff_dash_torta.setCalendarPopup(True)
        self.ff_dash_torta.setDate(QDate(2023, 1, 1))

        self.horizontalLayout_87.addWidget(self.ff_dash_torta)


        self.verticalLayout_51.addWidget(self.ff_torta)

        self.verticalSpacer_48 = QSpacerItem(20, 21, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_51.addItem(self.verticalSpacer_48)


        self.horizontalLayout_70.addWidget(self.FrameTorta_Izq)


        self.verticalLayout_50.addWidget(self.FrameDash_Content_Torta)


        self.horizontalLayout_74.addWidget(self.FrameDash_Torta)

        self.horizontalSpacer_57 = QSpacerItem(233, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_74.addItem(self.horizontalSpacer_57)


        self.verticalLayout_53.addWidget(self.FrameDashCont_Torta)

        self.scrollArea.setWidget(self.ScrollContents_Dashboard)
        self.FrameDashCont_Torta.raise_()
        self.FrameDashCont_Histo.raise_()
        self.FrameDash_Barras.raise_()

        self.gridLayout_13.addWidget(self.scrollArea, 2, 1, 2, 3)

        self.horizontalSpacer_53 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_53, 2, 4, 1, 1)

        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_52, 3, 0, 1, 1)

        self.verticalSpacer_38 = QSpacerItem(20, 51, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_38, 4, 3, 1, 1)

        self.Tittle_Dashboard = QLabel(self.dashboard)
        self.Tittle_Dashboard.setObjectName(u"Tittle_Dashboard")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tittle_Dashboard.sizePolicy().hasHeightForWidth())
        self.Tittle_Dashboard.setSizePolicy(sizePolicy)
        self.Tittle_Dashboard.setMinimumSize(QSize(0, 45))
        self.Tittle_Dashboard.setFont(font10)
        self.Tittle_Dashboard.setStyleSheet(u"#Tittle_Dashboard{\n"
"background-color: rgb(237, 65, 36);\n"
"color:white;\n"
"border: 1px solid black;\n"
"}\n"
"")
        self.Tittle_Dashboard.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.Tittle_Dashboard, 0, 0, 1, 5)

        self.stackedWidget.addWidget(self.dashboard)
        self.hashes = QWidget()
        self.hashes.setObjectName(u"hashes")
        self.hashes.setStyleSheet(u"")
        self.gridLayout_10 = QGridLayout(self.hashes)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_38 = QSpacerItem(231, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_38, 3, 0, 1, 1)

        self.Tittle_Hashes = QLabel(self.hashes)
        self.Tittle_Hashes.setObjectName(u"Tittle_Hashes")
        self.Tittle_Hashes.setMinimumSize(QSize(0, 45))
        self.Tittle_Hashes.setFont(font10)
        self.Tittle_Hashes.setStyleSheet(u"#Tittle_Hashes{\n"
"background-color: rgb(237, 65, 36);\n"
"color:white;\n"
"border: 1px solid black;\n"
"}\n"
"")
        self.Tittle_Hashes.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.Tittle_Hashes, 0, 0, 2, 4)

        self.FrameContent_Hashes = QWidget(self.hashes)
        self.FrameContent_Hashes.setObjectName(u"FrameContent_Hashes")
        self.FrameContent_Hashes.setStyleSheet(u"#FrameContent_Hashes{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#FrameSubContent_Tittle{\n"
"background-color: rgb(51, 51, 51);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"}\n"
"\n"
"QLineEdit, QComboBox{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"padding:5px;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: rgb(217, 217, 217);\n"
"    border: none;\n"
"    selection-background-color: rgba(51, 51, 51, 0.5);\n"
"    outline: none;\n"
"}\n"
"\n"
"#QPushButton{\n"
"color:white;\n"
"background-color: rgb(0, 161, 92);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#QPushButton:hover{\n"
"background-color:rgb(40, 209, 118);\n"
"color: rgb(26, 26, 26);\n"
"}")
        self.verticalLayout_31 = QVBoxLayout(self.FrameContent_Hashes)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.FrameSubContent_Tittle = QFrame(self.FrameContent_Hashes)
        self.FrameSubContent_Tittle.setObjectName(u"FrameSubContent_Tittle")
        self.FrameSubContent_Tittle.setMinimumSize(QSize(0, 40))
        self.FrameSubContent_Tittle.setMaximumSize(QSize(16777215, 40))
        self.FrameSubContent_Tittle.setFrameShape(QFrame.StyledPanel)
        self.FrameSubContent_Tittle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.FrameSubContent_Tittle)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.FrameSubContent_Tittle)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font11)
        self.label_39.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_39)


        self.verticalLayout_31.addWidget(self.FrameSubContent_Tittle)

        self.FrameSubContent_List = QFrame(self.FrameContent_Hashes)
        self.FrameSubContent_List.setObjectName(u"FrameSubContent_List")
        self.FrameSubContent_List.setMinimumSize(QSize(800, 250))
        self.FrameSubContent_List.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.FrameSubContent_List.setFrameShape(QFrame.StyledPanel)
        self.FrameSubContent_List.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.FrameSubContent_List)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, -1)
        self.List_Clientes = QListWidget(self.FrameSubContent_List)
        self.List_Clientes.setObjectName(u"List_Clientes")

        self.verticalLayout_32.addWidget(self.List_Clientes)


        self.verticalLayout_31.addWidget(self.FrameSubContent_List)

        self.FrameSubContent_Hashes = QFrame(self.FrameContent_Hashes)
        self.FrameSubContent_Hashes.setObjectName(u"FrameSubContent_Hashes")
        self.FrameSubContent_Hashes.setMinimumSize(QSize(0, 0))
        self.FrameSubContent_Hashes.setFrameShape(QFrame.StyledPanel)
        self.FrameSubContent_Hashes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.FrameSubContent_Hashes)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.f1 = QFrame(self.FrameSubContent_Hashes)
        self.f1.setObjectName(u"f1")
        self.f1.setFrameShape(QFrame.StyledPanel)
        self.f1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.f1)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.entry_hashes = QLineEdit(self.f1)
        self.entry_hashes.setObjectName(u"entry_hashes")
        self.entry_hashes.setFont(font12)

        self.horizontalLayout_35.addWidget(self.entry_hashes)

        self.btn_hashes_aadir = QPushButton(self.f1)
        self.btn_hashes_aadir.setObjectName(u"btn_hashes_aadir")
        self.btn_hashes_aadir.setMinimumSize(QSize(150, 0))
        self.btn_hashes_aadir.setFont(font11)
        self.btn_hashes_aadir.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color:rgb(31, 106, 165);\n"
"padding:5px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
" QPushButton:hover{\n"
"background-color:rgb(38, 130, 202);\n"
"}")

        self.horizontalLayout_35.addWidget(self.btn_hashes_aadir)


        self.verticalLayout_30.addWidget(self.f1)

        self.f2 = QFrame(self.FrameSubContent_Hashes)
        self.f2.setObjectName(u"f2")
        self.f2.setFrameShape(QFrame.StyledPanel)
        self.f2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.f2)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_40 = QLabel(self.f2)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(150, 0))
        self.label_40.setFont(font11)
        self.label_40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_40)

        self.tipolista_combo = QComboBox(self.f2)
        self.tipolista_combo.addItem("")
        self.tipolista_combo.addItem("")
        self.tipolista_combo.setObjectName(u"tipolista_combo")
        self.tipolista_combo.setMinimumSize(QSize(200, 0))
        self.tipolista_combo.setFont(font12)

        self.horizontalLayout_36.addWidget(self.tipolista_combo)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_40)

        self.label_41 = QLabel(self.f2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(150, 0))
        self.label_41.setFont(font11)
        self.label_41.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_41)

        self.category_combo = QComboBox(self.f2)
        self.category_combo.addItem("")
        self.category_combo.addItem("")
        self.category_combo.addItem("")
        self.category_combo.addItem("")
        self.category_combo.addItem("")
        self.category_combo.addItem("")
        self.category_combo.addItem("")
        self.category_combo.setObjectName(u"category_combo")
        self.category_combo.setMinimumSize(QSize(200, 0))
        self.category_combo.setFont(font12)

        self.horizontalLayout_36.addWidget(self.category_combo)


        self.verticalLayout_30.addWidget(self.f2)

        self.f3 = QFrame(self.FrameSubContent_Hashes)
        self.f3.setObjectName(u"f3")
        self.f3.setFrameShape(QFrame.StyledPanel)
        self.f3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.f3)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(-1, -1, -1, 30)
        self.label_42 = QLabel(self.f3)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(150, 0))
        self.label_42.setFont(font11)
        self.label_42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_42)

        self.entry_reason = QLineEdit(self.f3)
        self.entry_reason.setObjectName(u"entry_reason")
        self.entry_reason.setFont(font12)

        self.horizontalLayout_37.addWidget(self.entry_reason)


        self.verticalLayout_30.addWidget(self.f3)

        self.f1_7 = QFrame(self.FrameSubContent_Hashes)
        self.f1_7.setObjectName(u"f1_7")
        self.f1_7.setFrameShape(QFrame.StyledPanel)
        self.f1_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.f1_7)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.progressBar = QProgressBar(self.f1_7)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.horizontalLayout_79.addWidget(self.progressBar)


        self.verticalLayout_30.addWidget(self.f1_7)


        self.verticalLayout_31.addWidget(self.FrameSubContent_Hashes)

        self.FrameSubContent_Buttons = QFrame(self.FrameContent_Hashes)
        self.FrameSubContent_Buttons.setObjectName(u"FrameSubContent_Buttons")
        self.FrameSubContent_Buttons.setMinimumSize(QSize(0, 60))
        self.FrameSubContent_Buttons.setFrameShape(QFrame.StyledPanel)
        self.FrameSubContent_Buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.FrameSubContent_Buttons)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_59 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_59)

        self.btn_hashes_select = QPushButton(self.FrameSubContent_Buttons)
        self.btn_hashes_select.setObjectName(u"btn_hashes_select")
        self.btn_hashes_select.setMinimumSize(QSize(130, 0))
        font14 = QFont()
        font14.setFamily(u"Poppins Medium")
        font14.setPointSize(11)
        self.btn_hashes_select.setFont(font14)
        self.btn_hashes_select.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color: rgb(0, 161, 92);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
" QPushButton:hover{\n"
"background-color:rgb(40, 209, 118);\n"
"color: rgb(26, 26, 26);\n"
"}")

        self.horizontalLayout_38.addWidget(self.btn_hashes_select)

        self.horizontalSpacer_36 = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_36)

        self.btn_hashes_borrar = QPushButton(self.FrameSubContent_Buttons)
        self.btn_hashes_borrar.setObjectName(u"btn_hashes_borrar")
        self.btn_hashes_borrar.setMinimumSize(QSize(130, 0))
        self.btn_hashes_borrar.setFont(font11)
        self.btn_hashes_borrar.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color:rgb(161, 0, 0);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
" QPushButton:hover{\n"
"background-color:rgb(209, 40, 40);\n"
"}")

        self.horizontalLayout_38.addWidget(self.btn_hashes_borrar)

        self.horizontalSpacer_37 = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_37)

        self.btn_hashes_cargar = QPushButton(self.FrameSubContent_Buttons)
        self.btn_hashes_cargar.setObjectName(u"btn_hashes_cargar")
        self.btn_hashes_cargar.setMinimumSize(QSize(130, 0))
        self.btn_hashes_cargar.setFont(font11)
        self.btn_hashes_cargar.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color:rgb(31, 106, 165);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
" QPushButton:hover{\n"
"background-color:rgb(38, 130, 202);\n"
"}")

        self.horizontalLayout_38.addWidget(self.btn_hashes_cargar)

        self.horizontalSpacer_60 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_60)


        self.verticalLayout_31.addWidget(self.FrameSubContent_Buttons)

        self.FrameSubContent_List.raise_()
        self.FrameSubContent_Tittle.raise_()
        self.FrameSubContent_Buttons.raise_()
        self.FrameSubContent_Hashes.raise_()

        self.gridLayout_10.addWidget(self.FrameContent_Hashes, 3, 1, 2, 2)

        self.horizontalSpacer_39 = QSpacerItem(231, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_39, 4, 3, 1, 1)

        self.verticalSpacer_27 = QSpacerItem(20, 125, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_27, 5, 2, 1, 1)

        self.verticalSpacer_26 = QSpacerItem(20, 72, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_26, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.hashes)
        self.ayuda = QWidget()
        self.ayuda.setObjectName(u"ayuda")
        self.gridLayout_11 = QGridLayout(self.ayuda)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Tittle_Ayuda = QLabel(self.ayuda)
        self.Tittle_Ayuda.setObjectName(u"Tittle_Ayuda")
        self.Tittle_Ayuda.setMinimumSize(QSize(0, 45))
        self.Tittle_Ayuda.setFont(font10)
        self.Tittle_Ayuda.setStyleSheet(u"#Tittle_Ayuda{\n"
"background-color: rgb(237, 65, 36);\n"
"color:white;\n"
"border: 1px solid black;\n"
"}\n"
"")
        self.Tittle_Ayuda.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.Tittle_Ayuda, 0, 0, 1, 3)

        self.verticalSpacer_28 = QSpacerItem(20, 243, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_28, 1, 1, 1, 1)

        self.horizontalSpacer_41 = QSpacerItem(293, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_41, 2, 0, 1, 1)

        self.FrameContent_Ayuda = QWidget(self.ayuda)
        self.FrameContent_Ayuda.setObjectName(u"FrameContent_Ayuda")
        self.FrameContent_Ayuda.setStyleSheet(u"#FrameContent_Ayuda{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#FrameSubContent_Tittle{\n"
"background-color: rgba(51, 51, 51);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"color:white;\n"
"background-color:rgb(31, 106, 165);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
" QPushButton:hover{\n"
"background-color:rgb(38, 130, 202);\n"
"}")
        self.verticalLayout_34 = QVBoxLayout(self.FrameContent_Ayuda)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.FrameSubContent_Top = QFrame(self.FrameContent_Ayuda)
        self.FrameSubContent_Top.setObjectName(u"FrameSubContent_Top")
        self.FrameSubContent_Top.setFrameShape(QFrame.StyledPanel)
        self.FrameSubContent_Top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.FrameSubContent_Top)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_6 = QLabel(self.FrameSubContent_Top)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font11)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_6)

        self.label_10 = QLabel(self.FrameSubContent_Top)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font11)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_10)

        self.verticalSpacer_30 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_30)


        self.verticalLayout_34.addWidget(self.FrameSubContent_Top)

        self.FrameSubContent_Inf = QFrame(self.FrameContent_Ayuda)
        self.FrameSubContent_Inf.setObjectName(u"FrameSubContent_Inf")
        self.FrameSubContent_Inf.setStyleSheet(u"#FrameSubContent_Inf{\n"
"background-color: rgba(58, 58, 58, 0.5);\n"
"}")
        self.FrameSubContent_Inf.setFrameShape(QFrame.StyledPanel)
        self.FrameSubContent_Inf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.FrameSubContent_Inf)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 10, 0, 10)
        self.label_43 = QLabel(self.FrameSubContent_Inf)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font11)
        self.label_43.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.label_43)


        self.verticalLayout_34.addWidget(self.FrameSubContent_Inf)

        self.FrameSubContent_Buttons_2 = QFrame(self.FrameContent_Ayuda)
        self.FrameSubContent_Buttons_2.setObjectName(u"FrameSubContent_Buttons_2")
        self.FrameSubContent_Buttons_2.setFrameShape(QFrame.StyledPanel)
        self.FrameSubContent_Buttons_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.FrameSubContent_Buttons_2)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(-1, 30, -1, -1)
        self.horizontalSpacer_43 = QSpacerItem(74, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_43)

        self.btn_descarga = QPushButton(self.FrameSubContent_Buttons_2)
        self.btn_descarga.setObjectName(u"btn_descarga")
        self.btn_descarga.setFont(font11)
        icon12 = QIcon()
        icon12.addFile(u":/icons/feather/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_descarga.setIcon(icon12)
        self.btn_descarga.setIconSize(QSize(24, 24))

        self.horizontalLayout_39.addWidget(self.btn_descarga)

        self.horizontalSpacer_44 = QSpacerItem(75, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_44)

        self.btn_readonline = QPushButton(self.FrameSubContent_Buttons_2)
        self.btn_readonline.setObjectName(u"btn_readonline")
        self.btn_readonline.setFont(font11)
        self.btn_readonline.setLayoutDirection(Qt.RightToLeft)
        icon13 = QIcon()
        icon13.addFile(u":/icons/feather/wifi.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_readonline.setIcon(icon13)
        self.btn_readonline.setIconSize(QSize(24, 24))
        self.btn_readonline.setFlat(False)

        self.horizontalLayout_39.addWidget(self.btn_readonline)

        self.horizontalSpacer_45 = QSpacerItem(74, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_45)


        self.verticalLayout_34.addWidget(self.FrameSubContent_Buttons_2)


        self.gridLayout_11.addWidget(self.FrameContent_Ayuda, 2, 1, 2, 1)

        self.horizontalSpacer_42 = QSpacerItem(293, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_42, 3, 2, 1, 1)

        self.verticalSpacer_29 = QSpacerItem(20, 243, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_29, 4, 1, 1, 1)

        self.stackedWidget.addWidget(self.ayuda)
        self.graficos = QWidget()
        self.graficos.setObjectName(u"graficos")
        self.gridLayout_12 = QGridLayout(self.graficos)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.Tittle_Graficos = QLabel(self.graficos)
        self.Tittle_Graficos.setObjectName(u"Tittle_Graficos")
        self.Tittle_Graficos.setMinimumSize(QSize(0, 45))
        self.Tittle_Graficos.setFont(font10)
        self.Tittle_Graficos.setStyleSheet(u"#Tittle_Graficos{\n"
"background-color: rgb(237, 65, 36);\n"
"color:white;\n"
"border: 1px solid black;\n"
"}\n"
"")
        self.Tittle_Graficos.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.Tittle_Graficos, 0, 0, 1, 3)

        self.verticalSpacer_31 = QSpacerItem(20, 73, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_31, 1, 1, 1, 1)

        self.horizontalSpacer_46 = QSpacerItem(112, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_46, 2, 0, 1, 1)

        self.FrameContent_Graficos = QWidget(self.graficos)
        self.FrameContent_Graficos.setObjectName(u"FrameContent_Graficos")
        self.FrameContent_Graficos.setStyleSheet(u"#FrameContent_Graficos{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"}\n"
"\n"
"#FrameContent_Graficos QPushButton{\n"
"color:white;\n"
"background-color: rgb(0, 161, 92);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#FrameContent_Graficos QPushButton:hover{\n"
"background-color:rgb(40, 209, 118);\n"
"color: rgb(26, 26, 26);\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"padding:5px;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: rgb(217, 217, 217);\n"
"    border: none;\n"
"    selection-background-color: rgba(51, 51, 51, 0.5);\n"
"    outline: none;\n"
"}\n"
"\n"
"")
        self.verticalLayout_38 = QVBoxLayout(self.FrameContent_Graficos)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.FrameSubContent_Top_2 = QFrame(self.FrameContent_Graficos)
        self.FrameSubContent_Top_2.setObjectName(u"FrameSubContent_Top_2")
        self.FrameSubContent_Top_2.setFrameShape(QFrame.StyledPanel)
        self.FrameSubContent_Top_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.FrameSubContent_Top_2)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.FrameIzq = QFrame(self.FrameSubContent_Top_2)
        self.FrameIzq.setObjectName(u"FrameIzq")
        self.FrameIzq.setFrameShape(QFrame.StyledPanel)
        self.FrameIzq.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.FrameIzq)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalSpacer_34 = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_34)

        self.f1_data = QFrame(self.FrameIzq)
        self.f1_data.setObjectName(u"f1_data")
        self.f1_data.setFrameShape(QFrame.StyledPanel)
        self.f1_data.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.f1_data)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_7 = QLabel(self.f1_data)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font11)

        self.horizontalLayout_42.addWidget(self.label_7)

        self.graficos_tipod_combo = QComboBox(self.f1_data)
        self.graficos_tipod_combo.setObjectName(u"graficos_tipod_combo")
        self.graficos_tipod_combo.setFont(font12)

        self.horizontalLayout_42.addWidget(self.graficos_tipod_combo)


        self.verticalLayout_35.addWidget(self.f1_data)

        self.f2_data = QFrame(self.FrameIzq)
        self.f2_data.setObjectName(u"f2_data")
        self.f2_data.setFrameShape(QFrame.StyledPanel)
        self.f2_data.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.f2_data)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_44 = QLabel(self.f2_data)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font11)

        self.horizontalLayout_43.addWidget(self.label_44)

        self.graficos_tipog_combo = QComboBox(self.f2_data)
        self.graficos_tipog_combo.setObjectName(u"graficos_tipog_combo")
        self.graficos_tipog_combo.setFont(font12)

        self.horizontalLayout_43.addWidget(self.graficos_tipog_combo)


        self.verticalLayout_35.addWidget(self.f2_data)

        self.f3_data = QFrame(self.FrameIzq)
        self.f3_data.setObjectName(u"f3_data")
        self.f3_data.setFrameShape(QFrame.StyledPanel)
        self.f3_data.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.f3_data)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_45 = QLabel(self.f3_data)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font11)

        self.horizontalLayout_44.addWidget(self.label_45)

        self.graficos_colum_combo = QComboBox(self.f3_data)
        self.graficos_colum_combo.setObjectName(u"graficos_colum_combo")
        self.graficos_colum_combo.setFont(font12)

        self.horizontalLayout_44.addWidget(self.graficos_colum_combo)


        self.verticalLayout_35.addWidget(self.f3_data)

        self.f4_data = QFrame(self.FrameIzq)
        self.f4_data.setObjectName(u"f4_data")
        self.f4_data.setFrameShape(QFrame.StyledPanel)
        self.f4_data.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.f4_data)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_46 = QLabel(self.f4_data)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font11)

        self.horizontalLayout_45.addWidget(self.label_46)

        self.graficos_cliente_combo = QComboBox(self.f4_data)
        self.graficos_cliente_combo.setObjectName(u"graficos_cliente_combo")
        self.graficos_cliente_combo.setFont(font12)

        self.horizontalLayout_45.addWidget(self.graficos_cliente_combo)


        self.verticalLayout_35.addWidget(self.f4_data)

        self.frame_7 = QFrame(self.FrameIzq)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_47 = QLabel(self.frame_7)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font11)

        self.horizontalLayout_46.addWidget(self.label_47)

        self.fecha_inicio = QDateEdit(self.frame_7)
        self.fecha_inicio.setObjectName(u"fecha_inicio")
        self.fecha_inicio.setFont(font12)
        self.fecha_inicio.setStyleSheet(u"QCalendarWidget {\n"
"    background-color: rgb(165, 165, 165);\n"
"}\n"
"\n"
"QCalendarWidget QTableView {\n"
"    background-color:rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: white;\n"
"	font-size: 12px;\n"
"	background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"	width: 150px;\n"
"	left: 20px;\n"
"	color: white;\n"
"	font-size: 15px;\n"
"	background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"	background-color:  rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"")
        self.fecha_inicio.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.fecha_inicio.setCalendarPopup(True)

        self.horizontalLayout_46.addWidget(self.fecha_inicio)

        self.fecha_fin = QDateEdit(self.frame_7)
        self.fecha_fin.setObjectName(u"fecha_fin")
        self.fecha_fin.setFont(font12)
        self.fecha_fin.setStyleSheet(u"QCalendarWidget {\n"
"    background-color: rgb(165, 165, 165);\n"
"}\n"
"\n"
"QCalendarWidget QTableView {\n"
"    background-color:rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: white;\n"
"	font-size: 12px;\n"
"	background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"	width: 150px;\n"
"	left: 20px;\n"
"	color: white;\n"
"	font-size: 15px;\n"
"	background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"	background-color:  rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}")
        self.fecha_fin.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.fecha_fin.setCalendarPopup(True)

        self.horizontalLayout_46.addWidget(self.fecha_fin)


        self.verticalLayout_35.addWidget(self.frame_7)

        self.verticalSpacer_33 = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_35.addItem(self.verticalSpacer_33)


        self.horizontalLayout_47.addWidget(self.FrameIzq)

        self.FrameDer = QFrame(self.FrameSubContent_Top_2)
        self.FrameDer.setObjectName(u"FrameDer")
        self.FrameDer.setFrameShape(QFrame.StyledPanel)
        self.FrameDer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.FrameDer)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalSpacer_35 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_37.addItem(self.verticalSpacer_35)

        self.FrameImage = QFrame(self.FrameDer)
        self.FrameImage.setObjectName(u"FrameImage")
        self.FrameImage.setMinimumSize(QSize(600, 400))
        self.FrameImage.setMaximumSize(QSize(600, 400))
        self.FrameImage.setFrameShape(QFrame.StyledPanel)
        self.FrameImage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.FrameImage)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_grafico = QLabel(self.FrameImage)
        self.label_grafico.setObjectName(u"label_grafico")
        self.label_grafico.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_grafico)


        self.verticalLayout_37.addWidget(self.FrameImage)

        self.verticalSpacer_36 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_37.addItem(self.verticalSpacer_36)


        self.horizontalLayout_47.addWidget(self.FrameDer)


        self.verticalLayout_38.addWidget(self.FrameSubContent_Top_2)

        self.FrameSubContent_Buttons_3 = QFrame(self.FrameContent_Graficos)
        self.FrameSubContent_Buttons_3.setObjectName(u"FrameSubContent_Buttons_3")
        self.FrameSubContent_Buttons_3.setFrameShape(QFrame.StyledPanel)
        self.FrameSubContent_Buttons_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.FrameSubContent_Buttons_3)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalSpacer_48 = QSpacerItem(101, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_48)

        self.btn_grafico_crear = QPushButton(self.FrameSubContent_Buttons_3)
        self.btn_grafico_crear.setObjectName(u"btn_grafico_crear")
        self.btn_grafico_crear.setMinimumSize(QSize(130, 0))
        self.btn_grafico_crear.setFont(font11)
        self.btn_grafico_crear.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color:rgb(31, 106, 165);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
" QPushButton:hover{\n"
"background-color:rgb(38, 130, 202);\n"
"}")

        self.horizontalLayout_41.addWidget(self.btn_grafico_crear)

        self.horizontalSpacer_49 = QSpacerItem(102, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_49)

        self.btn_graficos_borrar = QPushButton(self.FrameSubContent_Buttons_3)
        self.btn_graficos_borrar.setObjectName(u"btn_graficos_borrar")
        self.btn_graficos_borrar.setMinimumSize(QSize(130, 0))
        self.btn_graficos_borrar.setFont(font11)
        self.btn_graficos_borrar.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color:rgb(161, 0, 0);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
" QPushButton:hover{\n"
"background-color:rgb(209, 40, 40);\n"
"}")

        self.horizontalLayout_41.addWidget(self.btn_graficos_borrar)

        self.horizontalSpacer_50 = QSpacerItem(101, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_50)

        self.btn_graficos_exportar = QPushButton(self.FrameSubContent_Buttons_3)
        self.btn_graficos_exportar.setObjectName(u"btn_graficos_exportar")
        self.btn_graficos_exportar.setMinimumSize(QSize(130, 0))
        self.btn_graficos_exportar.setFont(font11)

        self.horizontalLayout_41.addWidget(self.btn_graficos_exportar)

        self.horizontalSpacer_51 = QSpacerItem(101, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_51)


        self.verticalLayout_38.addWidget(self.FrameSubContent_Buttons_3)


        self.gridLayout_12.addWidget(self.FrameContent_Graficos, 2, 1, 2, 1)

        self.horizontalSpacer_47 = QSpacerItem(112, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_47, 3, 2, 1, 1)

        self.verticalSpacer_32 = QSpacerItem(20, 73, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_32, 4, 1, 1, 1)

        self.stackedWidget.addWidget(self.graficos)
        self.cargar_clientes = QWidget()
        self.cargar_clientes.setObjectName(u"cargar_clientes")
        self.gridLayout_4 = QGridLayout(self.cargar_clientes)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Tittle_Cclientes = QLabel(self.cargar_clientes)
        self.Tittle_Cclientes.setObjectName(u"Tittle_Cclientes")
        self.Tittle_Cclientes.setMinimumSize(QSize(0, 45))
        self.Tittle_Cclientes.setFont(font10)
        self.Tittle_Cclientes.setStyleSheet(u"#Tittle_Cclientes{\n"
"background-color: rgb(237, 65, 36);\n"
"color:white;\n"
"border: 1px solid black;\n"
"}\n"
"")
        self.Tittle_Cclientes.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.Tittle_Cclientes, 0, 0, 1, 3)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_14, 2, 2, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 141, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_12, 4, 1, 1, 1)

        self.FrameContent_Cclientes = QWidget(self.cargar_clientes)
        self.FrameContent_Cclientes.setObjectName(u"FrameContent_Cclientes")
        self.FrameContent_Cclientes.setMinimumSize(QSize(500, 0))
        self.FrameContent_Cclientes.setStyleSheet(u"#FrameContent_Cclientes{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"}\n"
"\n"
"#FrameContent_Inicio QPushButton{\n"
"color:white;\n"
"background-color: rgb(0, 161, 92);\n"
"padding:5px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#FrameContent_Inicio QPushButton:hover{\n"
"background-color:rgb(40, 209, 118);\n"
"color: rgb(26, 26, 26);\n"
"}\n"
"\n"
"QLineEdit, QComboBox{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"padding:5px;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: rgb(217, 217, 217);\n"
"    border: none;\n"
"    selection-background-color: rgba(51, 51, 51, 0.5);\n"
"    outline: none;\n"
"}\n"
"\n"
"#FrameContent_Cclientes QPushButton{\n"
"color:white;\n"
"background-color: rgb(0, 161, 92);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#FrameContent_Cclientes QPushButton:hover{\n"
"background-color:rgb(40, 209, 118);\n"
"color: rgb(26, 26, 26);\n"
"}")
        self.gridLayout_3 = QGridLayout(self.FrameContent_Cclientes)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.f2_tid = QFrame(self.FrameContent_Cclientes)
        self.f2_tid.setObjectName(u"f2_tid")
        self.f2_tid.setFrameShape(QFrame.StyledPanel)
        self.f2_tid.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.f2_tid)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_17 = QLabel(self.f2_tid)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font11)

        self.horizontalLayout_14.addWidget(self.label_17)

        self.entry_tid = QLineEdit(self.f2_tid)
        self.entry_tid.setObjectName(u"entry_tid")
        self.entry_tid.setMaximumSize(QSize(370, 16777215))
        self.entry_tid.setFont(font12)

        self.horizontalLayout_14.addWidget(self.entry_tid)


        self.gridLayout_3.addWidget(self.f2_tid, 1, 0, 1, 1)

        self.f5_token = QFrame(self.FrameContent_Cclientes)
        self.f5_token.setObjectName(u"f5_token")
        self.f5_token.setFrameShape(QFrame.StyledPanel)
        self.f5_token.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.f5_token)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_20 = QLabel(self.f5_token)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font11)

        self.horizontalLayout_17.addWidget(self.label_20)

        self.entry_token = QLineEdit(self.f5_token)
        self.entry_token.setObjectName(u"entry_token")
        self.entry_token.setMaximumSize(QSize(370, 16777215))
        self.entry_token.setFont(font12)

        self.horizontalLayout_17.addWidget(self.entry_token)


        self.gridLayout_3.addWidget(self.f5_token, 4, 0, 1, 1)

        self.f6_perio = QFrame(self.FrameContent_Cclientes)
        self.f6_perio.setObjectName(u"f6_perio")
        self.f6_perio.setFrameShape(QFrame.StyledPanel)
        self.f6_perio.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.f6_perio)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_21 = QLabel(self.f6_perio)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(105, 0))
        self.label_21.setMaximumSize(QSize(105, 16777215))
        self.label_21.setFont(font11)

        self.horizontalLayout_18.addWidget(self.label_21)

        self.horizontalSpacer_61 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_61)

        self.perio_combo = QComboBox(self.f6_perio)
        self.perio_combo.addItem("")
        self.perio_combo.addItem("")
        self.perio_combo.addItem("")
        self.perio_combo.setObjectName(u"perio_combo")
        self.perio_combo.setMinimumSize(QSize(195, 0))
        self.perio_combo.setMaximumSize(QSize(16777215, 16777215))
        self.perio_combo.setFont(font12)

        self.horizontalLayout_18.addWidget(self.perio_combo)

        self.horizontalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_15)


        self.gridLayout_3.addWidget(self.f6_perio, 5, 0, 1, 1)

        self.frame = QFrame(self.FrameContent_Cclientes)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_cargacli = QPushButton(self.frame)
        self.btn_cargacli.setObjectName(u"btn_cargacli")
        self.btn_cargacli.setMaximumSize(QSize(140, 40))
        self.btn_cargacli.setFont(font8)

        self.horizontalLayout_11.addWidget(self.btn_cargacli)


        self.gridLayout_3.addWidget(self.frame, 8, 0, 1, 1)

        self.f1_nombre = QFrame(self.FrameContent_Cclientes)
        self.f1_nombre.setObjectName(u"f1_nombre")
        self.f1_nombre.setFrameShape(QFrame.StyledPanel)
        self.f1_nombre.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.f1_nombre)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_16 = QLabel(self.f1_nombre)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font11)

        self.horizontalLayout_10.addWidget(self.label_16)

        self.entry_nombre = QLineEdit(self.f1_nombre)
        self.entry_nombre.setObjectName(u"entry_nombre")
        self.entry_nombre.setMinimumSize(QSize(100, 0))
        self.entry_nombre.setMaximumSize(QSize(370, 16777215))
        self.entry_nombre.setFont(font12)

        self.horizontalLayout_10.addWidget(self.entry_nombre)


        self.gridLayout_3.addWidget(self.f1_nombre, 0, 0, 1, 1)

        self.f7_region = QFrame(self.FrameContent_Cclientes)
        self.f7_region.setObjectName(u"f7_region")
        self.f7_region.setFont(font12)
        self.f7_region.setFrameShape(QFrame.StyledPanel)
        self.f7_region.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.f7_region)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_22 = QLabel(self.f7_region)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(105, 0))
        self.label_22.setMaximumSize(QSize(125, 16777215))
        self.label_22.setFont(font11)

        self.horizontalLayout_13.addWidget(self.label_22)

        self.horizontalSpacer_62 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_62)

        self.regio_combo = QComboBox(self.f7_region)
        self.regio_combo.addItem("")
        self.regio_combo.addItem("")
        self.regio_combo.setObjectName(u"regio_combo")
        self.regio_combo.setMinimumSize(QSize(195, 0))
        self.regio_combo.setFont(font12)

        self.horizontalLayout_13.addWidget(self.regio_combo)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_16)


        self.gridLayout_3.addWidget(self.f7_region, 6, 0, 1, 1)

        self.f8_logo = QFrame(self.FrameContent_Cclientes)
        self.f8_logo.setObjectName(u"f8_logo")
        self.f8_logo.setFrameShape(QFrame.StyledPanel)
        self.f8_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.f8_logo)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_23 = QLabel(self.f8_logo)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(105, 16777215))
        self.label_23.setFont(font11)

        self.horizontalLayout_12.addWidget(self.label_23)

        self.horizontalSpacer_63 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_63)

        self.label_logo = QLabel(self.f8_logo)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMinimumSize(QSize(210, 0))
        self.label_logo.setMaximumSize(QSize(210, 35))
        self.label_logo.setFont(font12)
        self.label_logo.setStyleSheet(u"background-color: rgba(51, 51, 51,0.2);\n"
"padding:5px;\n"
"border-radius:10px;\n"
"color:white;")

        self.horizontalLayout_12.addWidget(self.label_logo)

        self.btn_agregar_logo = QPushButton(self.f8_logo)
        self.btn_agregar_logo.setObjectName(u"btn_agregar_logo")
        self.btn_agregar_logo.setMaximumSize(QSize(150, 16777215))
        self.btn_agregar_logo.setFont(font11)
        self.btn_agregar_logo.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color:rgb(31, 106, 165);\n"
"padding:5px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
" QPushButton:hover{\n"
"background-color:rgb(38, 130, 202);\n"
"}")

        self.horizontalLayout_12.addWidget(self.btn_agregar_logo)


        self.gridLayout_3.addWidget(self.f8_logo, 7, 0, 1, 1)

        self.f3_appid = QFrame(self.FrameContent_Cclientes)
        self.f3_appid.setObjectName(u"f3_appid")
        self.f3_appid.setFont(font12)
        self.f3_appid.setFrameShape(QFrame.StyledPanel)
        self.f3_appid.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.f3_appid)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_18 = QLabel(self.f3_appid)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font11)

        self.horizontalLayout_15.addWidget(self.label_18)

        self.entry_aid = QLineEdit(self.f3_appid)
        self.entry_aid.setObjectName(u"entry_aid")
        self.entry_aid.setMaximumSize(QSize(370, 16777215))
        self.entry_aid.setFont(font12)

        self.horizontalLayout_15.addWidget(self.entry_aid)


        self.gridLayout_3.addWidget(self.f3_appid, 2, 0, 1, 1)

        self.f4_sid = QFrame(self.FrameContent_Cclientes)
        self.f4_sid.setObjectName(u"f4_sid")
        self.f4_sid.setFrameShape(QFrame.StyledPanel)
        self.f4_sid.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.f4_sid)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_19 = QLabel(self.f4_sid)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font11)

        self.horizontalLayout_16.addWidget(self.label_19)

        self.entry_sid = QLineEdit(self.f4_sid)
        self.entry_sid.setObjectName(u"entry_sid")
        self.entry_sid.setMaximumSize(QSize(370, 16777215))
        self.entry_sid.setFont(font12)

        self.horizontalLayout_16.addWidget(self.entry_sid)


        self.gridLayout_3.addWidget(self.f4_sid, 3, 0, 1, 1)


        self.gridLayout_4.addWidget(self.FrameContent_Cclientes, 2, 1, 2, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 141, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_11, 1, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_13, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.cargar_clientes)
        self.listar_clientes = QWidget()
        self.listar_clientes.setObjectName(u"listar_clientes")
        self.gridLayout_5 = QGridLayout(self.listar_clientes)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Tittle_Lclientes = QLabel(self.listar_clientes)
        self.Tittle_Lclientes.setObjectName(u"Tittle_Lclientes")
        self.Tittle_Lclientes.setMinimumSize(QSize(0, 45))
        self.Tittle_Lclientes.setFont(font10)
        self.Tittle_Lclientes.setStyleSheet(u"#Tittle_Lclientes{\n"
"background-color: rgb(237, 65, 36);\n"
"color:white;\n"
"border: 1px solid black;\n"
"}\n"
"")
        self.Tittle_Lclientes.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.Tittle_Lclientes, 0, 0, 1, 4)

        self.verticalSpacer_13 = QSpacerItem(20, 27, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_13, 1, 1, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(64, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_17, 2, 0, 1, 1)

        self.FrameContent_Lclientes = QWidget(self.listar_clientes)
        self.FrameContent_Lclientes.setObjectName(u"FrameContent_Lclientes")
        self.FrameContent_Lclientes.setMinimumSize(QSize(0, 600))
        self.FrameContent_Lclientes.setMaximumSize(QSize(16777215, 16777215))
        self.FrameContent_Lclientes.setStyleSheet(u"#FrameContent_Lclientes{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"}\n"
"\n"
"QLineEdit, QComboBox{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"padding:5px;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: rgb(217, 217, 217);\n"
"    border: none;\n"
"    selection-background-color: rgba(51, 51, 51, 0.5);\n"
"    outline: none;\n"
"}\n"
"\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.FrameContent_Lclientes)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Frame_table = QFrame(self.FrameContent_Lclientes)
        self.Frame_table.setObjectName(u"Frame_table")
        self.Frame_table.setStyleSheet(u"#QTableWidget{\n"
"	background-color: rgb(255, 85, 0);\n"
"	alternate-background-color: rgb(170, 85, 255);\n"
"	selection-background-color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"")
        self.Frame_table.setFrameShape(QFrame.StyledPanel)
        self.Frame_table.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.Frame_table)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.Frame_table)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(109)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_16.addWidget(self.tableWidget)


        self.verticalLayout_5.addWidget(self.Frame_table)

        self.FrameSubContent = QFrame(self.FrameContent_Lclientes)
        self.FrameSubContent.setObjectName(u"FrameSubContent")
        self.FrameSubContent.setMinimumSize(QSize(0, 200))
        self.FrameSubContent.setStyleSheet(u"")
        self.FrameSubContent.setFrameShape(QFrame.StyledPanel)
        self.FrameSubContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.FrameSubContent)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 0, 0, 0)
        self.f_logo = QFrame(self.FrameSubContent)
        self.f_logo.setObjectName(u"f_logo")
        self.f_logo.setMinimumSize(QSize(125, 0))
        self.f_logo.setFrameShape(QFrame.StyledPanel)
        self.f_logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.f_logo)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.show_logo = QLabel(self.f_logo)
        self.show_logo.setObjectName(u"show_logo")
        self.show_logo.setMinimumSize(QSize(125, 125))
        self.show_logo.setMaximumSize(QSize(125, 125))
        self.show_logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.show_logo)


        self.horizontalLayout_20.addWidget(self.f_logo)

        self.f_entrys = QFrame(self.FrameSubContent)
        self.f_entrys.setObjectName(u"f_entrys")
        self.f_entrys.setStyleSheet(u"")
        self.f_entrys.setFrameShape(QFrame.StyledPanel)
        self.f_entrys.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.f_entrys)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.f_entry_sup = QFrame(self.f_entrys)
        self.f_entry_sup.setObjectName(u"f_entry_sup")
        self.f_entry_sup.setFrameShape(QFrame.StyledPanel)
        self.f_entry_sup.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.f_entry_sup)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, -1, -1, -1)
        self.f1_logo = QFrame(self.f_entry_sup)
        self.f1_logo.setObjectName(u"f1_logo")
        self.f1_logo.setFrameShape(QFrame.StyledPanel)
        self.f1_logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.f1_logo)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.f1_izq = QFrame(self.f1_logo)
        self.f1_izq.setObjectName(u"f1_izq")
        self.f1_izq.setFrameShape(QFrame.StyledPanel)
        self.f1_izq.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.f1_izq)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.f1_izq)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font11)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.label_11)

        self.entrylist_logo = QLineEdit(self.f1_izq)
        self.entrylist_logo.setObjectName(u"entrylist_logo")
        self.entrylist_logo.setMinimumSize(QSize(200, 0))
        self.entrylist_logo.setFont(font12)

        self.verticalLayout_44.addWidget(self.entrylist_logo)


        self.horizontalLayout_60.addWidget(self.f1_izq)

        self.f1_der = QFrame(self.f1_logo)
        self.f1_der.setObjectName(u"f1_der")
        self.f1_der.setFrameShape(QFrame.StyledPanel)
        self.f1_der.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.f1_der)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, -1, -1, 0)
        self.btn_act_logo = QPushButton(self.f1_der)
        self.btn_act_logo.setObjectName(u"btn_act_logo")
        self.btn_act_logo.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color:rgb(31, 106, 165);\n"
"padding:5px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
" QPushButton:hover{\n"
"background-color:rgb(38, 130, 202);\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/icons/feather/image.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_act_logo.setIcon(icon14)
        self.btn_act_logo.setIconSize(QSize(25, 25))

        self.horizontalLayout_21.addWidget(self.btn_act_logo, 0, Qt.AlignBottom)


        self.horizontalLayout_60.addWidget(self.f1_der)


        self.horizontalLayout_61.addWidget(self.f1_logo)

        self.f2_nombre = QVBoxLayout()
        self.f2_nombre.setSpacing(0)
        self.f2_nombre.setObjectName(u"f2_nombre")
        self.label_24 = QLabel(self.f_entry_sup)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font11)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.f2_nombre.addWidget(self.label_24)

        self.entrylist_nombre = QLineEdit(self.f_entry_sup)
        self.entrylist_nombre.setObjectName(u"entrylist_nombre")
        self.entrylist_nombre.setMinimumSize(QSize(200, 0))
        self.entrylist_nombre.setFont(font12)

        self.f2_nombre.addWidget(self.entrylist_nombre)


        self.horizontalLayout_61.addLayout(self.f2_nombre)

        self.f3_perio = QVBoxLayout()
        self.f3_perio.setObjectName(u"f3_perio")
        self.label_29 = QLabel(self.f_entry_sup)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font11)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.f3_perio.addWidget(self.label_29)

        self.combol_perio = QComboBox(self.f_entry_sup)
        self.combol_perio.addItem("")
        self.combol_perio.addItem("")
        self.combol_perio.addItem("")
        self.combol_perio.setObjectName(u"combol_perio")
        self.combol_perio.setMinimumSize(QSize(150, 0))
        self.combol_perio.setFont(font12)

        self.f3_perio.addWidget(self.combol_perio)


        self.horizontalLayout_61.addLayout(self.f3_perio)

        self.f4_region = QVBoxLayout()
        self.f4_region.setSpacing(0)
        self.f4_region.setObjectName(u"f4_region")
        self.label_30 = QLabel(self.f_entry_sup)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font11)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.f4_region.addWidget(self.label_30)

        self.combol_region = QComboBox(self.f_entry_sup)
        self.combol_region.addItem("")
        self.combol_region.addItem("")
        self.combol_region.setObjectName(u"combol_region")
        self.combol_region.setMinimumSize(QSize(150, 0))
        self.combol_region.setMaximumSize(QSize(150, 16777215))
        self.combol_region.setFont(font12)

        self.f4_region.addWidget(self.combol_region)


        self.horizontalLayout_61.addLayout(self.f4_region)


        self.verticalLayout_15.addWidget(self.f_entry_sup)

        self.f_entry_inf = QFrame(self.f_entrys)
        self.f_entry_inf.setObjectName(u"f_entry_inf")
        self.f_entry_inf.setFrameShape(QFrame.StyledPanel)
        self.f_entry_inf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.f_entry_inf)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, -1, -1, -1)
        self.f5_sid = QVBoxLayout()
        self.f5_sid.setSpacing(0)
        self.f5_sid.setObjectName(u"f5_sid")
        self.label_25 = QLabel(self.f_entry_inf)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font11)
        self.label_25.setAlignment(Qt.AlignCenter)

        self.f5_sid.addWidget(self.label_25)

        self.entrylist_sid = QLineEdit(self.f_entry_inf)
        self.entrylist_sid.setObjectName(u"entrylist_sid")
        self.entrylist_sid.setMinimumSize(QSize(200, 0))
        self.entrylist_sid.setFont(font12)

        self.f5_sid.addWidget(self.entrylist_sid)


        self.horizontalLayout_22.addLayout(self.f5_sid)

        self.f6_token = QVBoxLayout()
        self.f6_token.setSpacing(0)
        self.f6_token.setObjectName(u"f6_token")
        self.label_26 = QLabel(self.f_entry_inf)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font11)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.f6_token.addWidget(self.label_26)

        self.entrylist__token = QLineEdit(self.f_entry_inf)
        self.entrylist__token.setObjectName(u"entrylist__token")
        self.entrylist__token.setMinimumSize(QSize(200, 0))
        self.entrylist__token.setFont(font12)

        self.f6_token.addWidget(self.entrylist__token)


        self.horizontalLayout_22.addLayout(self.f6_token)

        self.f7_tid = QVBoxLayout()
        self.f7_tid.setSpacing(0)
        self.f7_tid.setObjectName(u"f7_tid")
        self.label_27 = QLabel(self.f_entry_inf)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font11)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.f7_tid.addWidget(self.label_27)

        self.entrylist_tid = QLineEdit(self.f_entry_inf)
        self.entrylist_tid.setObjectName(u"entrylist_tid")
        self.entrylist_tid.setMinimumSize(QSize(200, 0))
        self.entrylist_tid.setFont(font12)

        self.f7_tid.addWidget(self.entrylist_tid)


        self.horizontalLayout_22.addLayout(self.f7_tid)

        self.f8_aid = QVBoxLayout()
        self.f8_aid.setSpacing(0)
        self.f8_aid.setObjectName(u"f8_aid")
        self.label_28 = QLabel(self.f_entry_inf)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font11)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.f8_aid.addWidget(self.label_28)

        self.entrylist_aid = QLineEdit(self.f_entry_inf)
        self.entrylist_aid.setObjectName(u"entrylist_aid")
        self.entrylist_aid.setMinimumSize(QSize(200, 0))
        self.entrylist_aid.setFont(font12)

        self.f8_aid.addWidget(self.entrylist_aid)


        self.horizontalLayout_22.addLayout(self.f8_aid)


        self.verticalLayout_15.addWidget(self.f_entry_inf)

        self.f_entry_inf.raise_()
        self.f_entry_sup.raise_()

        self.horizontalLayout_20.addWidget(self.f_entrys)

        self.f_entrys.raise_()
        self.f_logo.raise_()

        self.verticalLayout_5.addWidget(self.FrameSubContent)

        self.FrameButtons_3 = QFrame(self.FrameContent_Lclientes)
        self.FrameButtons_3.setObjectName(u"FrameButtons_3")
        self.FrameButtons_3.setFrameShape(QFrame.StyledPanel)
        self.FrameButtons_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.FrameButtons_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.f_buttons = QFrame(self.FrameButtons_3)
        self.f_buttons.setObjectName(u"f_buttons")
        self.f_buttons.setFrameShape(QFrame.StyledPanel)
        self.f_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.f_buttons)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_20)

        self.btn_selectcli = QPushButton(self.f_buttons)
        self.btn_selectcli.setObjectName(u"btn_selectcli")
        self.btn_selectcli.setMinimumSize(QSize(200, 0))
        self.btn_selectcli.setMaximumSize(QSize(200, 16777215))
        self.btn_selectcli.setFont(font11)
        self.btn_selectcli.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color: rgb(0, 161, 92);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(40, 209, 118);\n"
"color: rgb(26, 26, 26);\n"
"}")

        self.horizontalLayout_19.addWidget(self.btn_selectcli)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_19)

        self.btn_borrarcli = QPushButton(self.f_buttons)
        self.btn_borrarcli.setObjectName(u"btn_borrarcli")
        self.btn_borrarcli.setMinimumSize(QSize(175, 0))
        self.btn_borrarcli.setMaximumSize(QSize(175, 16777215))
        self.btn_borrarcli.setFont(font11)
        self.btn_borrarcli.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color:rgb(161, 0, 0);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
" QPushButton:hover{\n"
"background-color:rgb(209, 40, 40);\n"
"}")

        self.horizontalLayout_19.addWidget(self.btn_borrarcli)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_21)

        self.btn_aceptarmod = QPushButton(self.f_buttons)
        self.btn_aceptarmod.setObjectName(u"btn_aceptarmod")
        self.btn_aceptarmod.setMinimumSize(QSize(175, 0))
        self.btn_aceptarmod.setMaximumSize(QSize(175, 16777215))
        self.btn_aceptarmod.setFont(font11)
        self.btn_aceptarmod.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color: rgb(0, 161, 92);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
" QPushButton:hover{\n"
"background-color:rgb(40, 209, 118);\n"
"color: rgb(26, 26, 26);\n"
"}")

        self.horizontalLayout_19.addWidget(self.btn_aceptarmod)

        self.horizontalSpacer_58 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_58)


        self.verticalLayout_14.addWidget(self.f_buttons)


        self.verticalLayout_5.addWidget(self.FrameButtons_3)


        self.gridLayout_5.addWidget(self.FrameContent_Lclientes, 2, 1, 1, 2)

        self.horizontalSpacer_18 = QSpacerItem(65, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_18, 2, 3, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_14, 3, 2, 1, 1)

        self.stackedWidget.addWidget(self.listar_clientes)
        self.schedule = QWidget()
        self.schedule.setObjectName(u"schedule")
        self.schedule.setStyleSheet(u"")
        self.gridLayout_7 = QGridLayout(self.schedule)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Tittle_Configuracion = QLabel(self.schedule)
        self.Tittle_Configuracion.setObjectName(u"Tittle_Configuracion")
        self.Tittle_Configuracion.setMinimumSize(QSize(0, 45))
        self.Tittle_Configuracion.setFont(font10)
        self.Tittle_Configuracion.setStyleSheet(u"#Tittle_Configuracion{\n"
"background-color: rgb(237, 65, 36);\n"
"color:white;\n"
"border: 1px solid black;\n"
"}\n"
"")
        self.Tittle_Configuracion.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.Tittle_Configuracion, 0, 0, 1, 3)

        self.verticalSpacer_16 = QSpacerItem(20, 156, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_16, 1, 1, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(363, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_22, 2, 0, 1, 1)

        self.FrameContent_Config_sch = QWidget(self.schedule)
        self.FrameContent_Config_sch.setObjectName(u"FrameContent_Config_sch")
        self.FrameContent_Config_sch.setStyleSheet(u"#FrameContent_Config_sch{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#FrameSubContent_sch{\n"
"background-color: rgb(51, 51, 51);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"padding:5px;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"color:white;\n"
"background-color: rgb(0, 161, 92);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(40, 209, 118);\n"
"color: rgb(26, 26, 26);\n"
"}\n"
"")
        self.verticalLayout_17 = QVBoxLayout(self.FrameContent_Config_sch)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.FrameSubContent_sch = QFrame(self.FrameContent_Config_sch)
        self.FrameSubContent_sch.setObjectName(u"FrameSubContent_sch")
        self.FrameSubContent_sch.setFrameShape(QFrame.StyledPanel)
        self.FrameSubContent_sch.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.FrameSubContent_sch)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.Tittle_Frame = QLabel(self.FrameSubContent_sch)
        self.Tittle_Frame.setObjectName(u"Tittle_Frame")
        self.Tittle_Frame.setMinimumSize(QSize(0, 40))
        self.Tittle_Frame.setFont(font11)
        self.Tittle_Frame.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.Tittle_Frame)


        self.verticalLayout_17.addWidget(self.FrameSubContent_sch)

        self.FrameSubContent_inf = QFrame(self.FrameContent_Config_sch)
        self.FrameSubContent_inf.setObjectName(u"FrameSubContent_inf")
        self.FrameSubContent_inf.setFrameShape(QFrame.StyledPanel)
        self.FrameSubContent_inf.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.FrameSubContent_inf)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_33 = QLabel(self.FrameSubContent_inf)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font11)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_33)

        self.entry_schedule = QLineEdit(self.FrameSubContent_inf)
        self.entry_schedule.setObjectName(u"entry_schedule")
        self.entry_schedule.setMinimumSize(QSize(100, 0))
        self.entry_schedule.setMaximumSize(QSize(100, 16777215))
        self.entry_schedule.setFont(font12)
        self.entry_schedule.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.entry_schedule)


        self.gridLayout_6.addLayout(self.horizontalLayout_24, 3, 0, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_31 = QLabel(self.FrameSubContent_inf)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font11)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_31)

        self.label_schedule = QLabel(self.FrameSubContent_inf)
        self.label_schedule.setObjectName(u"label_schedule")
        self.label_schedule.setMinimumSize(QSize(100, 0))
        self.label_schedule.setMaximumSize(QSize(100, 16777215))
        self.label_schedule.setFont(font12)
        self.label_schedule.setStyleSheet(u"QLabel{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"padding:5px;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"")
        self.label_schedule.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_schedule)


        self.gridLayout_6.addLayout(self.horizontalLayout_23, 1, 0, 1, 1)

        self.f_button = QFrame(self.FrameSubContent_inf)
        self.f_button.setObjectName(u"f_button")
        self.f_button.setFrameShape(QFrame.StyledPanel)
        self.f_button.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.f_button)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_24)

        self.bnt_cargar_sch = QPushButton(self.f_button)
        self.bnt_cargar_sch.setObjectName(u"bnt_cargar_sch")
        self.bnt_cargar_sch.setMinimumSize(QSize(125, 0))
        self.bnt_cargar_sch.setMaximumSize(QSize(150, 16777215))
        self.bnt_cargar_sch.setFont(font11)

        self.horizontalLayout_25.addWidget(self.bnt_cargar_sch)


        self.gridLayout_6.addWidget(self.f_button, 5, 0, 1, 1)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_18, 4, 0, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_15, 2, 0, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_19, 0, 0, 1, 1)


        self.verticalLayout_17.addWidget(self.FrameSubContent_inf)


        self.gridLayout_7.addWidget(self.FrameContent_Config_sch, 2, 1, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(363, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_23, 2, 2, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 156, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_17, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.schedule)
        self.conexion = QWidget()
        self.conexion.setObjectName(u"conexion")
        self.gridLayout_8 = QGridLayout(self.conexion)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_21 = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_21, 3, 1, 1, 1)

        self.verticalSpacer_20 = QSpacerItem(20, 59, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_20, 1, 1, 1, 1)

        self.FrameContent_Config_conx = QWidget(self.conexion)
        self.FrameContent_Config_conx.setObjectName(u"FrameContent_Config_conx")
        self.FrameContent_Config_conx.setMinimumSize(QSize(500, 0))
        self.FrameContent_Config_conx.setStyleSheet(u"#FrameContent_Config_conx{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#FrameSubContent_conx{\n"
"background-color: rgb(51, 51, 51);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"}\n"
"\n"
"#Frame_Console{\n"
"background-color: rgba(51, 51, 51,0.5)\n"
"}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"padding:5px;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"color:white;\n"
"background-color: rgb(0, 161, 92);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(40, 209, 118);\n"
"color: rgb(26, 26, 26);\n"
"}\n"
"")
        self.verticalLayout_20 = QVBoxLayout(self.FrameContent_Config_conx)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.FrameSubContent_conx = QFrame(self.FrameContent_Config_conx)
        self.FrameSubContent_conx.setObjectName(u"FrameSubContent_conx")
        self.FrameSubContent_conx.setMinimumSize(QSize(0, 40))
        self.FrameSubContent_conx.setMaximumSize(QSize(16777215, 40))
        self.FrameSubContent_conx.setFont(font11)
        self.FrameSubContent_conx.setFrameShape(QFrame.StyledPanel)
        self.FrameSubContent_conx.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.FrameSubContent_conx)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.Tittle_Frame_conx = QLabel(self.FrameSubContent_conx)
        self.Tittle_Frame_conx.setObjectName(u"Tittle_Frame_conx")
        self.Tittle_Frame_conx.setFont(font11)
        self.Tittle_Frame_conx.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.Tittle_Frame_conx)


        self.verticalLayout_20.addWidget(self.FrameSubContent_conx)

        self.FrameContent_Entry = QFrame(self.FrameContent_Config_conx)
        self.FrameContent_Entry.setObjectName(u"FrameContent_Entry")
        self.FrameContent_Entry.setFrameShape(QFrame.StyledPanel)
        self.FrameContent_Entry.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.FrameContent_Entry)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.Frame_Entrys = QFrame(self.FrameContent_Entry)
        self.Frame_Entrys.setObjectName(u"Frame_Entrys")
        self.Frame_Entrys.setFrameShape(QFrame.StyledPanel)
        self.Frame_Entrys.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.Frame_Entrys)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_14 = QLabel(self.Frame_Entrys)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(100, 0))
        self.label_14.setMaximumSize(QSize(100, 16777215))
        self.label_14.setFont(font11)

        self.horizontalLayout_26.addWidget(self.label_14)

        self.ip_entry = QLineEdit(self.Frame_Entrys)
        self.ip_entry.setObjectName(u"ip_entry")
        self.ip_entry.setMinimumSize(QSize(300, 0))
        self.ip_entry.setMaximumSize(QSize(300, 16777215))
        self.ip_entry.setFont(font12)

        self.horizontalLayout_26.addWidget(self.ip_entry)


        self.verticalLayout_19.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_32 = QLabel(self.Frame_Entrys)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(100, 0))
        self.label_32.setMaximumSize(QSize(100, 16777215))
        self.label_32.setFont(font11)

        self.horizontalLayout_27.addWidget(self.label_32)

        self.user_entry = QLineEdit(self.Frame_Entrys)
        self.user_entry.setObjectName(u"user_entry")
        self.user_entry.setMinimumSize(QSize(300, 0))
        self.user_entry.setMaximumSize(QSize(300, 16777215))
        self.user_entry.setFont(font12)

        self.horizontalLayout_27.addWidget(self.user_entry)


        self.verticalLayout_19.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_34 = QLabel(self.Frame_Entrys)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(100, 0))
        self.label_34.setMaximumSize(QSize(100, 16777215))
        self.label_34.setFont(font11)

        self.horizontalLayout_28.addWidget(self.label_34)

        self.pass_entry = QLineEdit(self.Frame_Entrys)
        self.pass_entry.setObjectName(u"pass_entry")
        self.pass_entry.setMinimumSize(QSize(300, 0))
        self.pass_entry.setMaximumSize(QSize(300, 16777215))
        self.pass_entry.setFont(font12)

        self.horizontalLayout_28.addWidget(self.pass_entry)


        self.verticalLayout_19.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_35 = QLabel(self.Frame_Entrys)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(100, 0))
        self.label_35.setMaximumSize(QSize(100, 16777215))
        self.label_35.setFont(font11)

        self.horizontalLayout_29.addWidget(self.label_35)

        self.namedb_entry = QLineEdit(self.Frame_Entrys)
        self.namedb_entry.setObjectName(u"namedb_entry")
        self.namedb_entry.setMinimumSize(QSize(300, 0))
        self.namedb_entry.setMaximumSize(QSize(300, 16777215))
        self.namedb_entry.setFont(font12)

        self.horizontalLayout_29.addWidget(self.namedb_entry)


        self.verticalLayout_19.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_36 = QLabel(self.Frame_Entrys)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(100, 0))
        self.label_36.setMaximumSize(QSize(100, 16777215))
        self.label_36.setFont(font11)

        self.horizontalLayout_30.addWidget(self.label_36)

        self.port_entry = QLineEdit(self.Frame_Entrys)
        self.port_entry.setObjectName(u"port_entry")
        self.port_entry.setMinimumSize(QSize(200, 0))
        self.port_entry.setMaximumSize(QSize(300, 16777215))
        self.port_entry.setFont(font12)

        self.horizontalLayout_30.addWidget(self.port_entry)


        self.verticalLayout_19.addLayout(self.horizontalLayout_30)


        self.verticalLayout_23.addWidget(self.Frame_Entrys)

        self.verticalSpacer_22 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_22)

        self.progressBar_2 = QProgressBar(self.FrameContent_Entry)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(24)

        self.verticalLayout_23.addWidget(self.progressBar_2)


        self.verticalLayout_20.addWidget(self.FrameContent_Entry)

        self.Frame_Console = QFrame(self.FrameContent_Config_conx)
        self.Frame_Console.setObjectName(u"Frame_Console")
        self.Frame_Console.setMinimumSize(QSize(0, 100))
        self.Frame_Console.setFrameShape(QFrame.StyledPanel)
        self.Frame_Console.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.Frame_Console)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.Label_Console_conx = QLabel(self.Frame_Console)
        self.Label_Console_conx.setObjectName(u"Label_Console_conx")

        self.verticalLayout_22.addWidget(self.Label_Console_conx)


        self.verticalLayout_20.addWidget(self.Frame_Console)

        self.Frame_buttons = QFrame(self.FrameContent_Config_conx)
        self.Frame_buttons.setObjectName(u"Frame_buttons")
        self.Frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.Frame_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.Frame_buttons)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(-1, 20, -1, -1)
        self.bnt_test_conx = QPushButton(self.Frame_buttons)
        self.bnt_test_conx.setObjectName(u"bnt_test_conx")
        self.bnt_test_conx.setMinimumSize(QSize(100, 0))
        self.bnt_test_conx.setFont(font11)
        self.bnt_test_conx.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color:rgb(31, 106, 165);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
" QPushButton:hover{\n"
"background-color:rgb(38, 130, 202);\n"
"}")

        self.horizontalLayout_31.addWidget(self.bnt_test_conx)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_27)

        self.btn_borrar_conx = QPushButton(self.Frame_buttons)
        self.btn_borrar_conx.setObjectName(u"btn_borrar_conx")
        self.btn_borrar_conx.setMinimumSize(QSize(110, 0))
        self.btn_borrar_conx.setFont(font11)
        self.btn_borrar_conx.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color:rgb(161, 0, 0);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
" QPushButton:hover{\n"
"background-color:rgb(209, 40, 40);\n"
"}")

        self.horizontalLayout_31.addWidget(self.btn_borrar_conx)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_28)

        self.btn_aplicar_conx = QPushButton(self.Frame_buttons)
        self.btn_aplicar_conx.setObjectName(u"btn_aplicar_conx")
        self.btn_aplicar_conx.setMinimumSize(QSize(110, 0))
        self.btn_aplicar_conx.setFont(font11)

        self.horizontalLayout_31.addWidget(self.btn_aplicar_conx)


        self.verticalLayout_20.addWidget(self.Frame_buttons)


        self.gridLayout_8.addWidget(self.FrameContent_Config_conx, 2, 1, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(295, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_26, 2, 2, 1, 1)

        self.Tittle_Configuracion_2 = QLabel(self.conexion)
        self.Tittle_Configuracion_2.setObjectName(u"Tittle_Configuracion_2")
        self.Tittle_Configuracion_2.setMinimumSize(QSize(0, 45))
        self.Tittle_Configuracion_2.setFont(font10)
        self.Tittle_Configuracion_2.setStyleSheet(u"#Tittle_Configuracion_2{\n"
"background-color: rgb(237, 65, 36);\n"
"color:white;\n"
"border: 1px solid black;\n"
"height:40px;\n"
"}\n"
"")
        self.Tittle_Configuracion_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.Tittle_Configuracion_2, 0, 0, 1, 3)

        self.horizontalSpacer_25 = QSpacerItem(296, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_25, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.conexion)
        self.email = QWidget()
        self.email.setObjectName(u"email")
        self.gridLayout_9 = QGridLayout(self.email)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Tittle_Configuracion_3 = QLabel(self.email)
        self.Tittle_Configuracion_3.setObjectName(u"Tittle_Configuracion_3")
        self.Tittle_Configuracion_3.setMinimumSize(QSize(0, 45))
        self.Tittle_Configuracion_3.setFont(font10)
        self.Tittle_Configuracion_3.setStyleSheet(u"#Tittle_Configuracion_3{\n"
"background-color: rgb(237, 65, 36);\n"
"color:white;\n"
"border: 1px solid black;\n"
"height:40px;\n"
"}\n"
"")
        self.Tittle_Configuracion_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.Tittle_Configuracion_3, 0, 0, 1, 3)

        self.verticalSpacer_23 = QSpacerItem(20, 85, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_23, 1, 1, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(142, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_29, 2, 0, 1, 1)

        self.FrameContent_Config_email = QWidget(self.email)
        self.FrameContent_Config_email.setObjectName(u"FrameContent_Config_email")
        self.FrameContent_Config_email.setStyleSheet(u"#FrameContent_Config_email{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#FrameSubContent_email{\n"
"background-color: rgb(51, 51, 51);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"padding:5px;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"color:white;\n"
"background-color: rgb(0, 161, 92);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(40, 209, 118);\n"
"color: rgb(26, 26, 26);\n"
"}\n"
"")
        self.verticalLayout_29 = QVBoxLayout(self.FrameContent_Config_email)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.FrameSubContent_email = QFrame(self.FrameContent_Config_email)
        self.FrameSubContent_email.setObjectName(u"FrameSubContent_email")
        self.FrameSubContent_email.setMaximumSize(QSize(16777215, 40))
        self.FrameSubContent_email.setFrameShape(QFrame.StyledPanel)
        self.FrameSubContent_email.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.FrameSubContent_email)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_13 = QLabel(self.FrameSubContent_email)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font11)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_13)


        self.verticalLayout_29.addWidget(self.FrameSubContent_email)

        self.frame_2 = QFrame(self.FrameContent_Config_email)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_2)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_2 = QTableWidget(self.frame_2)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_28.addWidget(self.tableWidget_2)


        self.verticalLayout_29.addWidget(self.frame_2)

        self.Frame_entrys = QFrame(self.FrameContent_Config_email)
        self.Frame_entrys.setObjectName(u"Frame_entrys")
        self.Frame_entrys.setFrameShape(QFrame.StyledPanel)
        self.Frame_entrys.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.Frame_entrys)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(-1, 40, -1, -1)
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_15 = QLabel(self.Frame_entrys)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font11)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_15)

        self.id_entry = QLineEdit(self.Frame_entrys)
        self.id_entry.setObjectName(u"id_entry")
        self.id_entry.setMinimumSize(QSize(200, 0))
        self.id_entry.setFont(font12)

        self.verticalLayout_25.addWidget(self.id_entry)


        self.horizontalLayout_33.addLayout(self.verticalLayout_25)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_31)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_37 = QLabel(self.Frame_entrys)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font11)
        self.label_37.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_37)

        self.email_entry = QLineEdit(self.Frame_entrys)
        self.email_entry.setObjectName(u"email_entry")
        self.email_entry.setMinimumSize(QSize(250, 0))
        self.email_entry.setFont(font12)

        self.verticalLayout_26.addWidget(self.email_entry)


        self.horizontalLayout_33.addLayout(self.verticalLayout_26)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_32)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_38 = QLabel(self.Frame_entrys)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font11)
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_38)

        self.asign_entry = QLineEdit(self.Frame_entrys)
        self.asign_entry.setObjectName(u"asign_entry")
        self.asign_entry.setMinimumSize(QSize(250, 0))
        self.asign_entry.setFont(font12)

        self.verticalLayout_27.addWidget(self.asign_entry)


        self.horizontalLayout_33.addLayout(self.verticalLayout_27)


        self.verticalLayout_29.addWidget(self.Frame_entrys)

        self.verticalSpacer_25 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_25)

        self.f_buttons_2 = QFrame(self.FrameContent_Config_email)
        self.f_buttons_2.setObjectName(u"f_buttons_2")
        self.f_buttons_2.setFrameShape(QFrame.StyledPanel)
        self.f_buttons_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.f_buttons_2)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.btn_email_agregar = QPushButton(self.f_buttons_2)
        self.btn_email_agregar.setObjectName(u"btn_email_agregar")
        self.btn_email_agregar.setMinimumSize(QSize(120, 0))
        self.btn_email_agregar.setFont(font11)

        self.horizontalLayout_32.addWidget(self.btn_email_agregar)

        self.horizontalSpacer_33 = QSpacerItem(97, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_33)

        self.btn_email_mod = QPushButton(self.f_buttons_2)
        self.btn_email_mod.setObjectName(u"btn_email_mod")
        self.btn_email_mod.setMinimumSize(QSize(120, 0))
        self.btn_email_mod.setFont(font11)
        self.btn_email_mod.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color:rgb(31, 106, 165);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
" QPushButton:hover{\n"
"background-color:rgb(38, 130, 202);\n"
"}")

        self.horizontalLayout_32.addWidget(self.btn_email_mod)

        self.horizontalSpacer_34 = QSpacerItem(97, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_34)

        self.btn_email_borrar = QPushButton(self.f_buttons_2)
        self.btn_email_borrar.setObjectName(u"btn_email_borrar")
        self.btn_email_borrar.setMinimumSize(QSize(120, 0))
        self.btn_email_borrar.setFont(font11)
        self.btn_email_borrar.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"background-color:rgb(161, 0, 0);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
" QPushButton:hover{\n"
"background-color:rgb(209, 40, 40);\n"
"}")

        self.horizontalLayout_32.addWidget(self.btn_email_borrar)

        self.horizontalSpacer_35 = QSpacerItem(97, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_35)

        self.btn_email_asign = QPushButton(self.f_buttons_2)
        self.btn_email_asign.setObjectName(u"btn_email_asign")
        self.btn_email_asign.setMinimumSize(QSize(120, 0))
        self.btn_email_asign.setFont(font11)

        self.horizontalLayout_32.addWidget(self.btn_email_asign)


        self.verticalLayout_29.addWidget(self.f_buttons_2)


        self.gridLayout_9.addWidget(self.FrameContent_Config_email, 2, 1, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(142, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_30, 2, 2, 1, 1)

        self.verticalSpacer_24 = QSpacerItem(20, 84, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_24, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.email)
        self.informes = QWidget()
        self.informes.setObjectName(u"informes")
        self.gridLayout_14 = QGridLayout(self.informes)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.Tittle_Configuracion_4 = QLabel(self.informes)
        self.Tittle_Configuracion_4.setObjectName(u"Tittle_Configuracion_4")
        self.Tittle_Configuracion_4.setMinimumSize(QSize(0, 45))
        self.Tittle_Configuracion_4.setFont(font10)
        self.Tittle_Configuracion_4.setStyleSheet(u"#Tittle_Configuracion_4{\n"
"background-color: rgb(237, 65, 36);\n"
"color:white;\n"
"border: 1px solid black;\n"
"height:40px;\n"
"}\n"
"")
        self.Tittle_Configuracion_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.Tittle_Configuracion_4, 0, 0, 1, 3)

        self.verticalSpacer_52 = QSpacerItem(20, 183, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_52, 1, 1, 1, 1)

        self.FrameContent_Informes = QWidget(self.informes)
        self.FrameContent_Informes.setObjectName(u"FrameContent_Informes")
        self.FrameContent_Informes.setStyleSheet(u"#FrameContent_Informes{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#FrameSubContent_Informes{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QDateEdit{\n"
"background-color: rgba(51, 51, 51,0.2);\n"
"padding:5px;\n"
"border-radius:10px;\n"
"color:white;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: rgb(217, 217, 217);\n"
"    border: none;\n"
"    selection-background-color: rgba(51, 51, 51, 0.5);\n"
"    outline: none;\n"
"}\n"
"\n"
"QPushButton{\n"
"color:white;\n"
"background-color: rgb(0, 161, 92);\n"
"padding:8px;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(40, 209, 118);\n"
"color: rgb(26, 26, 26);\n"
"}")
        self.horizontalLayout_78 = QHBoxLayout(self.FrameContent_Informes)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.FrameSubContent_Informes = QFrame(self.FrameContent_Informes)
        self.FrameSubContent_Informes.setObjectName(u"FrameSubContent_Informes")
        self.FrameSubContent_Informes.setMinimumSize(QSize(475, 0))
        self.FrameSubContent_Informes.setMaximumSize(QSize(16777215, 16777215))
        self.FrameSubContent_Informes.setFrameShape(QFrame.StyledPanel)
        self.FrameSubContent_Informes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.FrameSubContent_Informes)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.FrameSubContent_1 = QFrame(self.FrameSubContent_Informes)
        self.FrameSubContent_1.setObjectName(u"FrameSubContent_1")
        self.FrameSubContent_1.setFrameShape(QFrame.StyledPanel)
        self.FrameSubContent_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.FrameSubContent_1)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.label_58 = QLabel(self.FrameSubContent_1)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(150, 0))
        self.label_58.setFont(font11)

        self.horizontalLayout_76.addWidget(self.label_58)

        self.combo_clientes_inf = QComboBox(self.FrameSubContent_1)
        self.combo_clientes_inf.setObjectName(u"combo_clientes_inf")
        self.combo_clientes_inf.setMinimumSize(QSize(150, 35))
        self.combo_clientes_inf.setMaximumSize(QSize(16777215, 35))
        self.combo_clientes_inf.setFont(font12)

        self.horizontalLayout_76.addWidget(self.combo_clientes_inf)

        self.horizontalSpacer_65 = QSpacerItem(133, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_76.addItem(self.horizontalSpacer_65)


        self.verticalLayout_55.addWidget(self.FrameSubContent_1)

        self.verticalSpacer_50 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_55.addItem(self.verticalSpacer_50)

        self.FrameSubContent_2 = QFrame(self.FrameSubContent_Informes)
        self.FrameSubContent_2.setObjectName(u"FrameSubContent_2")
        self.FrameSubContent_2.setFrameShape(QFrame.StyledPanel)
        self.FrameSubContent_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.FrameSubContent_2)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.label_8 = QLabel(self.FrameSubContent_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(150, 0))
        self.label_8.setFont(font11)

        self.horizontalLayout_77.addWidget(self.label_8)

        self.fecha_inicio_inf = QDateEdit(self.FrameSubContent_2)
        self.fecha_inicio_inf.setObjectName(u"fecha_inicio_inf")
        self.fecha_inicio_inf.setMinimumSize(QSize(120, 30))
        self.fecha_inicio_inf.setMaximumSize(QSize(120, 30))
        self.fecha_inicio_inf.setFont(font12)
        self.fecha_inicio_inf.setStyleSheet(u"QCalendarWidget {\n"
"    background-color: rgb(165, 165, 165);\n"
"}\n"
"\n"
"QCalendarWidget QTableView {\n"
"    background-color:rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: white;\n"
"	font-size: 12px;\n"
"	background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"	width: 150px;\n"
"	left: 20px;\n"
"	color: white;\n"
"	font-size: 15px;\n"
"	background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"	background-color:  rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"")
        self.fecha_inicio_inf.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.fecha_inicio_inf.setCalendarPopup(True)

        self.horizontalLayout_77.addWidget(self.fecha_inicio_inf)

        self.fecha_fin_inf = QDateEdit(self.FrameSubContent_2)
        self.fecha_fin_inf.setObjectName(u"fecha_fin_inf")
        self.fecha_fin_inf.setMinimumSize(QSize(120, 30))
        self.fecha_fin_inf.setMaximumSize(QSize(120, 30))
        self.fecha_fin_inf.setFont(font12)
        self.fecha_fin_inf.setStyleSheet(u"QCalendarWidget {\n"
"    background-color: rgb(165, 165, 165);\n"
"}\n"
"\n"
"QCalendarWidget QTableView {\n"
"    background-color:rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"	color: white;\n"
"	font-size: 12px;\n"
"	background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QMenu {\n"
"	width: 150px;\n"
"	left: 20px;\n"
"	color: white;\n"
"	font-size: 15px;\n"
"	background-color: rgb(100, 100, 100);\n"
"}\n"
"\n"
"QCalendarWidget QWidget {\n"
"	background-color:  rgb(47, 47, 47);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"background-color:  rgb(197, 197, 197);\n"
"}\n"
"\n"
"")
        self.fecha_fin_inf.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.fecha_fin_inf.setCalendarPopup(True)

        self.horizontalLayout_77.addWidget(self.fecha_fin_inf)

        self.horizontalSpacer_67 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_77.addItem(self.horizontalSpacer_67)


        self.verticalLayout_55.addWidget(self.FrameSubContent_2)

        self.verticalSpacer_49 = QSpacerItem(20, 130, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_55.addItem(self.verticalSpacer_49)

        self.FrameSubContent_3 = QFrame(self.FrameSubContent_Informes)
        self.FrameSubContent_3.setObjectName(u"FrameSubContent_3")
        self.FrameSubContent_3.setFrameShape(QFrame.StyledPanel)
        self.FrameSubContent_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.FrameSubContent_3)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalSpacer_64 = QSpacerItem(319, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_75.addItem(self.horizontalSpacer_64)

        self.pushButton = QPushButton(self.FrameSubContent_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(120, 35))
        self.pushButton.setMaximumSize(QSize(16777215, 35))
        self.pushButton.setFont(font11)

        self.horizontalLayout_75.addWidget(self.pushButton)


        self.verticalLayout_55.addWidget(self.FrameSubContent_3)


        self.horizontalLayout_78.addWidget(self.FrameSubContent_Informes)

        self.horizontalSpacer_66 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_78.addItem(self.horizontalSpacer_66)


        self.gridLayout_14.addWidget(self.FrameContent_Informes, 2, 1, 2, 1)

        self.horizontalSpacer_69 = QSpacerItem(391, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_69, 2, 2, 1, 1)

        self.horizontalSpacer_68 = QSpacerItem(391, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_68, 3, 0, 1, 1)

        self.verticalSpacer_51 = QSpacerItem(20, 183, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_51, 4, 1, 1, 1)

        self.stackedWidget.addWidget(self.informes)

        self.horizontalLayout_88.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.FrameStacked)

        self.FrameStacked.raise_()
        self.FrameSubMenu.raise_()

        self.horizontalLayout.addWidget(self.FrameContent)


        self.verticalLayout.addWidget(self.FrameInf)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bnt_menu.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.Menu.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.bnt_min.setText("")
        self.bnt_maximize.setText("")
        self.bnt_minimize.setText("")
        self.bnt_close.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"SOCcrate", None))
        self.btn_inicio.setText(QCoreApplication.translate("MainWindow", u"  INICIO", None))
        self.btn_clientes.setText(QCoreApplication.translate("MainWindow", u"CLIENTES", None))
        self.btn_graph.setText(QCoreApplication.translate("MainWindow", u"GR\u00c1FICOS", None))
        self.btn_informes.setText(QCoreApplication.translate("MainWindow", u"INFORMES", None))
        self.btn_config.setText(QCoreApplication.translate("MainWindow", u"CONFIGURACI\u00d3N", None))
        self.btn_help.setText(QCoreApplication.translate("MainWindow", u"AYUDA", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"v2.0", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btn_closecli.setText("")
        self.btn_addcli.setText(QCoreApplication.translate("MainWindow", u"Cargar Clientes", None))
        self.btn_listcli.setText(QCoreApplication.translate("MainWindow", u"Listar Clientes", None))
        self.btn_hashes.setText(QCoreApplication.translate("MainWindow", u"Hashes", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Informes", None))
        self.btn_closeinf.setText("")
        self.btn_crear_infor.setText(QCoreApplication.translate("MainWindow", u"Crear Informes", None))
        self.btn_abrir_infor.setText(QCoreApplication.translate("MainWindow", u"Abrir Informes", None))
        self.btn_abrir_csv_2.setText(QCoreApplication.translate("MainWindow", u"Abrir CSV", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.btn_closeconf.setText("")
        self.btn_abrir_logs_2.setText(QCoreApplication.translate("MainWindow", u"Abrir Logs", None))
        self.btn_schedule.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.btn_conexion.setText(QCoreApplication.translate("MainWindow", u"Conexi\u00f3n", None))
        self.btn_email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"  SOCcrate  ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Versi\u00f3n 2.0", None))
        self.Label_Content_Inicio.setText(QCoreApplication.translate("MainWindow", u"En esta seccion puede encontrar los accesos directos \n"
" a los directorios nombrados segun su necesidad.", None))
        self.btn_abrir_logs.setText(QCoreApplication.translate("MainWindow", u"ABRIR LOGS", None))
        self.btn_abrir_informes.setText(QCoreApplication.translate("MainWindow", u"ABRIR INFORMES", None))
        self.btn_abrir_csv.setText(QCoreApplication.translate("MainWindow", u"ABRIR CSV", None))
        self.btn_dashboard.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.Tittle_Inicio.setText(QCoreApplication.translate("MainWindow", u"INICIO", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Histograma", None))
        self.Label_Histo.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Tipo de dato:", None))
        self.histo_tdato_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Devices", None))
        self.histo_tdato_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Exploits", None))
        self.histo_tdato_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Threats", None))

        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Columna:", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Fecha inicio:", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Fecha fin:", None))
        self.TOCAME.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Barras", None))
        self.Label_Barras1.setText(QCoreApplication.translate("MainWindow", u"img", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Tipo de dato:", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Columna:", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Fecha inicio:", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Fecha fin:", None))
        self.barras1.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.Label_Barras.setText(QCoreApplication.translate("MainWindow", u"Barras", None))
        self.Label_Barras2.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Tipo de dato:", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Columna:", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Fecha inicio:", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Fecha fin:", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Torta", None))
        self.Label_Torta.setText(QCoreApplication.translate("MainWindow", u"IMG", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Tipo de dato:", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Columna:", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Fecha inicio:", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Fecha fin:", None))
        self.Tittle_Dashboard.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.Tittle_Hashes.setText(QCoreApplication.translate("MainWindow", u"HASHES", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btn_hashes_aadir.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir CSV", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Tipo de lista:", None))
        self.tipolista_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Global Quarentine", None))
        self.tipolista_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Global Safe", None))

        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Categor\u00eda:", None))
        self.category_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"AdminTool", None))
        self.category_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"CommercialSoftware", None))
        self.category_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Drivers", None))
        self.category_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"InternalApplication", None))
        self.category_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"OperatingSystem", None))
        self.category_combo.setItemText(5, QCoreApplication.translate("MainWindow", u"SecuritySoftware", None))
        self.category_combo.setItemText(6, QCoreApplication.translate("MainWindow", u"None", None))

        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Motivo:", None))
        self.btn_hashes_select.setText(QCoreApplication.translate("MainWindow", u"Seleccionar", None))
        self.btn_hashes_borrar.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.btn_hashes_cargar.setText(QCoreApplication.translate("MainWindow", u"Cargar", None))
        self.Tittle_Ayuda.setText(QCoreApplication.translate("MainWindow", u"AYUDA", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Descargate el manual de usuario para despejar tus dudas.", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Tambi\u00e9n podes acceder al mismo mediante tu cuenta en Helpjuice para verlo online.", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Dirigete a la opcion que prefieras mediante los botones.", None))
        self.btn_descarga.setText(QCoreApplication.translate("MainWindow", u"  Dercarga Manual", None))
        self.btn_readonline.setText(QCoreApplication.translate("MainWindow", u"Leer Manual Online   ", None))
        self.Tittle_Graficos.setText(QCoreApplication.translate("MainWindow", u"GR\u00c1FICOS PERSONALIZADOS", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tipo de dato:", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Tipo de gr\u00e1fico:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Columna:", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Rango de fechas:", None))
        self.label_grafico.setText("")
        self.btn_grafico_crear.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.btn_graficos_borrar.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.btn_graficos_exportar.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.Tittle_Cclientes.setText(QCoreApplication.translate("MainWindow", u"CARGAR CLIENTES", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Tenant ID:  ", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Token:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Periodicidad:", None))
        self.perio_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Diario", None))
        self.perio_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Semanal", None))
        self.perio_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Mensual", None))

        self.btn_cargacli.setText(QCoreApplication.translate("MainWindow", u"CARGAR", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Nombre: ", None))
        self.entry_nombre.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Region:", None))
        self.regio_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"NA", None))
        self.regio_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"SA", None))

        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Logo:", None))
        self.label_logo.setText("")
        self.btn_agregar_logo.setText(QCoreApplication.translate("MainWindow", u"Agregar Imagen", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Aplication ID:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Secret ID:", None))
        self.Tittle_Lclientes.setText(QCoreApplication.translate("MainWindow", u"LISTAR CLIENTES", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Logo", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Aplication ID", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tenant ID", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Secret ID", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Token", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Periodicidad", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Region", None));
        self.show_logo.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Logo", None))
        self.btn_act_logo.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Periodicidad", None))
        self.combol_perio.setItemText(0, QCoreApplication.translate("MainWindow", u"Diario", None))
        self.combol_perio.setItemText(1, QCoreApplication.translate("MainWindow", u"Semanal", None))
        self.combol_perio.setItemText(2, QCoreApplication.translate("MainWindow", u"Mensual", None))

        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Regi\u00f3n", None))
        self.combol_region.setItemText(0, QCoreApplication.translate("MainWindow", u"NA", None))
        self.combol_region.setItemText(1, QCoreApplication.translate("MainWindow", u"SA", None))

        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Secret ID", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Token", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Tenant ID", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Aplication ID", None))
        self.btn_selectcli.setText(QCoreApplication.translate("MainWindow", u"Seleccionar Cliente", None))
        self.btn_borrarcli.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.btn_aceptarmod.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.Tittle_Configuracion.setText(QCoreApplication.translate("MainWindow", u"CONFIGURACI\u00d3N", None))
        self.Tittle_Frame.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n horaria del schedule", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Ingrese el nuevo horario:", None))
        self.entry_schedule.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Horario actual:", None))
        self.label_schedule.setText("")
        self.bnt_cargar_sch.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.Tittle_Frame_conx.setText(QCoreApplication.translate("MainWindow", u"Conexi\u00f3n DataBase", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"IP:", None))
        self.ip_entry.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Nombre db:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Puerto:", None))
        self.Label_Console_conx.setText(QCoreApplication.translate("MainWindow", u"Console", None))
        self.bnt_test_conx.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.btn_borrar_conx.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.btn_aplicar_conx.setText(QCoreApplication.translate("MainWindow", u"Aplicar", None))
        self.Tittle_Configuracion_2.setText(QCoreApplication.translate("MainWindow", u"CONFIGURACI\u00d3N", None))
        self.Tittle_Configuracion_3.setText(QCoreApplication.translate("MainWindow", u"CONFIGURACI\u00d3N", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Email Autom\u00e1ticos", None))
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Nueva columna", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Asignado", None));
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Asignado", None))
        self.btn_email_agregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.btn_email_mod.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.btn_email_borrar.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.btn_email_asign.setText(QCoreApplication.translate("MainWindow", u"Asignar", None))
        self.Tittle_Configuracion_4.setText(QCoreApplication.translate("MainWindow", u"INFORMES", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Rango de fechas:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Generar", None))
    # retranslateUi

