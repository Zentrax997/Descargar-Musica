import tkinter as tk
from PIL import Image, ImageTk
import urllib.request
import io
import youtube_dl

def descargar_mp3():
    url = entry.get()
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    estado_label.config(text="¡Descarga completada!")

# Cargar la imagen por url
def cargar_imagen_desde_url(url):
    try:
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
        return Image.open(io.BytesIO(raw_data))
    except Exception as e:
        print("Error al cargar la imagen:", e)
        return None

root = tk.Tk()
root.geometry("900x400")
root.title("Descargar Música de Youtube")
root.config(bg="#1f1f1f")

# No estirar la interfaz
root.resizable(False, False)

# URL fondo de la imagen
imagen_url = "https://s1.zerochan.net/Unidentified.600.208086.jpg"

imagen = cargar_imagen_desde_url(imagen_url)

if imagen:
    
    imagen = imagen.resize((900, 400), Image.LANCZOS)
    imagen_de_fondo = ImageTk.PhotoImage(imagen)
    
   
    fondo_label = tk.Label(root, image=imagen_de_fondo, bg=root["bg"])
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    
    fondo_label.image = imagen_de_fondo

# Estilos para el Entry
entry_style = {"bg": "white", "fg": "#000000", "width": 50, "font": ("Arial", 12), "highlightthickness": 0}

# Entry para ingresar el enlace
entry = tk.Entry(root, **entry_style)
entry.pack(pady=50, padx=20)

# Botón de descarga
boton_descargar = tk.Button(root, text="DESCARGAR", command=descargar_mp3, bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), highlightthickness=0)
boton_descargar.pack(pady=5)

# Label para mostrar el estado de la descarga
estado_label = tk.Label(root, text="", bg=root["bg"], fg="#ffffff", bd=0) 
estado_label.pack(pady=10)

root.mainloop()