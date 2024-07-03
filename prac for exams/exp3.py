import tkinter as tk


def login():
    if username_entry.get()=="admin" and password_entry.get()=="password":
        tk.messagebox.showinfo("sucess")
    else:
        tk. messagebox.showinfo("noo")

root=tk.Tk()
root.title("login form")
root.geometry("300*200")

username_label=tk.label(root,text="username",width=10,hieght)
username_lable.pack()


root.mainloop()
