from tkinter import *
import pygame
import webbrowser, pyautogui
from tkinter import messagebox #XD
from tkinter import font #XD
import os

pygame.init()

def btn_clicked():
    webbrowser.open(f"https://web.whatsapp.com")

def reproducir_sonido():
    pygame.mixer.music.load("files/ATERNOS.mp3")
    pygame.mixer.music.play()

def BUM():
    try:
        UNO = str(entry0.get())
        DOS = int(entry1.get())
        TRES = str(entry2.get())
        print(UNO)
        print(DOS)
        print(TRES)

        global Fuente, Icon, Fondo, BTN

        def CERRAR():
            Segunda_ventana.destroy()

        def Sound():
            pygame.mixer.music.load("files2/inicio.mp3")
            pygame.mixer.music.play()

        def actualizar_tiempo():
            nonlocal tiempo_restante
            tiempo_restante -= 1
            canvas.itemconfig(tiempo_text, text=str(tiempo_restante))
            if tiempo_restante <= 0:
                for i in range(DOS):
                    pyautogui.typewrite(TRES)
                    pyautogui.press("enter")
                messagebox.showinfo(message=f"Se ha enviado a: {UNO} \n{DOS} mensajes\n de contenido: {TRES}", title="¡Resultado exitoso!")
                Segunda_ventana.destroy()
            else:
                Segunda_ventana.after(1000, actualizar_tiempo)

        tiempo_restante = 60

        Segunda_ventana = Toplevel()
        webbrowser.open(f"https://web.whatsapp.com/send?phone={UNO}")
        Sound()

        Segunda_ventana.geometry("352x224")
        Segunda_ventana.configure(bg="#ffffff")
        Segunda_ventana.iconbitmap(Icon)
        Segunda_ventana.title("Ejecución")

        canvas = Canvas(
            Segunda_ventana,
            bg="#ffffff",
            height=224,
            width=353,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=-1, y=0)

        background = canvas.create_image(
            176.5, 112.0,
            image=Fondo)

        tiempo_text = canvas.create_text(
            177.0, 123.5,
            text=str(tiempo_restante),
            fill="#000000",
            font=Fuente)

        b0 = Button(
            Segunda_ventana,
            image=BTN,
            borderwidth=0,
            highlightthickness=0,
            command=CERRAR,
            relief="flat")

        b0.place(
            x=100, y=165,
            width=160,
            height=35)

        Segunda_ventana.resizable(False, False)

        # Llama a la función actualizar_tiempo después de 1000 milisegundos (1 segundo)
        Segunda_ventana.after(1000, actualizar_tiempo)

    except:
        messagebox.showerror("Error", "Ops, ha ocurrido un error.")

window = Tk()

window.geometry("986x606")
window.configure(bg = "#ffffff")
window.title("PWB")
window.iconbitmap("files/XD.ico")

reproducir_sonido()

#IMPORTES
Fuente = font.Font(family = "files2/LilitaOne", size = 24, weight = "bold")
Icon = "files2/icon.ico"
Fondo = PhotoImage(file = f"files2/background.png")
BTN = PhotoImage(file = f"files2/B.png")

canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 606,
    width = 987,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = -1, y = 0)

background_img = PhotoImage(file = f"files/background.png")
background = canvas.create_image(
    493.5, 303.0,
    image=background_img)

entry0_img = PhotoImage(file = f"files/img_textBox0.png")
entry0_bg = canvas.create_image(
    287.0, 216.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#cc2b2b",
    font = ("Helvita", 20, "bold"),
    highlightthickness = 0)

entry0.place(
    x = 64.5, y = 198,
    width = 445.0,
    height = 45)

entry1_img = PhotoImage(file = f"files/img_textBox1.png")
entry1_bg = canvas.create_image(
    292.0, 318.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#cc2b2b",
    font = ("Helvita", 20, "bold"),
    highlightthickness = 0)

entry1.place(
    x = 69.5, y = 300,
    width = 445.0,
    height = 45)

entry2_img = PhotoImage(file = f"files/img_textBox2.png")
entry2_bg = canvas.create_image(
    292.0, 420.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#2b7ecc",
    font = ("Helvita", 20, "bold"),
    highlightthickness = 0)

entry2.place(
    x = 69.5, y = 401,
    width = 445.0,
    height = 45)

img0 = PhotoImage(file = f"files/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = BUM,
    relief = "flat")

b0.place(
    x = 182, y = 467,
    width = 210,
    height = 63)

img1 = PhotoImage(file = f"files/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 15, y = 6,
    width = 71,
    height = 71)

window.resizable(False, False)
window.mainloop()
