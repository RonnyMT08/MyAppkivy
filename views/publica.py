from kivy.uix.screenmanager import Screen
from widgets.toast import Toast

class PublicaView(Screen):
    juegos_publicos = [
        {
            "nombre": "Partido del Sábado",
            "fecha": "28 Sep 2026",
            "hora": "10:00",
            "cupo": "15/20",
            "modo": "Equipo vs Equipo",
        },
        {
            "nombre": "Batalla Nocturna",
            "fecha": "3 Oct 2026",
            "hora": "20:00",
            "cupo": "10/30",
            "modo": "Battle Royale",
        },
        {
            "nombre": "Torneo Relámpago",
            "fecha": "10 Oct 2026",
            "hora": "14:00",
            "cupo": "20/40",
            "modo": "Captura la Bandera",
        },
    ]

    def unirse_al_juego(self, juego):
        Toast.show(self, f"Te uniste a: {juego['nombre']}")
