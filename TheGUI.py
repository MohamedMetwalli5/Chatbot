from chat import get_response, bot_name
import tkinter
from PIL import ImageTk, Image



def GetInput():
    output_text_box.delete("1.0", "end")
    input = input_text_box.get(1.0, "end-1c")
    output = get_response(input)
    input_text_box.delete("1.0","end")
    output_text_box.insert(tkinter.INSERT, output)


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


input_text_box = tkinter.Text(root, height=2, width=300)
input_text_box.pack()
input_text_box.place(x=0, y=250)


img = ImageTk.PhotoImage(Image.open("BackGround.PNG"))
l_image = tkinter.Label(root, image=img)
l_image.pack()


input_text_box = tkinter.Text(root, height=2, width=300)
input_text_box.pack()
input_text_box.place(x=0, y=250)


button = tkinter.Button(root, text="Send", command=GetInput)
button.configure(bg='purple')
button.configure(fg='black')
button.pack()
button.place(x=150, y=300)


root.mainloop()
