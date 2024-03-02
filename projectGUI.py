import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('green')


class MyGUI:
    def __init__(self):

        self.root = ctk.CTk()

        self.label = ctk.CTkLabel(self.root, text='Your message', font=('aptos',18))
        self.label.pack(padx=10, pady=10)

        self.textbox = ctk.CTkTextbox(self.root, font=('aptos', 16))
        self.textbox.bind('<KeyPress>', self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = ctk.IntVar()

        self.check = ctk.CTkCheckBox(self.root, text='Show messagebox', font=('aptos', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = ctk.CTkButton(self.root, text='Show message', font=('aptos', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title='Message', message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        if event.state == 12 and event.keysym == 'Return':
            self.show_message()

    def on_closing(self):
        if messagebox.askyesno(title='QUIT?', message='En serio te vas puta?'):
            self.root.destroy()
MyGUI()





#
#
# def login():
#     print('test')
#
#
# frame = customtkinter.CTkFrame(master=root)
# frame.pack(pady=20, padx=60, fill='both', expand=True)
#
# label = customtkinter.CTkLabel(master=frame, text='Login system', font=('aptos', 20))
# label.pack(pady=12, padx=10)
#
# entry1 = customtkinter.CTkEntry(master=frame, placeholder_text='Username')
# entry1.pack(pady=12, padx=10)
#
# entry2 = customtkinter.CTkEntry(master=frame, placeholder_text='Password', show='*')
# entry2.pack(pady=12, padx=10)
#
# button = customtkinter.CTkButton(master=frame, text='Login', command=login)
# button.pack(pady=12, padx=10)
#
# checkbox = customtkinter.CTkCheckBox(master=frame, text='Remember me')
# checkbox.pack(pady=12, padx=10)
#
# root.mainloop()
#



# root = tk.Tk()
# root.geometry('800x500')
# root.title('Capture photos')
#
# label = tk.Label(root, text='HOLA PUTOS', font=('Aptos', 18))
# label.pack(padx=20, pady=20)
#
# textbox = tk.Text(root, height=3, font=('aptos', 16))
# textbox.pack(padx=20)
#
# # button = tk.Button(root, text='Click', font=('aptos', 18))
# # button.pack()
#
# buttonframe = tk.Frame(root)
# buttonframe.columnconfigure(0, weight=1)
# buttonframe.columnconfigure(1, weight=1)
# buttonframe.columnconfigure(2, weight=1)
#
# btn1 = tk.Button(buttonframe, text=1, font=('aptos', 18))
# btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
#
# btn2 = tk.Button(buttonframe, text=2, font=('aptos', 18))
# btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
#
# btn3 = tk.Button(buttonframe, text=3, font=('aptos', 18))
# btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
#
# btn4 = tk.Button(buttonframe, text=4, font=('aptos', 18))
# btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
#
# btn5 = tk.Button(buttonframe, text=5, font=('aptos', 18))
# btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
#
# btn6 = tk.Button(buttonframe, text=6, font=('aptos', 18))
# btn6.grid(row=1, column=2, sticky=tk.W+tk.E)
#
# buttonframe.pack(fill= 'x')
#
# anotherbutton = tk.Button(root, text='TEST')
# anotherbutton.place(x=200, y=200, height=200, width=200)
#
# root.mainloop()
