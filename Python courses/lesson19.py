from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('This is tkinter program')
# root.geometry('100x100')
# # #
# # #
# # # # Show info (showinfo)
# # # # Show warning  ( showwarning)
# # # # Show error  (showerror)
# # # # Ask quastion  (askquastion)
# # # # Ask, ok, cancel (askokcancel)
# # # # Ask, yes, no  (askyesno)
# # #
# # # def clicked():
# # #     # # messagebox.showinfo('This is window title', 'This is window message')
# # #     # responce = messagebox.askyesno('This is window title', 'This is window body')
# # #     responce = messagebox.askyesno('This is window title', 'This is window body')
# # #
# # #     if responce == 0:
# # #         Label(root, text='User chose NO').pack()
# # #     else:
# # #         Label(root, text='User chose YES').pack()
# # #
# # #
# # # Label_var = StringVar()
# # # myLabel = Label(root, textvariable=label_var).pack()
# # # mybutton = Button(root, text='Click me', comand=clicked).pack()
# # #
# # #
# # #
# # # print(dir(messagebox.askcancel()))
# # # root.mainloop()
# #
# # check_var = InVar()
# # # check_box = Checkbutton(root, text='Check me', variable=check_var).pack()
# # check_box = Checkbutton(root, text='Check me', variable=check_var)\
# # check_box.pack()
# #
# # label_var = IntVar()
# # def check_status():
# #     label_var.set(check_var.ger())
# #
# #
# #
# # # mylable = Lable(root, text=chk_box.get()).pack()
# # mylable = Lable(root, text=label_var).pack()
# # mybutton = Button(root, text='Click me', command=check_status).pack()
# #
#
# # DropDownMenu
#
# def show():
#     Label(root, text=clicked.get()).pack()
#
# menu_list = [
#     'Manday',
#     'Tuesday',
#     'Wednesday',
#     'Thursday',
# ]
# clicked = StringVar()
# # dropdown = OptiMenu(root, clicker, 'Monday', 'Tuesday', 'Wednesday', 'Thursday')
# dropdown = OptionMenu(root, clicked, *menu_list)
# clicked.set('Chose day')
# dropdown.pack()
#
#
# mybutton = Button(root, text='Show selection', command=show).pack()
#
# root.mainloop()



# Slider
#
# vertical = Scale(root, from_=0, to=255)
# vertical.pack()
#
# horizontal = Scale(root, from_=0, to=255, orient=HORIZONTAL)
# harizontal.pack()
#
#
# root.mainloop()


horizontal = Scale(root, from_=0, to=255, orient=HORIZONTAL)
harizontal.pack()

slide_var = StringVar()

def slide():
    slide_var.set(horizontal.get())

mylabel = Label(root, textvariable=slide_var)
mylabel.pack()

mybutton = Button(root, text='Click me', command=slide)
mybutton.pack()


root.mainloop()