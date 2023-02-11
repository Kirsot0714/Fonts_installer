from tkinter import Tk, Label, Button, Entry, filedialog, Frame
from tkdnd import *
import shutil
import collections
import os
import tkinter.ttk as ttk


class MyFirstGUI:
    def __init__(self, master):  # Функция ИНИЦИАЛИЗАЦИИ
        self.master = master

        master.iconbitmap(r"picture_for_fi.ico")
        master.title("Установщик шрифтов")  # Указание текста в верхнем левом углу объекта "окно"
        frame = Frame(master)
        frame.grid(row=0, column=0, columnspan=2, padx=20, pady=30)

        self.dnd_lable = Label(frame, text='Перетащи сюда папку со шрифтами', bg='grey90', highlightbackground='black',
                               highlightthickness=1)
        self.dnd_lable.grid(row=0, column=0, columnspan=2, ipadx=20, ipady=40)
        Label(master, text='Откуда брать файлы').grid(row=1, column=0, columnspan=2)

        self.drop_and_damp_input = Entry(master, width=40)  # АТРЕБУТ
        self.drop_and_damp_input.grid(row=2, column=0, columnspan=2, ipadx=23, padx=5)

        self.master.drop_target_register(DND_FILES)
        self.master.dnd_bind('<<Drop>>', self.path_listbox)

        self.greet_button = Button(master, text="Выбрать папку", width=15,
                                   command=self.choose_the_folder)
        self.greet_button.grid(row=3, column=0, columnspan=1, ipadx=15, pady=5)
        self.button_ready = Button(master, text='Перенести', width=15, command=self.d_and_d_and_entry)
        self.master.bind('<Return>', self.d_and_d_and_entry)
        self.button_ready.grid(row=3, column=1, columnspan=1, ipadx=15, pady=5)

    def path_listbox(self, event):
        self.drop_and_damp_input.insert("end", event.data)

    def choose_the_folder(self):
        file_way = filedialog.askdirectory()  # Здесь я использую askdirectory чтобы выбрать папку в которой у меня хранятся шрифты.
        # print(file_way)
        self.start(file_way)

    def d_and_d_and_entry(self, event=None):
        # print(self.drop_and_damp_input.get())
        self.start(self.drop_and_damp_input.get())

    def start(self, file_way):
        progress_bar = ttk.Progressbar(self.master, orient="horizontal", mode="determinate", value=0)
        progress_bar.grid(row=4, column=0, columnspan=2)
        self.master.update()
        # print(f'Запустилась функция старт :{file_way}')
        os_wolk = os.walk
        dic = collections.defaultdict(dict)
        EXTENTION_PRIORITY = ('otf', 'ttf')
        extention_filtr = {'otf', 'ttf'}
        lable = Label(self.master, text='Собираю файлы...')
        lable.grid(row=5, column=0, columnspan=2)
        if os.path.isdir(str(file_way)):
            for way, namderectory, names in os_wolk(str(file_way)):
                for i in names:
                    split_i = i.split('.')
                    name = i[:-4:]
                    type = split_i[-1]
                    if split_i[-1] in extention_filtr:
                        dic[name][type] = rf"{way}\{i}"
        progress_bar['maximum'] = len(dic)
        self.master.update()
        for name_of_font, value in dic.items():
            for ext in EXTENTION_PRIORITY:
                path = value.get(ext)
                if path:
                    progress_bar['value'] += 1
                    self.master.update()
                    # shutil.copy(path, r'C:\Users\Кирилл\Desktop\шрифты_перенос')
                    shutil.copy(path, r'C:\Windows\Fonts')
                    print(name_of_font, path.replace('', ''))
                    break
        lable.config(text='Перенос завершён.')
        progress_bar.destroy()


root = Tk()  # Создаётся объект который связан с окном
my_gui = MyFirstGUI(root)  # Передача объекта root в функцию инициализации объекта MyFirstGUI
root.mainloop()  # Выводит объект root
