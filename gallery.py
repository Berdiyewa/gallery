from tkinter import *
from PIL import ImageTk, Image

tk = Tk()
tk.title('Photo project')
tk.config(bg='white')


my_img = ImageTk.PhotoImage(Image.open('photo/1.jpg').resize((900,700), Image.BILINEAR))
my_img1 = ImageTk.PhotoImage(Image.open('photo/2.jpg').resize((900,700), Image.BILINEAR))
my_img2 = ImageTk.PhotoImage(Image.open('photo/3.jpg').resize((900,700), Image.BILINEAR))
my_img3 = ImageTk.PhotoImage(Image.open('photo/4.jpg').resize((900,700), Image.BILINEAR))
my_img4 = ImageTk.PhotoImage(Image.open('photo/5.jpg').resize((900,700), Image.BILINEAR))
my_img5 = ImageTk.PhotoImage(Image.open('photo/6.jpg').resize((900,700), Image.BILINEAR))
my_img6 = ImageTk.PhotoImage(Image.open('photo/7.jpg').resize((900,700), Image.BILINEAR))
my_img7 = ImageTk.PhotoImage(Image.open('photo/8.jpg').resize((900,700), Image.BILINEAR))
my_img8 = ImageTk.PhotoImage(Image.open('photo/9.jpg').resize((900,700), Image.BILINEAR))
my_img9 = ImageTk.PhotoImage(Image.open('photo/10.jpg').resize((900,700), Image.BILINEAR))
my_img10 = ImageTk.PhotoImage(Image.open('photo/11.jpg').resize((900,700), Image.BILINEAR))
my_img11 = ImageTk.PhotoImage(Image.open('photo/12.jpg').resize((900,700), Image.BILINEAR))
my_img12 = ImageTk.PhotoImage(Image.open('photo/13.jpg').resize((900,700), Image.BILINEAR))
my_img13 = ImageTk.PhotoImage(Image.open('photo/14.jpg').resize((900,700), Image.BILINEAR))
my_img14 = ImageTk.PhotoImage(Image.open('photo/15.jpg').resize((900,700), Image.BILINEAR))
my_img15 = ImageTk.PhotoImage(Image.open('photo/16.jpg').resize((900,700), Image.BILINEAR))



image_list =[my_img, my_img1, my_img2, my_img3, my_img4,
             my_img5, my_img6, my_img7, my_img8, my_img9,
             my_img10, my_img11, my_img12, my_img13, my_img14,
             my_img15]



my_label = Label(image = my_img)
my_label.grid(row = 0, column = 0, columnspan = 3)

def forward(image_number):
    global my_label
    global btn_forward
    global btn_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number - 1])
    btn_forward = Button(tk, text = "--->>>", command = lambda: forward(image_number + 1))
    btn_back = Button(tk, text = "<<<---", command = lambda: back(image_number - 1))

    if image_number == 16:
        btn_forward = Button(tk, text = "--->>>", state = DISABLED )
        
    
    my_label.grid(row =0, column = 0, columnspan = 3)
    btn_back.grid(row = 1, column = 0)
    btn_forward.grid(row = 1, column = 2)

def back(image_number):
    global my_label
    global btn_forward
    global btn_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number - 1])
    btn_forward = Button(tk, text = "--->>>", command = lambda: forward(image_number + 1))
    btn_back = Button(tk, text = "<<<---", command = lambda: back(image_number - 1))

    if image_number == 1:
        btn_back =Button(tk, text = "<<<---", state = DISABLED)
    
    my_label.grid(row =0, column = 0, columnspan = 3)
    btn_back.grid(row = 1, column = 0)
    btn_forward.grid(row = 1, column = 2)

btn_back = Button(tk, text = "<<<---", command = back, state = DISABLED )
btn_exit = Button(tk, text = 'EXIT PROGRAMM', command = quit)
btn_forward = Button(tk, text = "--->>>", command = lambda:  forward(2))

btn_back.grid(row = 1, column = 0)
btn_exit.grid(row = 1, column = 1)
btn_forward.grid(row = 1, column = 2)

tk.mainloop()





















