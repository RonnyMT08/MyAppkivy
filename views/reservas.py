from kivy.uix.screenmanager import Screen
from widgets.toast import Toast
from widgets import ERROR, WARNING

class ReservasView(Screen):
    def confirmar_reserva(self, nombre, apellido, telefono, fecha, hora, personas):
        if not all([nombre, apellido, telefono, fecha, hora, personas]):
            Toast.show(self, "Complete todos los campos", color=WARNING)
            return
        Toast.show(self, f"Reserva confirmada para {nombre} {apellido}")
        self.manager.current = "home"

    def cancelar_reserva(self, codigo):
        Toast.show(self, f"Reserva {codigo} cancelada", color=ERROR)
