from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyperclip
import string
import random

root = Tk()

root.title("Password-Generator")
root.geometry("640x400+350+150")
root.resizable(height=FALSE, width=False)


#===============Clear Programme===============
def clear_programme():
    option.set("Options")
    password_variable.set("")
    output_text.config(state=NORMAL)
    output_text.delete('1.0', END)
    output_text.config(state=DISABLED)
    generate_btn.config(state=NORMAL)
    option.config(state=NORMAL)
    copy_btn.config(state=DISABLED)
    clear_btn.config(state=DISABLED)


#=================Copy Programme===========
def copy_programme():
    output_text.config(state=NORMAL)
    pyperclip.copy(output_text.get('1.0', END))
    messagebox.showinfo("Info!", "Copied!")
    output_text.config(state=DISABLED)
    copy_btn.config(state=DISABLED)


#=================Generate Programme=======
def generate_programme():
    selected_option = option.get()
    password_length = password_length_entry.get()
    
    if selected_option == "Options":
        messagebox.showwarning("Warning!", "Select Option!")
    elif password_length == "":
        messagebox.showwarning("Warning", "Set Password Length")
    elif not password_length.isdigit():
        messagebox.showerror("Error!", "Length should be an integer.")
    else:
        password_length = int(password_length)
        if password_length < 1 or password_length >= 100:
            messagebox.showwarning("Warning!", "Password length should be between 1 and 99.")
        else:
            password_characters = ""
            if "Upper Case" in selected_option:
                password_characters += string.ascii_uppercase
            if "Lower Case" in selected_option:
                password_characters += string.ascii_lowercase
            if "Digits" in selected_option:
                password_characters += string.digits
            if "Characters" in selected_option:
                password_characters += string.punctuation

            if password_characters == "":
                messagebox.showwarning("Warning!", "Select at least one character type!")
            else:
                generated_password = ''.join(random.choice(password_characters) for _ in range(password_length))
                output_text.config(state=NORMAL)
                output_text.delete('1.0', END)
                output_text.insert(END, generated_password)
                output_text.config(state=DISABLED)
                generate_btn.config(state=DISABLED)
                copy_btn.config(state=NORMAL)
                clear_btn.config(state=NORMAL)
    


#==============Password Generator Text=================
intro = Label(root, text="Password Generator", font=("Times new roman", 15, "bold"), bg="gold", fg="red")
intro.pack(fill=BOTH)



#==============Select Option Text=====================
option_label = Label(root, text="Select Option: ", fg="#262626", font=("Times new roman", 12, "bold"))
option_label.place(x=20, y=45)


#==============Option Menu============================
option = ttk.Combobox(root, width=45, values=("Only Upper Case", "Only Lower Case", "Only Digits", "Only Characters", "Upper Case + Lower Case", "Upper Case + Digits", "Upper Case + Characters", "Lower Case + Digits", "Lower Case + Characters", "Digits + Characters", "Upper Case + Lower Case + Digits", "Upper Case + Lower Case + Characters", "Upper Case + Lower Case + Digits + Characters"), state="readonly")
option.set("Options")
option.place(x=170, y=48)



#=================Set Password Length Text=============
password_length_label = Label(root, text="Set Password Length: ", fg="#262626", font=("Times new roman", 10, "bold"))
password_length_label.place(x=20, y=90)


#================Variable For Password Storing
password_variable = StringVar()


#================Password Entry================
password_length_entry = Entry(root, bd=2, relief=RIDGE, textvariable=password_variable)
password_length_entry.place(x=250, y=90)




#=============Frame For Generated Password============
output = LabelFrame(root, text="Generated Password", bd=7, relief=GROOVE, font=("Segoe Script", 12, "bold"), fg="purple")
output.place(x=110, y=200, height=75, width=420)


#==============Scrollbar For Frame================
scroolbar_for_output = Scrollbar(output, orient=HORIZONTAL, cursor="hand2")
scroolbar_for_output.pack(side=BOTTOM, fill=X)


#==============Text Area In Frame=================
output_text = Text(output, wrap=NONE, xscrollcommand=scroolbar_for_output.set)
output_text.pack(fill=BOTH, expand=1)



#===============Configuring Scrollbar==============
scroolbar_for_output.config(command=output_text.xview)


#===============Setting State of Frame Disabled==========
output_text.config(state=DISABLED)


#===============Generate Button==============
generate_btn = Button(root, text="Generate", bd=5, relief=RIDGE, bg="green", cursor="hand2", fg="white", font=("times new roman", 11, "bold"), activebackground="lightgray", command=generate_programme)
generate_btn.place(x=110, y=310)



#===============Copy Button==============
copy_btn = Button(root, text="Copy", bd=4, relief=RIDGE, bg="orange", fg="white", cursor="hand2", font=("times new roman", 11, "bold"), activebackground="lightgray", command=copy_programme)
copy_btn.place(x=290, y=310)
copy_btn.config(state=DISABLED)


#===============Clear Button==============
clear_btn = Button(root, text="Clear *", bd=4, relief=RIDGE, bg="red", fg="white", cursor="hand2", font=("times new roman", 11, "bold"), activebackground="lightgray", command=clear_programme)
clear_btn.place(x=460, y=310)
clear_btn.config(state=DISABLED)


root.mainloop()