import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QMessageBox
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
import facturacion  # Importa el archivo facturacion.py que contiene la clase FacturacionApp

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("MenuPrincipal")
        self.resize(500, 600)
        self.setStyleSheet("background-color: rgb(173, 216, 230);")
        self.centralwidget = QWidget(self)
        
        # Título del menú principal
        self.lblTitulo = QLabel("Menú Principal", self.centralwidget)
        self.lblTitulo.setGeometry(QRect(0, 50, 500, 80))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setStyleSheet("color: rgb(12, 11, 13);")
        self.lblTitulo.setAlignment(Qt.AlignCenter)

        # Botón para ir a la ventana de facturación
        self.btnFacturacion = QPushButton("Ir a Facturación", self.centralwidget)
        self.btnFacturacion.setGeometry(QRect(150, 200, 200, 50))
        self.btnFacturacion.setStyleSheet("background-color: rgb(10, 10, 10); color: white; font-size: 16px;")
        self.btnFacturacion.clicked.connect(self.abrir_facturacion)

        # Botón para ir a la ventana de inventario
        self.btnInventario = QPushButton("Ir a Inventario", self.centralwidget)
        self.btnInventario.setGeometry(QRect(150, 280, 200, 50))
        self.btnInventario.setStyleSheet("background-color: rgb(10, 10, 10); color: white; font-size: 16px;")
        self.btnInventario.clicked.connect(self.abrir_inventario)

        # Botón para registro de clientes
        self.btnRegistroClientes = QPushButton("Registro de Clientes", self.centralwidget)
        self.btnRegistroClientes.setGeometry(QRect(150, 360, 200, 50))
        self.btnRegistroClientes.setStyleSheet("background-color: rgb(10, 10, 10); color: white; font-size: 16px;")
        self.btnRegistroClientes.clicked.connect(self.registro_clientes)

        # Botón para ventas
        self.btnVentas = QPushButton("Ventas", self.centralwidget)
        self.btnVentas.setGeometry(QRect(150, 440, 200, 50))
        self.btnVentas.setStyleSheet("background-color: rgb(10, 10, 10); color: white; font-size: 16px;")
        self.btnVentas.clicked.connect(self.ventas)

        # Configurar el widget central
        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("Menú Principal - CandyVoyage")

    def abrir_facturacion(self):
        """Abre la ventana de facturación y oculta el menú principal."""
        self.facturacion_window = facturacion.FacturacionApp()  # Crear instancia de FacturacionApp
        self.facturacion_window.show()
        self.hide()  # Ocultar el menú principal mientras se muestra la ventana de facturación

    def abrir_inventario(self):
        """Muestra un mensaje para indicar que el inventario fue seleccionado (o abre la ventana de inventario)."""
        QMessageBox.information(self, "Inventario", "Se ha seleccionado la opción de Inventario.")
        # Aquí podrías abrir una ventana de inventario en lugar de mostrar un mensaje.

    def registro_clientes(self):
        """Muestra un mensaje para indicar que el registro de clientes fue seleccionado (o abre la ventana de registro)."""
        QMessageBox.information(self, "Registro de Clientes", "Se ha seleccionado la opción de Registro de Clientes.")
        # Aquí podrías abrir una ventana de registro de clientes en lugar de mostrar un mensaje.

    def ventas(self):
        """Muestra un mensaje para indicar que la opción de ventas fue seleccionada (o abre la ventana de ventas)."""
        QMessageBox.information(self, "Ventas", "Se ha seleccionado la opción de Ventas.")
        # Aquí podrías abrir una ventana de ventas en lugar de mostrar un mensaje.

    def closeEvent(self, event):
        """Cierra la aplicación cuando se cierra el menú principal."""
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_principal = MainWindow()
    ventana_principal.show()
    sys.exit(app.exec_())
