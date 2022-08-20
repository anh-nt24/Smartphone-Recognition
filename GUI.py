from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.font import Font
from PIL import Image, ImageTk
from rec import recognizer



def browse():
    filename = askopenfilename()
    img = ImageTk.PhotoImage(Image.open(filename).resize((600,400)))
    label.image = img
    label['image'] = img
    label.pack()

    new_img, s = recognizer(filename)
    new_img =  ImageTk.PhotoImage(image=Image.fromarray(new_img))
    display.image = new_img
    display['image'] = new_img
    display.pack()
    st.set(s)



height = 900
width = 1300
master = Tk()
master.title("Smartphone Recognition")
canvas = Canvas(master, height=height, width=width)
canvas.pack()
filename = ''
st = StringVar(master)

border = 2
width = 650
height = 450
color = '#f8f8ff'

# Original image box
inp = Frame(master, width=width, height=height, bd=border, bg= color)
inp.place(relx=0.05, rely=0.04, relwidth=0.45, relheight=0.45, anchor=NW)


label = Label(inp)


br = Frame(master, bg= '#ccc', bd= border)
br.place(relx=0.9, rely=0.3, anchor=NE)
b = Button(br, width=20, height=2, text="BROWSE", command=browse)
b['font'] = Font(size=13)
b.pack()



# Result image box
out = Frame(master, width=width, height=height, bd=border, bg= color)
out.place(relx=0.05, rely=1-0.04, relwidth=0.45, relheight=0.45, anchor=SW)
display = Label(out)

status = Frame(master, width=width/1.5, height=60, bd=border, bg='yellow')
status.place(relx=0.92, rely=1-0.3, anchor=NE)
if filename == '':
    result = Label(status, bg='yellow', fg='red', text="The result will display here...", font=('Arial', 16)).place(relx=0.05, rely=0.25)

result = Label(status, bg='yellow', fg='red', textvariable=st, font=('Arial', 16)).place(relx=0.05, rely=0.25)
master.mainloop()