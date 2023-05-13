import customtkinter as ctk
import tkinter.messagebox as mb
from tkinter import *
import os
import re

ctk.set_appearance_mode("System")

class SampleApp(ctk.CTk):

    def loading_schedule(self):
        schedule_list = []
        file_schedule = open("Schedule.txt", 'r', encoding='utf-8')
        for line in file_schedule:
            line = line.split(",")
            schedule_list.append(line[0] + "," + line[1] + "," + line[2])
        file_schedule.close()
        return schedule_list

    schedule_list = []

    def __init__(self):
        ctk.CTk.__init__(self)

        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        SampleApp.schedule_list = SampleApp.loading_schedule(self)

        self.frames = {}
        for F in (Registration, Sign_in,
                  Client_Profile, Make_reg, Delete_reg,
                  Master_Profile, Check_appointment,
                  Manager_Profile, Add_master, Make_schedule, Delete_schedule):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Sign_in")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class Registration(ctk.CTkFrame):
    def __init__(self, parent, controller):

        def click_reg():
            if entry_login.get().replace(" ", "") == "" or entry_passwrod.get().replace(" ","") == "":
                return

            file_clients = open("Clients.txt", "r+", encoding = 'utf-8')
            for line in file_clients:
                line = line.split(",")
                if entry_login.get() == line[0]:
                    mb.showwarning("Предупреждение", "Логин уже существует")
                    file_clients.close()
                    return
            file_masters = open("Masters.txt", "r", encoding='utf-8')
            for line in file_masters:
                line = line.split(",")
                if entry_login.get() == line[0]:
                    mb.showwarning("Предупреждение", "Логин уже существует")
                    file_masters.close()
                    return
            file_masters.close()
            file_managers = open("Managers.txt", "r", encoding='utf-8')
            for line in file_managers:
                line = line.split(",")
                if entry_login.get() == line[0]:
                    mb.showwarning("Предупреждение", "Логин уже существует")
                    file_managers.close()
                    return
            file_managers.close()
            if len(entry_FIO.get().split()) != 3 or entry_FIO.get().replace(" ","").isalpha() == False:
                mb.showwarning("Предупреждение", "Неверно введено ФИО")
                return
            file_clients.write(entry_login.get() + "," + entry_passwrod.get() + "," + entry_FIO.get() + "\n")
            file_clients.close()
            mb.showinfo("Уведомление", "Вы успешно зарегистрировались!")
            controller.show_frame("Client_Profile")
            Sign_in.login = entry_login.get()
            return

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        btn_entry = ctk.CTkButton(self, text="Вход", command=lambda: controller.show_frame("Sign_in"))
        btn_quit = ctk.CTkButton(self, text="Выйти", command=lambda: app.destroy())
        btn_entry.place(rely = 0, relx = 0.05)
        btn_quit.place(rely = 0, relx = 0.6)

        label_FIO = ctk.CTkLabel(self, text = "ФИО")
        label_FIO.place(rely = 0.1, relx = 0.465)

        entry_FIO = ctk.CTkEntry(self)
        entry_FIO.place(rely = 0.18, relx = 0.33)

        label_login = ctk.CTkLabel(self, text="Логин")
        label_login.place(rely=0.28, relx=0.455)

        entry_login = ctk.CTkEntry(self)
        entry_login.place(rely=0.36, relx=0.33)

        label_password = ctk.CTkLabel(self, text="Пароль")
        label_password.place(rely=0.46, relx=0.445)

        entry_passwrod = ctk.CTkEntry(self, show = "*")
        entry_passwrod.place(rely=0.54, relx=0.33)

        btn_reg = ctk.CTkButton(self, text = "Зарегистрироваться", command = click_reg)
        btn_reg.place(rely = 0.70, relx = 0.33)

class Sign_in(ctk.CTkFrame):

    login = ""

    def __init__(self, parent, controller):

        def click_sign_in():

            file_clients = open("Clients.txt", "r", encoding = 'utf-8')
            for line in file_clients:
                line = line.split(",")
                if line[0] == entry_login.get() and line[1] == entry_password.get():
                    Sign_in.login = line[0]
                    mb.showinfo("Уведомление", "Успешно!")
                    file_clients.close()
                    controller.show_frame("Client_Profile")
                    return
            file_clients.close()

            file_masters = open("Masters.txt", "r", encoding='utf-8')
            for line in file_masters:
                line = line.split(",")
                if line[0] == entry_login.get() and line[1] == entry_password.get():
                    Sign_in.login = line[0]
                    mb.showinfo("Уведомление", "Успешно!")
                    file_masters.close()
                    controller.show_frame("Master_Profile")
                    return
            file_masters.close()

            file_managers = open("Managers.txt", "r", encoding='utf-8')
            for line in file_managers:
                line = line.split(",")
                if line[0] == entry_login.get() and line[1] == entry_password.get():
                    Sign_in.login = line[0]
                    mb.showinfo("Уведомление", "Успешно!")
                    file_managers.close()
                    controller.show_frame("Manager_Profile")
                    return
            file_managers.close()

            mb.showwarning("Предупреждение", "Неверный логин или пароль")
            return

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        button1 = ctk.CTkButton(self, text="Регистрация",
                                command=lambda: controller.show_frame("Registration"))
        button2 = ctk.CTkButton(self, text="Выйти",
                                command=lambda: app.destroy())
        button1.place(rely=0, relx=0.05)
        button2.place(rely=0, relx=0.6)

        label_login = ctk.CTkLabel(self, text="Логин")
        label_login.place(rely=0.1, relx=0.455)

        entry_login = ctk.CTkEntry(self)
        entry_login.place(rely=0.18, relx=0.33)

        label_password = ctk.CTkLabel(self, text="Пароль")
        label_password.place(rely=0.28, relx=0.445)

        entry_password = ctk.CTkEntry(self, show = "*")
        entry_password.place(rely=0.36, relx=0.33)

        btn_reg = ctk.CTkButton(self, text="Войти", command = click_sign_in)
        btn_reg.place(rely=0.52, relx=0.33)

class Client_Profile(ctk.CTkFrame):

    def __init__(self, parent, controller):
        def click_delete():
            controller.show_frame("Delete_reg")
            return

        def click_make():
            controller.show_frame("Make_reg")
            return

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        btn_make_reg = ctk.CTkButton(self, text="Запись на прием", command=click_make)
        btn_make_reg.pack(pady = 100)

        btn_delete_reg = ctk.CTkButton(self, text="Отменить прием", command=click_delete)
        btn_delete_reg.pack()

        btn_quit = ctk.CTkButton(self, text="Выйти", command=lambda: app.destroy())
        btn_quit.pack(side="bottom")

class Make_reg(ctk.CTkFrame):
    def __init__(self, parent, controller):

        def update_masters(event):
            Manager_Profile.master_list = Manager_Profile.create_list_master(self)
            Manager_Profile.master_file = Manager_Profile.create_file_master(self)
            menu_masters.configure(values=Manager_Profile.master_list)

        def set_master_time(menu_masters: str):
            menu_time.set("Выберите время")
            arr_work_time = []
            arr_busy_time = []
            for line in SampleApp.schedule_list:
                line = line.split(",")
                if line[0] == menu_masters:
                    arr_busy_time.append(line[1])
            file_master = open("Masters.txt", "r", encoding="utf-8")
            for line in file_master:
                line = line.split(",")
                if line[2] == menu_masters:
                    line[3] = line[3].split()
                    if len(line) == 4:
                        for work_time in line[3]:
                            if len(work_time) == 4:
                                work_time = work_time[:2] + ':' + work_time[2:]
                                if work_time not in arr_busy_time:
                                    arr_work_time.append(work_time)
                            else:
                                work_time = work_time[:1] + ':' + work_time[1:]
                                if work_time not in arr_busy_time:
                                    arr_work_time.append(work_time)
                    else:
                        menu_time.set("У данного массажиста нет рабочего времени")
            file_master.close()
            menu_time.configure(values= arr_work_time)
            return

        def click_make_reg():
            file = open("Schedule.txt", "r+", encoding="utf-8")
            str_master = menu_masters.get()
            str_time = menu_time.get()
            if str_master == "Выберите массажиста" or str_time == "Выберите время":
                mb.showwarning("Предупреждение", "Вы не выбрали мастера или время!")
                file.close()
                return
            if os.stat("Schedule.txt").st_size != 0:
                for line in file:
                    line = line.split(",")
                    if line[0] == str_master and line[1] == str_time:
                        mb.showwarning("Предупреждение", "Данное время уже занято")
                        file.close()
                        return
            answer = mb.askyesno("Внимание", "Вы уверены, что хотите сделать запись?")
            if answer:
                file.write(str_master + "," + str_time + "," + Sign_in.login + "\n")
                file.close()
                SampleApp.schedule_list = SampleApp.loading_schedule(self)
                mb.showinfo("Уведомление", "Запись сделана!")
            return

        def click_to_back():
            menu_time.set("Выберите время")
            menu_masters.set("Выберите массажиста")
            controller.show_frame("Client_Profile")

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        Manager_Profile.master_list = Manager_Profile.create_list_master(self)
        Manager_Profile.master_file = Manager_Profile.create_file_master(self)

        label_title = ctk.CTkLabel(self, text = "Запись на прием", font=ctk.CTkFont(size=20))
        label_title.pack(anchor = "nw", padx = 20)

        menu_masters = ctk.CTkOptionMenu(self, values = Manager_Profile.master_list, width= 300, command=set_master_time)
        menu_masters.pack(anchor = "center", pady = 50)
        menu_masters.set("Выберите массажиста")
        menu_masters.bind("<Enter>", update_masters)

        menu_time = ctk.CTkOptionMenu(self, values = "", width= 300)
        menu_time.pack(anchor = "center")
        menu_time.set("Выберите время")

        btn_make_reg = ctk.CTkButton(self, text = "Записаться", command = click_make_reg)
        btn_make_reg.pack(side = "left",padx = 40, pady = 90)

        btn_to_back = ctk.CTkButton(self, text = "Назад", command = click_to_back)
        btn_to_back.pack(side = "left")

class Delete_reg(ctk.CTkFrame):
    def __init__(self, parent, controller):

        def click_delete_reg():
            file_schedule = open("Schedule.txt", "w", encoding = "utf-8")
            if menu_reg.get() == "Выберите запись":
                mb.showwarning("Предупреждение", "Вы не выбрали запись!")
                file_schedule.close()
                return
            answer = mb.askyesno("Внимание", "Вы уверены, что хотите удалить запись?")
            if answer:
                for i in range(len(SampleApp.schedule_list)):
                    temp_str = SampleApp.schedule_list[i].split(",")
                    if temp_str[0] + " " + temp_str[1] == menu_reg.get():
                        SampleApp.schedule_list.pop(i)
                        break
            for line in SampleApp.schedule_list:
                file_schedule.write(line)
            menu_reg.set("Выберите запись")
            file_schedule.close()
            return

        def loading_user_schedule(event):
            user_schedule = []
            for list in SampleApp.schedule_list:
                list = list.split(",")
                list[2] = list[2].replace("\n", "")
                if list[2] == Sign_in.login:
                    user_schedule.append(list[0] + " " + list[1])
            menu_reg.configure(values=user_schedule)
            return

        def click_back():
            controller.show_frame("Client_Profile")
            return

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        btn_back = ctk.CTkButton(self, text="Назад", command=click_back)
        btn_back.pack(side = "top")

        label_del_reg = ctk.CTkLabel(self, text = "Отмена записи", font=ctk.CTkFont(size=20))
        label_del_reg.pack(side = "top", pady = 10)

        label_time = ctk.CTkLabel(self, text = "Время приема:", font=ctk.CTkFont(size=14))
        label_time.pack (side = "top" , anchor = "nw")

        menu_reg = ctk.CTkOptionMenu(self, values="", width=300)
        menu_reg.pack(side="top", pady=10)
        menu_reg.set("Выберите запись")
        menu_reg.bind("<Enter>", loading_user_schedule)

        btn_delete_reg = ctk.CTkButton(self, text="Отменить запись", command = click_delete_reg)
        btn_delete_reg.pack(side="top", pady=10)

class Master_Profile(ctk.CTkFrame):

    master_schedule = []

    def __init__(self, parent, controller):

        def click_check_reg():
            masters_fio = ""
            Master_Profile.master_schedule = []
            file_masters = open("Masters.txt", "r", encoding="utf-8")
            for line in file_masters:
                line = line.split(",")
                if Sign_in.login == line[0]:
                    line[2] = line[2].replace("\n","")
                    masters_fio = line[2]
                    break
            file_masters.close()

            SampleApp.schedule_list = SampleApp.loading_schedule(SampleApp)

            for list in SampleApp.schedule_list:
                temp_list = list.split(",")
                if temp_list[0] == masters_fio:
                    Master_Profile.master_schedule.append(list)

            controller.show_frame("Check_appointment")
            return

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        btn_check_reg = ctk.CTkButton(self, text="Просмотр записи", command=click_check_reg)
        btn_check_reg.pack(pady = 150, anchor = "center")

        btn_quit = ctk.CTkButton(self, text="Выйти", command=lambda: app.destroy())
        btn_quit.pack(side="bottom")

class Check_appointment(ctk.CTkFrame):
    def __init__(self, parent, controller):

        def click_mark():
            selection = listbox_schedule.curselection()
            text_select = []
            for i in selection:
                text_select.append(listbox_schedule.get(i))
            for list in Master_Profile.master_schedule:
                temp_list = list.split(",")
                for line in text_select:
                    time = "".join(line)
                    time = re.sub("\D", "", time)
                    temp_list[1] = re.sub("\D", "", temp_list[1])
                    if time == temp_list[1] :
                        Master_Profile.master_schedule.remove(list)
                        SampleApp.schedule_list.remove(list)
            file_schedule = open("Schedule.txt", "w", encoding="utf-8")
            for line in SampleApp.schedule_list:
                file_schedule.write(line)
            file_schedule.close()
            listbox_schedule.delete(selection)
            return

        def click_back():
            empty = Variable(value="")
            listbox_schedule.configure(listvariable=empty)
            controller.show_frame("Master_Profile")
            return

        def loading_master_schedule(event):
            update_master_schedule = []
            file_clients = open("Clients.txt", "r", encoding="utf-8")
            for line in file_clients:
                line = line.split(",")
                line[2] = line[2].replace("\n", "")
                for list in Master_Profile.master_schedule:
                    list = list.split(",")
                    list[2] = list[2].replace("\n", "")
                    if line[0] == list[2]:
                        update_master_schedule.append(line[2] + ", " + list[1])
            file_clients.close()
            schedule = Variable(value=update_master_schedule)
            listbox_schedule.configure(listvariable=schedule)
            return

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        btn_back = ctk.CTkButton(self, text="Назад", command=click_back)
        btn_back.pack(side="top")

        label_del_reg = ctk.CTkLabel(self, text="Записи", font=ctk.CTkFont(size=20))
        label_del_reg.pack(side="top", pady=10)

        listbox_schedule = Listbox(self, listvariable="", selectmode=EXTENDED, selectbackground="green", width=50)
        listbox_schedule.pack(side="top", anchor="center")
        listbox_schedule.bind("<Enter>", loading_master_schedule)

        btn_mark = ctk.CTkButton(self, text="Отметить выполнеными", command=click_mark)
        btn_mark.pack(side="top", pady=10)

class Manager_Profile(ctk.CTkFrame):

    master_list = []
    master_file = []

    def create_list_master(self):
        master_list = []
        file_master = open("Masters.txt", 'r', encoding='utf-8')
        for line in file_master:
            line = line.split(",")
            line[2] = line[2].replace("\n", "")
            master_list.append(line[2])
        file_master.close()
        return master_list

    def create_file_master(self):
        master_file = []
        file_master = open("Masters.txt", 'r', encoding='utf-8')
        for line in file_master:
            master_file.append(line)
        file_master.close()
        return master_file

    def __init__(self, parent, controller):

        def click_add_master():
            controller.show_frame("Add_master")
            return

        def click_make_schedule():
            controller.show_frame("Make_schedule")
            return

        def click_delete_schedule():
            controller.show_frame("Delete_schedule")
            return

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        btn_add_master = ctk.CTkButton(self, text="Добавить массажиста", command=click_add_master)
        btn_add_master.pack(pady = 50)

        btn_make_schedule = ctk.CTkButton(self, text="Создать расписание массажистов", command=click_make_schedule)
        btn_make_schedule.pack()

        btn_delete_schedule = ctk.CTkButton(self, text="Удалить расписание массажистов", command=click_delete_schedule)
        btn_delete_schedule.pack(pady = 50)

        btn_quit = ctk.CTkButton(self, text="Выйти", command=lambda: app.destroy())
        btn_quit.pack(side="bottom")

class Add_master(ctk.CTkFrame):
    def __init__(self, parent, controller):

        def click_reg():
            file_clients = open("Clients.txt", "r", encoding='utf-8')
            for line in file_clients:
                line = line.split(",")
                if entry_login.get() == line[0]:
                    mb.showwarning("Предупреждение", "Логин уже существует")
                    file_clients.close()
                    return
            file_clients.close()

            file_managers = open("Managers.txt", "r", encoding='utf-8')
            for line in file_managers:
                line = line.split(",")
                if entry_login.get() == line[0]:
                    mb.showwarning("Предупреждение", "Логин уже существует")
                    file_managers.close()
                    return
            file_managers.close()

            file_masters = open("Masters.txt", "r+", encoding='utf-8')
            for line in file_masters:
                line = line.split(",")
                if entry_login.get() == line[0]:
                    mb.showwarning("Предупреждение", "Логин уже существует")
                    file_masters.close()
                    return

            if len(entry_FIO.get().split()) != 3:
                mb.showwarning("Предупреждение", "Неверно введено ФИО")
                return
            answer = mb.askyesno("Внимание", "Вы уверены, что хотите зарегистрировать массажиста?")
            if answer:
                file_masters.write(entry_login.get() + "," + entry_passwrod.get() + "," + entry_FIO.get() + "\n")
            else:
                file_masters.close()
                return
            file_masters.close()
            mb.showinfo("Уведомление", "Вы успешно зарегистрировали массажиста!")
            Manager_Profile.master_list = Manager_Profile.create_list_master(self)
            Manager_Profile.master_file = Manager_Profile.create_file_master(self)
            return

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        btn_entry = ctk.CTkButton(self, text="Назад", command=lambda: controller.show_frame("Manager_Profile"))
        btn_entry.place(rely=0, relx=0.33)

        label_FIO = ctk.CTkLabel(self, text="ФИО массажиста")
        label_FIO.place(rely=0.1, relx=0.375)

        entry_FIO = ctk.CTkEntry(self)
        entry_FIO.place(rely=0.18, relx=0.33)

        label_login = ctk.CTkLabel(self, text="Логин")
        label_login.place(rely=0.28, relx=0.455)

        entry_login = ctk.CTkEntry(self)
        entry_login.place(rely=0.36, relx=0.33)

        label_password = ctk.CTkLabel(self, text="Пароль")
        label_password.place(rely=0.46, relx=0.445)

        entry_passwrod = ctk.CTkEntry(self, show="*")
        entry_passwrod.place(rely=0.54, relx=0.33)

        btn_reg = ctk.CTkButton(self, text="Зарегистрировать", command=click_reg)
        btn_reg.place(rely=0.70, relx=0.33)

class Make_schedule(ctk.CTkFrame):

    def __init__(self, parent, controller):

        def update_masters(event):
            menu_masters.configure(values=Manager_Profile.master_list)

        def click_make_reg():
            Manager_Profile.master_list = Manager_Profile.create_list_master(self)
            Manager_Profile.master_file = Manager_Profile.create_file_master(self)
            if menu_masters.get() == "Выберите массажиста":
                mb.showwarning("Предупреждение", "Вы не выбрали массажиста")
                return
            check_time = menu_time.get()
            if len(check_time) != 3 or len(check_time) != 4:
                if not re.fullmatch(r'\d{1,2}\:\d{2}',check_time ):
                    mb.showwarning("Предупреждение", "Неверно задано рабочее время")
                    return
            check_time = check_time.replace(":", "")
            file_masters = open("Masters.txt", "r", encoding="utf-8")
            for line in file_masters:
                line = line.split(",")
                if menu_masters.get() == line[2]:
                    line[3] = line[3].split()
                    for time in line[3]:
                        if time == check_time:
                            mb.showwarning("Предупреждение", "Данное рабочее время уже существует")
                            return
            answer = mb.askyesno("Внимание", "Вы уверены, что хотите добавить рабочее время?")
            if answer:
                temp_time = menu_time.get()
                temp_time = temp_time.replace(":", "")
                for i in range(len(Manager_Profile.master_file)):
                    line = Manager_Profile.master_file[i]
                    line = line.split(",")
                    line[2] = line[2].replace("\n", "")
                    if line[2] == menu_masters.get():
                        if len(line) == 3:
                            line.append(temp_time)
                            master_str = line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "\n"
                            Manager_Profile.master_file[i] = master_str
                        else:
                            line[3] = line[3].replace("\n", "")
                            line[3] = line[3] + " " + temp_time + "\n"
                            master_str = line[0] + "," + line[1] + "," + line[2] + "," + line[3]
                            Manager_Profile.master_file[i] = master_str

                file_masters = open("Masters.txt", 'w', encoding="utf-8")
                for line in Manager_Profile.master_file:
                    file_masters.write(line)
                file_masters.close()
                mb.showinfo("Уведомление", "Вы успешно добавили рабочее время!")
                return
            else:
                return

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        Manager_Profile.master_list = Manager_Profile.create_list_master(self)
        Manager_Profile.master_file = Manager_Profile.create_file_master(self)

        menu_masters = ctk.CTkOptionMenu(self, values=Manager_Profile.master_list, width=300)
        menu_masters.pack(anchor="center", pady=50)
        menu_masters.set("Выберите массажиста")
        menu_masters.bind("<Enter>", update_masters)

        label_time = ctk.CTkLabel(self, text="Добавить рабочие часы (в формате xx:xx)")
        label_time.pack(anchor = "w", padx = 55)

        menu_time = ctk.CTkEntry(self, width=300)
        menu_time.pack(anchor="center", pady = 1)

        btn_to_back = ctk.CTkButton(self, text="Назад", command=lambda: controller.show_frame("Manager_Profile"))
        btn_to_back.pack(side="left", padx = 40, pady=90)

        btn_make_reg = ctk.CTkButton(self, text="Сохранить", command=click_make_reg)
        btn_make_reg.pack(side="left")

class Delete_schedule(ctk.CTkFrame):
    def __init__(self, parent, controller):

        def update_masters(event):
            menu_masters.configure(values=Manager_Profile.master_list)

        def update_time(menu_masters: str):
            menu_time.set("Выберите время")
            arr_work_time = []
            file_master = open("Masters.txt", "r", encoding="utf-8")
            for line in file_master:
                line = line.split(",")
                if line[2] == menu_masters:
                    if len(line) == 4:
                        line[3] = line[3].split()
                        for work_time in line[3]:
                            if len(work_time) == 4:
                                work_time = work_time[:2] + ':' + work_time[2:]
                                arr_work_time.append(work_time)
                            else:
                                work_time = work_time[:1] + ':' + work_time[1:]
                                arr_work_time.append(work_time)
                    else:
                        menu_time.set("У данного массажиста нет рабочего времени")
            file_master.close()
            menu_time.configure(values=arr_work_time)
            return


        def click_make_reg():
            Manager_Profile.master_list = Manager_Profile.create_list_master(self)
            Manager_Profile.master_file = Manager_Profile.create_file_master(self)
            if menu_masters.get() == "Выберите массажиста":
                mb.showwarning("Предупреждение", "Вы не выбрали массажиста")
                return
            check_time = menu_time.get()
            if len(check_time) != 3 or len(check_time) != 4:
                if not re.fullmatch(r'\d{1,2}\:\d{2}',check_time ):
                    mb.showwarning("Предупреждение", "Неверно задано рабочее время")
                    return
            check_time = check_time.replace(":", "")
            file_masters = open("Masters.txt", "r", encoding="utf-8")
            for line in file_masters:
                line = line.split(",")
                if menu_masters.get() == line[2]:
                    line[3] = line[3].split()
                    check = False
                    for time in line[3]:
                        if time == check_time:
                            check = True
                            break
            if check == False:
                mb.showwarning("Предупреждение", "Данного времени нет у массажиста")
                return
            answer = mb.askyesno("Внимание", "Вы уверены, что хотите удалить рабочее время?")
            if answer:
                temp_time = menu_time.get()
                temp_time = temp_time.replace(":", "")
                for i in range(len(Manager_Profile.master_file)):
                    line = Manager_Profile.master_file[i]
                    line = line.split(",")
                    if line[2] == menu_masters.get():
                        line[3] = line[3].split()
                        for j in range(len(line[3])):
                            if line[3][j] == temp_time:
                                line[3].pop(j)
                                if not line[3]:
                                    Manager_Profile.master_file[i] = line[0] + "," + line[1] + "," + line[2] + "\n"
                                    break
                                else:
                                    time_str = ""
                                    for string in line[3]:
                                        time_str = time_str + string + " "
                                    time_str = time_str[:-1]
                                    Manager_Profile.master_file[i] = line[0] + "," + line[1] + "," + line[2] + "," + time_str + "\n"
                                    break

                file_masters = open("Masters.txt", 'w', encoding="utf-8")
                for line in Manager_Profile.master_file:
                    file_masters.write(line)
                file_masters.close()
                mb.showinfo("Уведомление", "Вы успешно удалили рабочее время")
                update_time(menu_masters.get())
                menu_masters.set("Выберите массажиста")
                return
            else:
                return

        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        Manager_Profile.master_list = Manager_Profile.create_list_master(self)
        Manager_Profile.master_file = Manager_Profile.create_file_master(self)

        menu_masters = ctk.CTkOptionMenu(self, values=Manager_Profile.master_list, width=300, command=update_time)
        menu_masters.pack(anchor="center", pady=50)
        menu_masters.set("Выберите массажиста")
        menu_masters.bind("<Enter>", update_masters)

        menu_time = ctk.CTkOptionMenu(self, values="", width=300)
        menu_time.pack(anchor="center")
        menu_time.set("Выберите время")

        btn_to_back = ctk.CTkButton(self, text="Назад", command=lambda: controller.show_frame("Manager_Profile"))
        btn_to_back.pack(side="left", padx=40, pady=90)

        btn_make_reg = ctk.CTkButton(self, text="Удалить", command=click_make_reg)
        btn_make_reg.pack(side="left")

app = SampleApp()
app.geometry("400x400")
app.resizable(width=0, height=0)
app.mainloop()