"""
Interfaz tipo inventario usando CustomTkinter (CTk)
Archivo: interfaz_customtkinter.py

Requisitos:
    pip install customtkinter

Estructura:
- Pantalla principal: imagen del campeón + estadísticas + barra superior con oro
- Esquina inferior derecha: cofre (imagen) que lleva a otra pestaña
- Segunda pestaña: dos cofres, uno con título 'Campeón' y otro 'Ítem'

Imágenes requeridas:
    img/campeon.png
    img/cofre.png
"""

import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

# Configuración global de CTk
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class InventarioApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Inventario de Campeones")
        self.geometry("1000x600")
        self.minsize(900, 500)

        # Variables
        self.oro = tk.IntVar(value=10000)

        # Frames
        self.main_frame = None
        self.cofre_frame = None

        self.create_main_screen()

    # ---------------- Pantalla Principal ----------------
    def create_main_screen(self):
        if self.cofre_frame:
            self.cofre_frame.destroy()

        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.pack(fill="both", expand=True)

        # Barra superior
        topbar = ctk.CTkFrame(self.main_frame, height=50)
        topbar.pack(fill="x", side="top")

        titulo = ctk.CTkLabel(topbar, text="Inventario de Campeones", font=ctk.CTkFont(size=22, weight="bold"))
        titulo.pack(side="left", padx=20, pady=10)

        # Indicador de oro (derecha)
        oro_frame = ctk.CTkFrame(topbar, fg_color="transparent")
        oro_frame.pack(side="right", padx=20)
        ctk.CTkLabel(oro_frame, text="💰", font=ctk.CTkFont(size=20)).pack(side="left")
        ctk.CTkLabel(oro_frame, textvariable=self.oro, font=ctk.CTkFont(size=18, weight="bold"), text_color="#FFD700").pack(side="left", padx=5)

        # Imagen del campeón
        try:
            img_campeon = Image.open("img/campeon.png").resize((250, 250))
            self.campeon_img = ImageTk.PhotoImage(img_campeon)
        except Exception:
            self.campeon_img = None

        img_label = ctk.CTkLabel(self.main_frame, image=self.campeon_img, text="")
        img_label.pack(pady=(50, 10))

        # Estadísticas
        stats_frame = ctk.CTkFrame(self.main_frame)
        stats_frame.pack(pady=10)

        stats = {
            "Vida": "1500",
            "Daño": "230",
            "Defensa": "120",
            "Velocidad": "80",
        }

        for k, v in stats.items():
            fila = ctk.CTkFrame(stats_frame, fg_color="transparent")
            fila.pack(anchor="w", pady=3)
            ctk.CTkLabel(fila, text=f"{k}:", width=120, anchor="w").pack(side="left")
            ctk.CTkLabel(fila, text=v, anchor="w", text_color="#A0E6FF").pack(side="left")

        # Imagen del cofre (botón inferior derecho)
        bottom_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        bottom_frame.pack(side="bottom", anchor="se", fill="x", pady=20, padx=30)

        try:
            img_cofre = Image.open("img/cofre.png").resize((100, 100))
            self.cofre_img = ImageTk.PhotoImage(img_cofre)
        except Exception:
            self.cofre_img = None

        cofre_btn = ctk.CTkButton(bottom_frame, image=self.cofre_img, text="", fg_color="transparent", hover_color="#FFFFFF20", command=self.open_cofre_screen)
        cofre_btn.pack(side="right")

    # ---------------- Pantalla de Cofres ----------------
    def open_cofre_screen(self):
        if self.main_frame:
            self.main_frame.destroy()

        self.cofre_frame = ctk.CTkFrame(self, corner_radius=0)
        self.cofre_frame.pack(fill="both", expand=True)

        # Título superior
        header = ctk.CTkLabel(self.cofre_frame, text="Cofres", font=ctk.CTkFont(size=24, weight="bold"))
        header.pack(pady=20)

        # Contenedor horizontal
        content = ctk.CTkFrame(self.cofre_frame)
        content.pack(expand=True)

        try:
            img_cofre = Image.open("img/cofre.png").resize((180, 180))
            self.cofre_display = ImageTk.PhotoImage(img_cofre)
        except Exception:
            self.cofre_display = None

        # Cofre izquierdo - Campeón
        left_frame = ctk.CTkFrame(content, fg_color="transparent")
        left_frame.pack(side="left", expand=True, padx=40)
        ctk.CTkLabel(left_frame, text="Campeón", font=ctk.CTkFont(size=18, weight="bold"), text_color="#7FDBFF").pack(pady=10)
        ctk.CTkLabel(left_frame, image=self.cofre_display, text="").pack()

        # Cofre derecho - Ítem
        right_frame = ctk.CTkFrame(content, fg_color="transparent")
        right_frame.pack(side="right", expand=True, padx=40)
        ctk.CTkLabel(right_frame, text="Ítem", font=ctk.CTkFont(size=18, weight="bold"), text_color="#FFD166").pack(pady=10)
        ctk.CTkLabel(right_frame, image=self.cofre_display, text="").pack()

        # Botón volver
        back_btn = ctk.CTkButton(self.cofre_frame, text="← Volver al inventario", command=self.create_main_screen)
        back_btn.pack(pady=20)


if __name__ == "__main__":
    app = InventarioApp()
    app.mainloop()


'''
class Campeon:
    def __init__(self, nombre, mana, AP, AD, armadura, resMagica, ):
        self.nombre
'''