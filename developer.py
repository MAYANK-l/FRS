
#Work Done by Harsh Gorakhnath Guddetwar and Mayank Gupta

from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from itertools import count


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="BLUE")
        title_lbl.place(x=0, y=0, width=1530, height=50)



        img_top=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\middle image.jpg")
        img_top=img_top.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=500, height=600)

        # img_top1=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\middle image.jpg")
        # img_top1=img_top1.resize((200,200),Image.Resampling.LANCZOS)
        # self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        # f_lbl=Label(main_frame, image=self.photoimg_top1)
        # f_lbl.place(x=300, y=0, width=200, height=200)

        dev_label = Label(main_frame, text="Capstone Project - 1", font=("times new roman", 30, "bold"), bg="red")
        dev_label.place(x=0,y=5)

        dev_label = Label(main_frame, text="Project Created By -\n Aniket Giri(24a12res850)\n Harsh Gorakhnath Guddetwar(24a12res934)\n Mayank Gautam(24a12res971)\n Sakshi Gupta(24a12res1205)\n Anirban Goswami(24a12res853) ", font=("times new roman", 15, "bold"), bg="white")
        dev_label.place(x=0,y=70)

        img2=Image.open(r"D:\final project\ATTENDANC3E USING FACE RECOGNITION\college pics\right image.jpg")
        img2=img2.resize((500,390),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=0, y=210, width=500, height=390)











if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()   