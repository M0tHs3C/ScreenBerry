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
        self.tk.overrideredirect(True)
        self.tk.bind("<Escape>", lambda e: e.widget.quit())
        self.label.image = bg_image
        self.label.place(x=0,y=0, relwidth=1, relheight=1)
        tk["background"] ="green"
        self.label_pass = Label(tk, text="user       password")
        self.label_pass.pack(padx=1, pady=1)

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
        self.ciao_B = Button(tk, text="greet", command=self.ciao)
        self.ciao_B.pack()
        self.text_get =Button(tk, text="get", width=10, command=self.userback)
        self.text_get.pack(side=LEFT)
        self.get_port = Button(tk, text="GET", command=self.portgetting)
        self.get_port.pack(side=RIGHT, padx=100,pady=100)
        self.but1 = Button(tk, text="try me", command=self.ciao)
        self.but2 = Button(tk, text="exit",borderwidth=1, background="red",command=tk.quit)
        self.but3 = Button(tk, text="dir", command=self.dire)
        self.but1.pack()
        self.but2.pack(side="right",padx=10,pady=20)
        self.but3.pack()
        self.buttonpres = Button(tk, text="start", command=self.start_file)
        self.buttonpres.pack(side=TOP)
        self.buttonstop = Button(tk, text="stop", command=self.stop_file)
        self.buttonstop.pack(side=TOP)
        self.buttonstvideo = Button(tk, text='start video', command=self.start_video)
        self.buttonstvideo.pack(side=TOP)
        self.buttonstpvideo = Button(tk,text='stop video', command=self.stop_video)
        self.buttonstpvideo.pack(side=TOP)
        self.buttonshowfile = Button(tk, text='Show file',command=self.show_file)
        self.buttonshowfile.pack(side=TOP)
        self.buttonora = Button(tk , text="ora",command=self.ora_set)
        self.buttonora.pack(side=TOP)



        #SETTINGS ENTRY
        global enter_port,entry1,epassword,enterip, enterora_mattina1
        global enterora_mattina1
        enter_port = Entry(tk)
        enter_port.pack(side=RIGHT)
        enter_port.focus_set()
        entry1 = Entry(tk)
        entry1.pack(pady=100, side=LEFT)
        entry1.focus_set()
        epassword = Entry(tk)
        epassword.config(show="*")
        epassword.pack(pady=100,padx=3,side=LEFT)
        epassword.focus_set()
        enterip = Entry(tk)
        enterip.pack(side=RIGHT)
        enterip.focus_set()
        #ENTRY ORA
        enterora_mattina1 = Text(tk, height=3, width=3)
        enterora_mattina1.pack(padx=0.5, pady=1)
        #enterora_mattina1.focus_set()
        """enterora_mattina2 = Entry(tk)
        enterora_mattina2.pack(padx=90,pady=50)
        enterora_mattina2.focus_set()"""

        #RADIO VARIABLES
        global v
        v = IntVar(tk)
        v.set(0)
        self.exe_radio()



    #MAIN
    def ciao(self):
        tkMessageBox.showinfo("test","test")
    def dire(self):
        text = subprocess.check_output("ping www.google.com" ,shell=True)
        tkMessagebox.showinfo('info',text)
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
                global target_host
                global passwd
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
        autorunconf = open(path + slash +"autorun.conf", "r").read()
        timeconf = open(path + slash + "time.conf", "r").read().splitlines()
        if login_var == 1 and autorunconf == 1 :
            if ora_uno >= localtime <= ora_due: 
                try:
                    import socket
                    global target_host
                    global passwd
                    from socket import error as socket_error
                    passwd ='\xd5\xbbe6N\xf1\xec\x9aC\x1ee\xe8\xe2\xc5F`'
                    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    client.connect((target_host,int(port)))
                    client.send(passwd)
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
                    files_path = path_dir + "\\" + inp[i]
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
            radio = Radiobutton(tk, text=d, variable=v, value=a , indicatoron=0).pack(anchor=E)

            if a == len(List):
                global but
                but = Button(tk , text="verify", command=self.verify).pack(anchor=E)
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


     
    def exe_radio(self):
        self.radiobutton()
        radio
        #button
        but
    def show_file(self):
        os.system(path + slash + "showfilerasp.py " + target_host)





#EXECUTION

tk = Tk()
gui = Gui(tk)
tk.mainloop()
        

        
        
