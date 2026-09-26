import os
import glob

from kivy.config import Config
Config.set('kivy', 'clipboard', 'null')  # Evita errores de xclip/xsel en Linux

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

# Importar todas las vistas
from views.login import LoginView
from views.homebase import HomeBaseView
from views.navbase import NavBaseView
from views.home import HomeView
from views.contacto import ContactoView
from views.reservas import ReservasView
from views.cuenta import CuentaView
from views.mapas import MapasView
from views.kits import KitsView
from views.modos import ModosView
from views.publica import PublicaView
from views.privada import PrivadaView


def load_kv_files(directory="views"):
    """Carga automáticamente todos los archivos .kv del directorio especificado."""
    kv_files = glob.glob(os.path.join(directory, "*.kv"))
    for kv_file in sorted(kv_files):
        Builder.load_file(kv_file)
        print(f"Cargado: {kv_file}")


# Registro de vistas: (nombre_en_screenmanager, ClaseVista)
VIEWS = [
    ("login",     LoginView),
    ("navbase",   NavBaseView),
    ("homebase",  HomeBaseView),
    ("home",      HomeView),
    ("contacto",  ContactoView),
    ("reservas",  ReservasView),
    ("cuenta",    CuentaView),
    ("mapas",     MapasView),
    ("kits",      KitsView),
    ("modos",     ModosView),
    ("publica",   PublicaView),
    ("privada",   PrivadaView),
]


class MyApp(App):
    def build(self):
        self.title = "My Kivy App"
        self.icon = "assets/images/icon.png"

        # Cargar todos los archivos .kv automáticamente
        load_kv_files("views")

        sm = ScreenManager()
        for name, view_class in VIEWS:
            sm.add_widget(view_class(name=name))
        return sm


if __name__ == "__main__":
    MyApp().run()
