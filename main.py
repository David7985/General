import customtkinter as ctk

# Configuración global de CTk
ctk.set_appearance_mode("Dark")  # "Light", "Dark" o "System"
ctk.set_default_color_theme("blue")  # temas: "blue", "green", "dark-blue" o uno custom

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Proyecto")
        self.geometry("900x600")

if __name__ == "__main__":
    app = App()
    app.mainloop()


'''
class Campeon:
    def __init__(self, nombre, mana, AP, AD, armadura, resMagica, ):
        self.nombre
'''