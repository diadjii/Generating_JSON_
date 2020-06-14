import json

from tkinter import *
from tkinter import messagebox

my_window = Tk()

my_window.title("Generateur de Fichier JSON")
# my_window.maxsize(width=1000, height=500)

input_name = Entry(my_window, width=25)
input_name.grid(row=1,column=1,padx=10,pady=10)

input_age = Entry(my_window, width=25)
input_age.grid(row=2,column=1,padx=10,pady=10)

input_country = Entry(my_window, width=25)
input_country.grid(row=3,column=1,padx=10,pady=10)
# input_name.pack()
title = Label(my_window,text="Generateur de Fichier JSON").grid(row=0,column=1)

label_name =Label(my_window, text="Name :").grid(row=1,padx=10)
label_name =Label(my_window, text="Age :").grid(row=2,padx=10)
label_name =Label(my_window, text="Country :").grid(row=3,padx=10)

def save():
    name = input_name.get()
    age = input_age.get()
    country = input_country.get()

    person = {"name":name, "age":age, "country":country}

    if name or age or country :
        data=[]

        with open("data.json") as json_file:
            data = json.load(json_file)

        with open("data.json","w") as json_file:
            data['people'].append(person)
            json.dump(data, json_file, indent=2)

            messagebox.showinfo("Ajout d'un Nouveau Membre","Le membre a ete ajouté dans le fichier avec succes")
            # input_name.set("")
            # input_age.set("")
            # input_country.set("")
    else:
        print("Veillez renseigner tous les champs")

btn_add = Button(my_window,text="Ajouter",command=save,bg="black", fg="white").grid(row=4,column=1,padx=15,pady=10)

c = Frame(my_window,width=1000, height=500)

my_window.geometry("600x400")
my_window.mainloop()
