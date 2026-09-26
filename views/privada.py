from kivy.uix.screenmanager import Screen
from widgets.toast import Toast
from widgets import WARNING

class PrivadaView(Screen):
    def crear_sala(self, codigo, nombre):
        if not nombre or not codigo:
            Toast.show(self, "Complete nombre y codigo", color=WARNING)
            return
        Toast.show(self, f"Sala '{nombre}' creada (codigo: {codigo})")

    def unirse_a_sala(self, codigo):
        if not codigo:
            Toast.show(self, "Ingrese un codigo", color=WARNING)
            return
        Toast.show(self, f"Uniendose a sala {codigo}")
