from .ui_interface import  *
from .resources2_rc import *
from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore, QtGui, QtWidgets
from .Presentacion_Dialog import Dialogo
from .Presentacion_Ayuda import Manual
from .Presentacion_listar_clientes import ListaClientes
from .Presentacion_cargar_clientes import CargarClientes
from .Presentacion_Schedule_Config import Schedule
from .Presentacion_Conexion_Congif import ConexionConfig
from .Presentacion_Hashes import Hashes
from .Presentacion_graficos_personalizados import GraficosPersonalizados
from .Presentacion_Dashboard import Dashboard_Page

class App(QMainWindow):
        def __init__(self):
            super().__init__()
            self.ui = Ui_MainWindow() 
            self.ui.setupUi(self)
            self.setWindowTitle("SOCcrate")
            #eliminar barra y de titulo - opacidad
            self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.setWindowOpacity(1)
            #SizeGrip
            self.gripSize = 10
            self.grip = QtWidgets.QSizeGrip(self)
            self.grip.resize(self.gripSize, self.gripSize)

            # mover ventana
            self.ui.FrameBar.mouseMoveEvent = self.mover_ventana   
            
            #acceder a las paginas
            self.ui.btn_inicio.clicked.connect(self.show_dashboard_widget)				
            
            self.ui.btn_addcli.clicked.connect(self.show_cargar_clientes_widget)
            self.ui.btn_listcli.clicked.connect(self.show_listar_clientes_widget)
            self.ui.btn_hashes.clicked.connect(self.show_hashes_widget)
            self.ui.btn_schedule.clicked.connect(self.show_schedule_widget)
            self.ui.btn_conexion.clicked.connect(self.show_conexion_congif_widget)
            self.ui.btn_graph.clicked.connect(self.show_graficos_personalizados_widget)
            self.ui.btn_help.clicked.connect(self.show_ayuda_widget)
            self.ui.btn_crear_infor.clicked.connect(self.show_informes_widget)
            
            self.ui.btn_email.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.email))				

            #control barra de titulos
            self.ui.bnt_min.clicked.connect(self.control_bt_minimizar)		
            self.ui.bnt_minimize.clicked.connect(self.control_bt_normal)
            self.ui.bnt_maximize.clicked.connect(self.control_bt_maximizar)
            self.ui.bnt_close.clicked.connect(lambda: self.close())

            self.ui.bnt_minimize.hide()

            self.ui.FrameStacked.mousePressEvent = self.ocultar_menues

            #menu lateral
            self.ui.bnt_menu.clicked.connect(self.mover_menu)

            #menu lateral clientes
            self.ui.btn_clientes.clicked.connect(self.menu_clientes)
            self.ui.btn_closecli.clicked.connect(self.ocultar_frame)

            #menu lateral configuracion
            self.ui.btn_config.clicked.connect(self.menu_config)
            self.ui.btn_closeconf.clicked.connect(self.ocultar_frame2)

            #menu lateral informes
            self.ui.btn_informes.clicked.connect(self.menu_informes)
            self.ui.btn_closeinf.clicked.connect(self.ocultar_frame3)

            self.current_pos = self.pos()
        
        def mousePressEvent(self, event):
            self.clickPosition = event.globalPos()
            pass

############################# H A S H E S ##############################################
        def show_hashes_widget(self):
            self.ui.stackedWidget.setCurrentWidget(self.ui.hashes)
            self.hashes = Hashes(self.ui)
            self.hashes.listar_clientes_hashes()

            self.ui.btn_hashes_select.clicked.connect(self.hashes.mostrar_usuarios_seleccionados)
            self.ui.btn_hashes_aadir.clicked.connect(self.hashes.open_file)
            self.ui.btn_hashes_cargar.clicked.connect(self.hashes.cargar_hashes)
            self.ui.btn_hashes_borrar.clicked.connect(self.hashes.eliminar_data)

############################# L I S T A R   C L I E N T E S #############################
        def show_listar_clientes_widget(self):
            self.ui.stackedWidget.setCurrentWidget(self.ui.listar_clientes)
            self.lista_clientes = ListaClientes(self.ui.tableWidget, self.ui)
            self.lista_clientes.listar_clientes()

            self.ui.btn_aceptarmod.setVisible(False)
            self.ui.btn_borrarcli.setVisible(False)
            self.ui.btn_act_logo.setVisible(False)
          
            self.ui.btn_selectcli.clicked.connect(self.lista_clientes.cliente_seleccionado)
            self.ui.btn_aceptarmod.clicked.connect(self.lista_clientes.modificar_cliente)
            self.ui.btn_borrarcli.clicked.connect(self.lista_clientes.borrar_cliente)
            self.ui.btn_act_logo.clicked.connect(self.lista_clientes.seleccionar_imagen)

############################# C A R G A R   C L I E N T E S #############################
        def show_cargar_clientes_widget(self):            
            self.ui.stackedWidget.setCurrentWidget(self.ui.cargar_clientes)
            self.cargar_clientes = CargarClientes(self.ui)
 
            self.ui.btn_agregar_logo.clicked.connect(self.cargar_clientes.seleccionar_imagen)
            self.ui.btn_cargacli.clicked.connect(self.cargar_clientes.agregar_cliente)

############################# S C H E D U L E ##########################################################
        def show_schedule_widget(self):
            self.ui.stackedWidget.setCurrentWidget(self.ui.schedule)
            self.schedule_conf = Schedule(self.ui)

            self.schedule_conf.mostrar_horario() 
            self.ui.bnt_cargar_sch.clicked.connect(self.schedule_conf.guardar_horario)

############################# C O N E X I O N ##########################################################
        def show_conexion_congif_widget(self):   
            self.ui.stackedWidget.setCurrentWidget(self.ui.conexion)
            self.conexion_conf = ConexionConfig(self.ui)

            self.ui.pass_entry.setEchoMode(QLineEdit.Password)

            # Validar la dirección IP
            validator = QtGui.QRegExpValidator(QtCore.QRegExp(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'), self.ui.ip_entry)
            self.ui.ip_entry.setValidator(validator)
            self.ui.ip_entry.textChanged.connect(self.conexion_conf.validar_ip)
            self.ui.ip_entry.setPlaceholderText("Ingrese solo números y puntos")

            # Establecer el validador para el campo del puerto
            validator = QtGui.QIntValidator(0, 65535, self.ui.port_entry)
            self.ui.port_entry.setValidator(validator)
            self.ui.port_entry.textChanged.connect(self.conexion_conf.validar_puerto)
            self.ui.port_entry.setPlaceholderText("Ingrese solo números")

            self.ui.bnt_test_conx.clicked.connect(self.conexion_conf.test_clicked)
            self.ui.btn_borrar_conx.clicked.connect(self.conexion_conf.borrar_clicked)
            self.ui.btn_aplicar_conx.clicked.connect(self.conexion_conf.asignar_clicked)

############################# G R A F I C O S   P E R S O N A L I Z A D O S #############################
        def show_graficos_personalizados_widget(self):   
            self.ui.stackedWidget.setCurrentWidget(self.ui.graficos)
            self.graficos_p = GraficosPersonalizados(self.ui)
            
            # Conectar la señal currentTextChanged del QComboBox graficos_tipod_combo a la función actualizar_graficos
            if self.ui.graficos_tipod_combo.count() == 0:
                self.ui.graficos_tipod_combo.addItems(["", "Devices", "Exploits", "Threats"])
                self.ui.graficos_tipod_combo.setCurrentIndex(0)
            
            for i in range(self.ui.graficos_tipod_combo.count()):
                print(self.ui.graficos_tipod_combo.itemText(i))
            self.ui.graficos_tipod_combo.currentTextChanged.connect(self.graficos_p.actualizar_graficos)

            # Conectar la señal currentIndexChanged del QComboBox graficos_tipod_combo a la función eliminar_vacio
            self.ui.graficos_tipod_combo.currentIndexChanged.connect(self.graficos_p.eliminar_vacio)

            self.graficos_p.cargar_clientes_combo()

            self.ui.btn_grafico_crear.clicked.connect(self.graficos_p.crear_grafico)
            self.ui.btn_graficos_borrar.clicked.connect(self.graficos_p.borrar_grafico)
            self.ui.btn_graficos_exportar.clicked.connect(self.graficos_p.exportar_grafico)

############################# A Y U D A ########################################################## 
        def show_ayuda_widget(self): 
            self.ui.stackedWidget.setCurrentWidget(self.ui.ayuda)
            self.manual = Manual()

            self.ui.btn_descarga.clicked.connect(self.manual.descargar_archivo)
            self.ui.btn_readonline.clicked.connect(self.manual.abrir_enlace)

############################# F I L E D I A L O G ################################################# 
        def show_informes_widget(self):    
            self.ui.stackedWidget.setCurrentWidget(self.ui.informes)
            self.dialogo = Dialogo()

            self.ui.btn_abrir_infor.clicked.connect(self.dialogo.abrir_informes)
            self.ui.btn_abrir_csv_2.clicked.connect(self.dialogo.abrir_csv)
            self.ui.btn_abrir_logs_2.clicked.connect(self.dialogo.abrir_logs)

############################# D A S H B O A R D ################################################# 
        def show_dashboard_widget(self):    
            self.ui.stackedWidget.setCurrentWidget(self.ui.dashboard)
            self.dashboard = Dashboard_Page(self.ui)

            self.dashboard.clintes_dashboard()
            self.dashboard.show_histograma()
            #self.dashboard.show_barras1()

            self.ui.histo_tdato_combo.currentIndexChanged.connect(self.dashboard.actualizar_columnas_histo)
            self.ui.barras1_tdato_combo.currentIndexChanged.connect(self.dashboard.actualizar_columnas_barras1)
            self.ui.barras2_tdato_combo.currentIndexChanged.connect(self.dashboard.actualizar_columnas_barras2)
            self.ui.torta_tdato_combo.currentIndexChanged.connect(self.dashboard.actualizar_columnas_torta)
            
            self.ui.TOCAME.clicked.connect(self.dashboard.show_histograma_personalizado)
            self.ui.barras1.clicked.connect(self.dashboard.show_barras1_personalizado)
            #self.dashboard.show_histograma_personalizado()

            #self.dashboard.plot_histogram()

            self.ui.barras1_tdato_combo.currentIndexChanged.connect(self.dashboard.eliminar_vacio_barras1)
            self.ui.barras2_tdato_combo.currentIndexChanged.connect(self.dashboard.eliminar_vacio_barras2)
            self.ui.torta_tdato_combo.currentIndexChanged.connect(self.dashboard.eliminar_vacio_torta)

        def control_bt_minimizar(self):
            self.showMinimized()		

        def  control_bt_normal(self): 
            self.showNormal()		
            self.ui.bnt_minimize.hide()
            self.ui.bnt_maximize.show()

        def  control_bt_maximizar(self): 
            self.showMaximized()
            self.ui.bnt_maximize.hide()
            self.ui.bnt_minimize.show()

        #Ajustar tamaño de la apertura de los menus en ventana normal
        def adjustWindowSize_min(self):
            #self.adjustSize()
            self.animation = QPropertyAnimation(self, b'size')
            self.animation.setDuration(0)  # Duración de la animación en milisegundos
            self.animation.setStartValue(self.size())
            self.animation.setEndValue(self.minimumSize())
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

        #Ajustar tamaño de la apertura de los menus en ventana maximizado
        def adjustWindowSize_max(self):
            screen_rect = self.screen().availableGeometry()
            self.setGeometry(screen_rect)
            self.showMaximized()

        #animacion apertura menu en ventana
        def run_animation(self, widget, width, extender, callback):
            self.animacion = QPropertyAnimation(widget, b'minimumWidth')
            self.animacion.setDuration(80)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
            self.animacion.finished.connect(callback)

        def mover_menu(self):
            if self.isMaximized():            
                width = self.ui.FrameMenu.width()
                normal = 0
                if width == 0:
                    extender = 250
                else:
                    extender = normal
                self.run_animation(self.ui.FrameMenu, width, extender, self.adjustWindowSize_max)
            else:
                width = self.ui.FrameMenu.width()
                normal = 0
                if width == 0:
                    extender = 250
                else:
                    extender = normal
                self.run_animation(self.ui.FrameMenu, width, extender, self.adjustWindowSize_min)

        def ocultar_menu(self):
            if self.isMaximized():
                width = self.ui.FrameMenu.width()
                normal = 0
                if width == 0:
                    return
                self.run_animation(self.ui.FrameMenu, width, normal, self.adjustWindowSize_max)
            else:
                width = self.ui.FrameMenu.width()
                normal = 0
                if width == 0:
                    return
                self.run_animation(self.ui.FrameMenu, width, normal, self.adjustWindowSize_min)

        def ocultar_frame(self):
            if self.isMaximized():
                width = self.ui.FrameClientes.width()
                normal = 0
                if width == 0:
                    return
                self.run_animation(self.ui.FrameClientes, width, normal, self.adjustWindowSize_max)
            else:
                width = self.ui.FrameClientes.width()
                normal = 0
                if width == 0:
                    return
                self.run_animation(self.ui.FrameClientes, width, normal, self.adjustWindowSize_min)

        def menu_clientes(self):
            if self.isMaximized():
                width = self.ui.FrameClientes.width()
                normal = 0
                if width == 0:
                    extender = 250
                else:
                    extender = normal
                    self.ocultar_frame()
                self.run_animation(self.ui.FrameClientes, width, extender, self.adjustWindowSize_max)
            else:
                width = self.ui.FrameClientes.width()
                normal = 0
                if width == 0:
                    extender = 250
                else:
                    extender = normal
                    self.ocultar_frame()
                self.run_animation(self.ui.FrameClientes, width, extender, self.adjustWindowSize_min)


        def ocultar_frame2(self):
            if self.isMaximized():            
                width = self.ui.FrameConfig.width()
                normal = 0
                if width == 0:
                    return
                self.run_animation(self.ui.FrameConfig, width, normal, self.adjustWindowSize_max)
            else:
                width = self.ui.FrameConfig.width()
                normal = 0
                if width == 0:
                    return
                self.run_animation(self.ui.FrameConfig, width, normal, self.adjustWindowSize_min)

        def menu_config(self):
            if self.isMaximized():                        
                width = self.ui.FrameConfig.width()
                normal = 0
                if width == 0:
                    extender = 250
                else:
                    extender = normal
                    self.ocultar_frame2()
                self.run_animation(self.ui.FrameConfig, width, extender, self.adjustWindowSize_max)
            else:
                width = self.ui.FrameConfig.width()
                normal = 0
                if width == 0:
                    extender = 250
                else:
                    extender = normal
                    self.ocultar_frame2()
                self.run_animation(self.ui.FrameConfig, width, extender, self.adjustWindowSize_min)
            
        def ocultar_frame3(self):
            if self.isMaximized(): 
                width = self.ui.FrameInformes.width()
                normal = 0
                if width == 0:
                    return
                self.run_animation(self.ui.FrameInformes, width, normal, self.adjustWindowSize_max)
            else:
                width = self.ui.FrameInformes.width()
                normal = 0
                if width == 0:
                    return
                self.run_animation(self.ui.FrameInformes, width, normal, self.adjustWindowSize_min)

        def menu_informes(self):
            if self.isMaximized():    
                width = self.ui.FrameInformes.width()
                normal = 0
                if width == 0:
                    extender = 250
                else:
                    extender = normal
                    self.ocultar_frame3()
                self.run_animation(self.ui.FrameInformes, width, extender, self.adjustWindowSize_max)
            else:
                width = self.ui.FrameInformes.width()
                normal = 0
                if width == 0:
                    extender = 250
                else:
                    extender = normal
                    self.ocultar_frame3()
                self.run_animation(self.ui.FrameInformes, width, extender, self.adjustWindowSize_min)

        def ocultar_menues(self, event):
            if event.button() == QtCore.Qt.LeftButton:
                self.ocultar_frame()
                self.ocultar_frame2()
                self.ocultar_frame3()
                self.ocultar_menu()

        ## Redimensionar ventana
        def resizeEvent(self, event):
            rect = self.rect()
            self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        
        ## mover ventana
        def mousePressEvent(self, event):
            self.clickPosition = event.globalPos()
        def mover_ventana(self, event):
            if self.isMaximized() == False:			
                if event.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.clickPosition)
                    self.clickPosition = event.globalPos()
                    event.accept()

            if event.globalPos().y() <=20:
                self.showMaximized()
            else:
                self.showNormal()

                


if __name__ == "__main__":
     app = QtWidgets.QApplication(sys.argv)
     mi_app = App()
     mi_app.show()
     sys.exit(app.exec_())	
