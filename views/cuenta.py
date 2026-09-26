from kivy.uix.screenmanager import Screen
from widgets.toast import Toast
from widgets import WARNING

class CuentaView(Screen):
    usuario = {
        "nombre": "Juan Pérez",
        "email": "juan@email.com",
        "telefono": "+54 9 11 1234-5678",
        "nivel": "Intermedio",
        "partidos_jugados": 23,
        "victorias": 11,
    }

    def guardar_cambios(self, nombre, email, telefono):
        if not all([nombre, email, telefono]):
            Toast.show(self, "Complete todos los campos", color=WARNING)
            return
        Toast.show(self, "Datos actualizados")

    def cerrar_sesion(self):
        self.manager.current = "login"
        Toast.show(self, "Sesion cerrada")
