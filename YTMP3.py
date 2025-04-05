from pytubefix import YouTube, exceptions
import datetime
from moviepy import AudioFileClip
import os
import tkinter as tk

def obtHFActual():
    return datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

def descargarAudio(urlVideo):
    try:
        labelEstado.config(text="Estado: Descargando...")
        if not os.path.exists("./Descargas"):
            os.mkdir("./Descargas")
        print(f'{obtHFActual()} INFO: Descargando y convirtiendo el vídeo a mp3.')
        video = YouTube(urlVideo)
        audio = video.streams.filter(only_audio=True).first().download()
        archivoAudio = AudioFileClip(audio)
        archivoAudio.write_audiofile(f'./Descargas/{video.title}.mp3', bitrate="192k")
        os.remove(f'./{video.title}.m4a')
        labelEstado.config(text="Estado: Audio descargado con éxito.")
        print(f'{obtHFActual()} INFO: Se ha descargado el audio correctamente.')
    except exceptions.RegexMatchError as e:
        labelEstado.config(text="Estado: La URL no es correcta.")
        print(f'{obtHFActual()} ERROR: La URL no es correcta: {e}')


ventana = tk.Tk()
ventana.title("YTMP3 by SalvaJS")
frame = tk.Frame(ventana, width=300, height=200)
frame.pack()
# Etiqueta
label = tk.Label(frame, text="Introduce el enlace del vídeo a descargar en mp3")
label.pack()
# Entry
cuadroTexto = tk.Entry(frame, width=60)
cuadroTexto.pack()
# Botón.
boton = tk.Button(frame, text="Descargar", command=lambda: descargarAudio(cuadroTexto.get()))
boton.pack()
# Etiqueta estado
labelEstado = tk.Label(frame, text="Estado:")
labelEstado.pack()
#Bucle.
ventana.mainloop()