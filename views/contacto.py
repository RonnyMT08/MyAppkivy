from kivy.uix.screenmanager import Screen

class ContactoView(Screen):
    def open_instagram(self):
        import webbrowser
        webbrowser.open("https://www.instagram.com/tu_usuario/")
    def open_facebook(self):
        import webbrowser
        webbrowser.open("https://www.facebook.com/tu_usuario/")
    def open_whatsapp(self):
        import webbrowser
        webbrowser.open("https://wa.me/1234567890")
    def open_email(self):
        import webbrowser
        webbrowser.open("mailto:tu_email@ejemplo.com")
