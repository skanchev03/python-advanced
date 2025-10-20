import tkinter as tk


def create_app():
    window = tk.Tk()
    window.geometry("700x600+50+50")
    window.title("GUI Product Shop")
    window.iconbitmap("database/images/computer.ico")
    return window

app = create_app()
