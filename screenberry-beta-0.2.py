#!/usr/bin/python
#_*_ coding: utf-8 _*_

#IMPORT
#from tkinter import *
from Tkinter import *
import tkMessageBox
import tkFileDialog
import os
import subprocess
import re
import sys
from ftplib import FTP , error_perm
import time

#VARIABLES
login_var = 0
target_host = ''
global localtime
localtime = time.localtime(time.time())
localtime = localtime[3]





class Gui:
    def __init__(self,tk):

        #SETTING WIN
        global os,path,slash
        os_get = sys.platform
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        if os_get == "linux2":
            slash = "/"
        else:
            slash ="\\"
        self.tk = tk
        tk.title("ScreenBerry")
        path = os.path.abspath(os.path.dirname(sys.argv[0]))
        tk.geometry("{0}x{1}+0+0".format(self.tk.winfo_screenwidth(), self.tk.winfo_screenheight()))
        bg_image = PhotoImage(file=path + slash +"image.gif")
        self.label = Label(tk, text="test beta 1", image=bg_image)
        #self.label.pack()
        self.tk.bind("<Escape>", lambda e: e.widget.quit())
        self.label.image = bg_image
        self.label.place(x=0,y=0, relwidth=1, relheight=1)
        tk["background"] ="green"
        self.label_pass = Label(tk, text="user       password")
        #self.label_pass.config(image=bg_image)
        self.label_pass.place(relx=.01, rely=.07)
        auto_run_var = open(path + slash +"autorun.conf","r").read().splitlines()
        auto_run_var = auto_run_var[0]
        auto_run_var = int(auto_run_var)
        if auto_run_var == 0:
            text_auto = "OFF"
        elif auto_run_var ==1:
            text_auto = "ON"

        #MENU
        self.menubar = Menu(tk)
        self.show_menu = Menu(tk, tearoff=0)
        self.show_menu.add_command(label="Select File",command=self.onOpen)
        self.show_menu.add_command(label="Select Dir", command=self.dirOpen)
        self.show_menu.add_separator()
        self.show_menu.add_command(label="Quit",command=tk.quit)
        self.about_menu = Menu(tk)
        self.about_menu.add_command(label="about",command=self.ciao)
        self.about_menu.add_command(label="help",command=self.ciao)
        self.menubar.add_cascade(label="Show", menu=self.show_menu)
        self.menubar.add_cascade(label="About",menu=self.about_menu)
        self.tk.config(menu=self.menubar)


        #SETTINGS BUTTON
        global button_auto_run
        self.text_get =Button(tk, text="login", width=10, command=self.userback)
        self.text_get.place(relx=.01, rely=.15)
        self.get_port = Button(tk, text="ADD MONITOR", command=self.portgetting)
        self.get_port.place(relx=.1,rely=.56)
        self.but2 = Button(tk, text="exit",borderwidth=1, background="red",command=tk.quit)
        self.but2.place(relx=0.97,rely=0.01)
        self.buttonpres = Button(tk, text="start ►", command=self.start_file)
        self.buttonpres.place(relx=.01,rely=.2)
        self.buttonstop = Button(tk, text="stop ■", command=self.stop_file)
        self.buttonstop.place(relx=.01,rely=.23)
        self.buttonstvideo = Button(tk, text='start video', command=self.start_video)
        self.buttonstvideo.place(relx=.01,rely=.26)
        self.buttonstpvideo = Button(tk,text='stop video', command=self.stop_video)
        self.buttonstpvideo.place(relx=.01,rely=.29)
        self.buttonshowfile = Button(tk, text='Show file',command=self.show_file)
        self.buttonshowfile.place(relx=0.1, rely=.4)
        self.buttonora = Button(tk , text="ora",command=self.ora_set)
        self.buttonora.place(relx=.93,rely=.29)
        self.button_write_host = Button(tk, text="SAVE MONITOR" ,command=self.write_host)
        self.button_write_host.place(relx=.15,rely=.56)
        self.button_auto_run = Button(tk, text=text_auto, command=self.auto_start_exec)
        self.button_auto_run.place(relx=.1,rely=.1)



        #SETTINGS ENTRY
        global enter_port,entry1,epassword,enterip, enterora_mattina1
        global enterora_mattina1
        enter_port = Entry(tk)
        enter_port.place(relx=.1, rely=.53)
        enter_port.focus_set()
        entry1 = Entry(tk)
        entry1.place(relx=.01, rely=.1)
        entry1.focus_set()
        epassword = Entry(tk)
        epassword.config(show="*")
        epassword.place(relx=.01, rely=.13)
        epassword.focus_set()
        enterip = Entry(tk)
        enterip.place(relx=.1, rely=.5)
        enterip.focus_set()
        #ENTRY ORA
        enterora_mattina1 = Text(tk, height=.5, width=3)
        enterora_mattina1.place(relx=0.9, rely=.3, anchor="e")
        enterora_mattina2 = Text(tk, height=.5, width=3)
        enterora_mattina2.place(relx=0.92, rely=.3, anchor="e")


        #RADIO VARIABLES
        global v
        v = IntVar(tk)
        v.set(0)
        self.exe_radio()
        self.auto_start_photo()



    #MAIN
    def ciao(self):
        pass
    def start_file(self):
        if login_var == 1:
            try:
                import socket
                global target_host
                global passwd
                from socket import error as socket_error
                passwd = '\xd5\xbbe6N\xf1\xec\x9aC\x1ee\xe8\xe2\xc5F`'
                client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                client.connect((target_host, int(port)))
                client.send(passwd)
                tkMessageBox.showinfo('result', 'started')
            except OverflowError:
                ofe = "port not legal"
                tkMessageBox.showinfo('Error', ofe)
            except socket_error:
                not_rsp = "the port is not responding"
                tkMessageBox.showinfo('Error',not_rsp)
        elif login_var == 0:
            tkMessageBox.showinfo("error","you must login first")
    def start_video(self):
        if login_var == 1:
            try:
                import socket
                global target_host
                global passwd
                from socket import error as socket_error
                passwd = '\xfe\xc7P\xa6\x88\xfe\xac\xdbF\xb9\xfdZ\x87\x909\xfa'
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect((target_host, int(port)))
                client.send(passwd)
                tkMessageBox.showinfo('result','started')
            except OverflowError:
                ofe = "port not legal"
                tkMessageBox.showinfo('Error', ofe)
            except socket_error:
                not_rsp = "the port is not responding"
                tkMessageBox.showinfo('Error', not_rsp)
        elif login_var == 0:
            tkMessageBox.showinfo("error", "you must login first")
    def stop_file(self):
        if login_var == 1:
            try:
                import socket
                global target_host
                global passwd
                from socket import error as socket_error
                passwd = '\xb9\x96\xda\xb8G\x05\x99\x14\xc6\xe7*\xd4\xe9\x08~\xb5'
                client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                client.connect((target_host, int(port)))
                client.send(passwd)
                tkMessageBox.showinfo('result', 'stopped')
            except OverflowError:
                ofe = "port not legal"
                tkMessageBox.showinfo('Error', ofe)
            except socket_error:
                not_rsp = "the port is not responding"
                tkMessageBox.showinfo('Error',not_rsp)
        elif login_var == 0:
            tkMessageBox.showinfo("error","you must login first")
    def stop_video(self):
        if login_var == 1:
            try:
                import socket
                from socket import error as socket_error
                passwd = '\x80\x8f\xf6{\xb7\x82\x8bPZ\x88\xdal\x15.7\x17'
                client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                client.connect((target_host, int(port)))
                client.send(passwd)
                tkMessageBox.showinfo('result', 'stopped')
            except OverflowError:
                ofe = "port not legal"
                tkMessageBox.showinfo('Error', ofe)
            except socket_error:
                not_rsp = "the port is not responding"
                tkMessageBox.showinfo('Error',not_rsp)
        elif login_var == 0:
            tkMessageBox.showinfo("error","you must login first")
    def auto_start_photo(self):
        target_host = "192.168.4.40"
        port = 136
        autorunconf = open(path + slash +"autorun.conf", "r").read().splitlines()
        autorunconf = autorunconf[0]
        autorunconf = int(autorunconf)
        timeconf = open(path + slash + "time.conf", "r").read().splitlines()
        ora_uno =     int(timeconf[0])
        ora_due =     int(timeconf[1])
        ora_tre =     int(timeconf[2])
        ora_quattro = int(timeconf[3])
        ora_cinque =  int(timeconf[4])
        ora_sei =     int(timeconf[5])
        ora_sette =   int(timeconf[6])
        ora_otto =    int(timeconf[7])
        if autorunconf == 1 :
            if ora_uno >= localtime < ora_due:
                try:
                    import socket
                    from socket import error as socket_error
                    passwd ='\xd5\xbbe6N\xf1\xec\x9aC\x1ee\xe8\xe2\xc5F`'#prima presentazione
                    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    client.connect((target_host,int(port)))
                    client.send(passwd)
                except OverflowError:
                    pass
                except socket_error:
                    pass
            elif ora_tre >= localtime <= ora_quattro:
                try:
                    import socket
                    from socket import error as socket_error
                    passwd = '\xd5\xbbe6N\xf1\xec\x9aC\x1ee\xe8\xe2\xc5F`'#seconda
                    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client.connect((target_host, int(port)))
                    client.send(passwd)
                except OverflowError:
                    pass
                except socket_error:
                    pass
            elif ora_cinque >= localtime <= ora_sei:
                try:
                    import socket
                    from socket import error as socket_error
                    passwd = '\xd5\xbbe6N\xf1\xec\x9aC\x1ee\xe8\xe2\xc5F`'#terza
                    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client.connect((target_host, int(port)))
                    client.send(passwd)
                except OverflowError:
                    pass
                except socket_error:
                    pass
            elif ora_sette >= localtime <= ora_otto:
                try:
                    import socket
                    from socket import error as socket_error
                    passwd = '\xd5\xbbe6N\xf1\xec\x9aC\x1ee\xe8\xe2\xc5F`'#quarta
                    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    client.connect((target_host, int(port)))
                    client.send(passwd)
                except OverflowError:
                    pass
                except socket_error:
                    pass





    def userback(self):
        global user
        global passwd_user
        global login_var
        user = entry1.get()
        passwd_user = epassword.get()
        if user == "pi" and passwd_user == "abc":
            tkMessageBox.showinfo('Login', 'User accepted')
            login_var = 1
        else:
            tkMessageBox.showinfo('Login', 'User not recognized')
            login_var = 0
    def portgetting(self):
        global port
        global target_host
        port = enter_port.get()
        target_host = enterip.get()
    def onOpen(self):
        if target_host != '':
            tk.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
            a = tk.filename
            dir_path = "/home/pi/wallpaper/"
            try:
                ftp = FTP(target_host)
                ftp.login(user,passwd_user)
                pending_file = open(a, "rb")
                pending_name_file = os.path.split(a)[1]
                ftp.cwd(dir_path)
                ftp.storbinary('STOR '+ pending_name_file, pending_file)
                ftp.quit()
                ftp.close()
            except error_perm:
                tkMessageBox.showinfo('Login','Login incorrect')
            except socket_error:
                tkMessageBox.showinfo('Login','Host Down')
        elif target_host == '':
            tkMessageBox.showinfo('Error', 'Select and address to send')
    def dirOpen(self):
        if target_host != '':
            dirname = tkFileDialog.askdirectory(parent=tk, initialdir="/", title='Please select a directory')
            path_dir = dirname
            inp = os.listdir(path_dir)
            dir_path = "/home/pi/wallpaper/"
            try:
                ftp = FTP(target_host)
                ftp.login(user,passwd_user)
                for i in range(0, len(inp)):
                    files_path = path_dir + slash + inp[i]
                    ftp.cwd(dir_path)
                    pending_files = open(files_path, "rb")
                    ftp.storbinary('STOR '+ inp[i], pending_files)
                ftp.quit()
                ftp.close()
            except error_perm:
                tkMessageBox.showinfo('Login','Login incorrect')
            except socket_error:
                tkMessageBox.showinfo('Login','Host Down')
        elif target_host == '':
            tkMessageBox.showinfo('Error', 'Select and address to send')





    def verify(self):
        global sel
        global target_host
        global port
        sel = v.get()
        
        if sel == sel:
            global res
            sel -= 1
            res = List[sel]
            tkMessageBox.showinfo("you choose:",res)
        def extract_selection():
            global target_host
            global port
            pattern_1 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
            pattern_2 = r'(\:).*'
            match1 = re.search(pattern_1, res[0])
            match2 = re.search(pattern_2, res[0])
            if match1 and match2:
                target_host = match1.group()
                port_raw = match2.group()
                port = port_raw[1:]
        extract_selection()
        
        
    def radiobutton(self):
        global a
        def number():
            global sel
            sel = a
            tkMessageBox.showinfo('choose', List[sel])
            
        i = 0
        f = 0.4
        global List

        global b
        List = open(path + slash + "screenberry.conf", "r").read().splitlines()
        for Line in List:
            List[i]=Line.split("|")
            i += 1
        a = 0
        b = 0
        while a < len(List):
            d = List[a]

            global radio
            global button
            a += 1
            f += .03
            radio = Radiobutton(tk, text=d, variable=v, value=a , indicatoron=0).place(relx=.06,rely=f, anchor=E)

            if a == len(List):
                global but
                but = Button(tk , text="verify", command=self.verify).place(relx=.01, rely=0.35)
    def ora_set(self):
        a = enterora_mattina1.get()
        tkMessageBox.showinfo('ora mattina', a)
        """if localtime >= 6 and localtime <= 11:
            print" mattina"
        if localtime >= 12 and localtime <= 14:
            print"ora di pranzo"
        if localtime >= 14 and localtime <= 18:
            print"pomeriggio"
        if localtime >= 18 and localtime <= 20:
            print "ora di cena"""
    def ora_changer_conf():
        with open(path + slash + "time.conf", "r") as file:
            data = file.readlines()
        data[5] = 'ciao\n'
        with open(path + slash + "time.conf", "w") as file:
            file.writelines(data)
    def autostartsetter(self):
        auto_run = open(path + slash + "autorun.conf", "r").read().splitlines()
        auto_run = int(auto_run[0])
        if auto_run == 0:
            with open(path + slash + "autorun.conf","r") as file:
                data = file.readlines()
            data[0] = '1'
            with open(path + slash + "autorun.conf", "w") as file:
                file.writelines(data)
        elif auto_run == 1:
            with open(path + slash + "autorun.conf","r") as file:
                data = file.readlines()
            data[0] = '0'
            with open(path + slash + "autorun.conf","w") as file:
                file.writelines(data)
    def exe_radio(self):
        self.radiobutton()
        radio
        #button
        but
    def show_file(self):
        os.system(path + slash + "showfilerasp.py " + target_host)
    def write_host(self):
        self.portgetting()
        List = open(path + slash + "screenberry.conf", "a")
        host_full = target_host+":"+port
        List_read = open(path+ slash+ "screenberry.conf", "r").read().splitlines()
        if host_full not in List_read:
            List.write("\n"+target_host+":"+port)
            List.close()
            self.exe_radio()
        elif host_full in List_read:
            tkMessageBox.showinfo("ERROR","MONITOR ALREADY SAVED")
    def toggle_text(self):
        if self.button_auto_run["text"] == "ON":
            self.button_auto_run["text"] = "OFF"
        else:
            self.button_auto_run["text"] = "ON"
    def auto_start_exec(self):
        self.toggle_text()
        self.autostartsetter()





#EXECUTION

tk = Tk()
tk.attributes("-fullscreen", True)
gui = Gui(tk)
tk.mainloop()
        

        
        
