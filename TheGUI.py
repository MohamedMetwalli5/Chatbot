import tkinter
from PIL import ImageTk, Image

input = ""

def GetInput():
    inp = input_text_box.get(1.0, "end-1c")
    input = inp
    print(input)
    # lbl.config(text=inp)


root = tkinter.Tk()
root.title("Alex: The Chatbot")
root.wm_minsize(350, 400)
root.wm_maxsize(350, 400)
root.configure(bg='black')


l_title = tkinter.Label(root, text="Alex 🤖")
l_title.configure(bg='black')
l_title.configure(fg='white')
l_title.config(font=("Courier", 16))
l_title.pack()

output_text_box = tkinter.Text(root, height=2, width=300)
output_text_box.configure(bg='yellow')
output_text_box.pack()
# output_text_box.place(x=0, y=250)


input_text_box = tkinter.Text(root, height=2, width=300)
input_text_box.pack()
input_text_box.place(x=0, y=250)


img = ImageTk.PhotoImage(Image.open("BackGround.PNG"))
l_image = tkinter.Label(root, image=img)
l_image.pack()

# T2 = tkinter.Text(root, height=2, width=300)
# Fact = """The text to be written"""
# T2.insert(tkinter.END, Fact)
# T2.pack()
# T2.place(x=0, y=250)

# l_robot_words = tkinter.Label(root, text="")
# l_robot_words.configure(fg='black')
# l_robot_words.config(font=("Courier", 14))
# l_robot_words.pack()


input_text_box = tkinter.Text(root, height=2, width=300)
input_text_box.pack()
input_text_box.place(x=0, y=250)


button = tkinter.Button(root, text="Send", command=GetInput)
button.configure(bg='yellow')
button.configure(fg='black')
button.pack()
button.place(x=150, y=300)

root.mainloop()
