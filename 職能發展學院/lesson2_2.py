#!usr/bin/python3.x

import tkinter as tk

def createInterface(w):
    label = tk.Label(w, text="Hello! tkinter")
    label.pack(padx=100,pady=50)

if __name__ == "__main__":
    print("這個是主執行檔")
    window = tk.Tk()
    window.title("這是我的第一個視窗")
    #window.geometry("300x300")
    createInterface(window)
    window.mainloop()