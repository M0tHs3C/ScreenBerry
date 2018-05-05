from Tkinter import *
from ftplib import FTP, error_perm
import sys
global host

host_raw = sys.argv[1]
host = str(host_raw)
wallpaper = "/home/pi/wallpaper/"
unactive_wallpaper = "/home/pi/unactive_wallpaper/"
gif = "/home/pi/gif/"
unactive_gif = "/home/pi/unactive_gif/"

class Gui:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x800")
        self.root.title("show files ready to be displayed on "+ host)
        self.frame = Frame(root).pack()
        self.active = Button(self.frame, text="active ->", command=self.active, anchor=CENTER).place(relx=.5, rely=.45, anchor="center")
        self.deactive = Button(self.frame, text="<- deactive", command=self.deactive).place(relx=.5, rely=.5, anchor="center")
        self.delete = Button(self.frame, text="delete", command=self.delete).place(relx=.5, rely=.55, anchor="center")
        self.get_data = Button(self.frame, text="get data", command=self.update).place(relx=.5, rely=.4, anchor="center")
        self.file_open = Button(self.frame, text="open file", command=self.onOpen)
        self.dir_open = Button(self.frame, text="open directory",command= self.dirOpen)
        self.file_open.pack()
        self.dir_open.pack()
        self.scrollbar = Scrollbar(root)
        self.scrollbar.pack(side=RIGHT, fill=Y, expand=False)
        self.list = Listbox(self.frame, yscrollcommand = self.scrollbar.set, selectmode=EXTENDED)
        self.list.pack(side=LEFT, fill=Y, expand=True)
        self.scrollbar.config(command=self.list.yview)
        self.list.config(width=40)
        self.list2 = Listbox(self.frame, yscrollcommand=self.scrollbar.set, selectmode=EXTENDED)
        self.list2.pack(side=LEFT, fill=Y, expand=True)
        self.scrollbar2 = Scrollbar(root)
        self.scrollbar2.pack(side=LEFT, fill=Y, expand=False)
        self.scrollbar2.config(command=self.list.yview)
        self.list2.config(width=40)

    def dirOpen(self):
        if target_host != '':
            dirname = tkFileDialog.askdirectory(parent=tk, initialdir="/", title='Please select a directory')
            path_dir = dirname
            inp = os.listdir(path_dir)
            dir_path = "/home/pi/wallpaper/"
            try:
                ftp = FTP(target_host)
                ftp.login(user, passwd_user)
                for i in range(0, len(inp)):
                    files_path = path_dir + "\\" + inp[i]
                    ftp.cwd(dir_path)
                    pending_files = open(files_path, "rb")
                    ftp.storbinary('STOR ' + inp[i], pending_files)
                ftp.quit()
                ftp.close()
            except error_perm:
                tkMessageBox.showinfo('Login', 'Login incorrect')
            except socket_error:
                tkMessageBox.showinfo('Login', 'Host Down')
        elif target_host == '':
            tkMessageBox.showinfo('Error', 'Select and address to send')


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


    def deactive(self):
        item = self.list2.curselection()
        item = map(int, item)
        ftp = FTP(host)
        ftp.login("pi", "abc")
        for i in range(0, len(item)):
            try:
                ftp.cwd(unactive_wallpaper)
                ftp.sendcmd("RNFR " + wallpaper + self.active_list[item[i]])
                ftp.sendcmd('RNTO ' + self.active_list[item[i]])
            except error_perm:
                try:
                    ftp.cwd(unactive_gif)
                    ftp.sendcmd("RNFR " + gif + self.active_list[item[i]])
                    ftp.sendcmd('RNTO ' + self.active_list[item[i]])
                except:
                    pass
            except:
                pass
        self.update()

    def active(self):
        item = self.list.curselection()
        item = map(int, item)
        ftp = FTP(host)
        ftp.login("pi", "abc")
        for i in range(0, len(item)):
            try:
                ftp.cwd(wallpaper)
                ftp.sendcmd("RNFR " + unactive_wallpaper + self.unactive_list[item[i]])
                ftp.sendcmd('RNTO ' + self.unactive_list[item[i]])
            except error_perm:
                try:
                    ftp.cwd(gif)
                    ftp.sendcmd("RNFR " + unactive_gif + self.unactive_list[item[i]])
                    ftp.sendcmd('RNTO ' + self.unactive_list[item[i]])
                except:
                    pass
            except:
                pass
        self.update()
    def delete(self):
        item = self.list.curselection()
        item = map(int, item)
        ftp = FTP(host)
        ftp.login("pi", "abc")
        for i in range(0, len(item)):
            try:
                ftp.cwd(unactive_wallpaper)
                ftp.delete(self.unactive_list[item[i]])
            except:
                try:
                    ftp.cwd(unactive_gif)
                    ftp.delete(self.unactive_list[item[i]])
                except:
                    pass

    def update(self):
        self.list.delete(0, END)
        self.list2.delete(0, END)
        ftp = FTP(host)
        ftp.login("pi", "abc")
        ftp.cwd(wallpaper)
        self.active_list = ftp.nlst()
        ftp.cwd(gif)
        giflist = ftp.nlst()
        for i in giflist:
            self.active_list.append(i)
        ftp.cwd(unactive_wallpaper)
        self.unactive_list = ftp.nlst()
        ftp.cwd(unactive_gif)
        ungif = ftp.nlst()
        for i in ungif:
            self.unactive_list.append(i)

        for i in self.active_list:
            self.list2.insert(END, i)
        for i in self.unactive_list:
            self.list.insert(END, i)






root = Tk()

gui = Gui(root)

root.mainloop()


