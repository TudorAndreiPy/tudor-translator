import time # import time for time.sleep()
from tkinter import *  #import tkinter
from tkinter import messagebox #import tkinter with messagebox
from googletrans import Translator

trans = Translator()

root = Tk()
root.title("Tudor Translator")
root.iconbitmap('C:/Users/eu/Desktop/tudor translator/language.ico')
root.geometry("+70+80")
bg = '#fff'
root.configure(bg = bg)

title = Label(root, text = "The Tudor Translator", font = ("Century 24") , bg = bg)
title.grid(row = 0 ,columnspan = 9, column = 0 , pady = 15)

options1 = ["English","Romanian", "French", "Spanish", "Hungarian" , "German" ] 
click1 = StringVar()                                   
click1.set(options1[1])                                
drop1 = OptionMenu(root, click1, *options1 )           
drop1.configure(font = ("Century 16"))                 
drop1.grid(row = 1 , column = 0, sticky = W)           

entrytext1 = Text(root, width = 60 , height = 15 , borderwidth = 3 , font = ("Century 13 bold"))
entrytext1.grid(row = 2 , column = 0)

##########################################################

options2 = ["English","Romanian", "French", "Spanish", "Hungarian" , "German"]
click2 = StringVar()
click2.set(options1[1])
drop2 = OptionMenu(root, click2, *options2 )
drop2.configure(font = ("Century 16"))
drop2.grid(row = 1 , column = 1, sticky = W)

entrytext2 = Text(root, width = 60 , height = 15 , borderwidth = 3 , font = ("Century 13 bold"))
entrytext2.grid(row = 2 , column = 1)

def translate():
    limbanr1 = click1.get()
    limbanr2 = click2.get()
    text1 = entrytext1.get(1.0 , END)

    ### CU ACELEASI ###

    if limbanr1 == "Romanian" and limbanr2 == "Romanian":
        t = trans.translate(
            text1 , src='ro' , dest = 'ro'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "English" and limbanr2 == "English":
        t = trans.translate(
            text1 , src='en' , dest = 'en'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        ###################

    elif limbanr1 == "French" and limbanr2 == "French":
        t = trans.translate(
            text1 , src='fr' , dest = 'fr'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #####################

    elif limbanr1 == "Spanish" and limbanr2 == "Spanish":
        t = trans.translate(
            text1 , src='es' , dest = 'es'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #######################

    elif limbanr1 == "German" and limbanr2 == "German":
        t = trans.translate(
            text1 , src='de' , dest = 'de'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #######################

    elif limbanr1 == "Hungarian" and limbanr2 == "Hungarian":
        t = trans.translate(
            text1 , src='hu' , dest = 'hu'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        ### // CU ACELEASI \\ ###

        ### RO CU TOATE ### 

    elif limbanr1 == "Romanian" and limbanr2 == "English":
        t = trans.translate(
            text1 , src='ro' , dest = 'en'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        ##########

    elif limbanr1 == "Romanian" and limbanr2 == "Spanish":
        t = trans.translate(
            text1 , src='ro' , dest = 'es'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "Romanian" and limbanr2 == "French":
        t = trans.translate(
            text1 , src='ro' , dest = 'fr'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        ##################

    elif limbanr1 == "Romanian" and limbanr2 == "Hungarian":
        t = trans.translate(
            text1 , src='ro' , dest = 'hu'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################33

    elif limbanr1 == "Romanian" and limbanr2 == "German":
        t = trans.translate(
            text1 , src='ro' , dest = 'de'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

    ### // TOATE CU RO \\ ###

    #toate cu engl


    elif limbanr1 == "English" and limbanr2 == "Romanian":
        t = trans.translate(
            text1 , src='en' , dest = 'ro'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "English" and limbanr2 == "French":
        t = trans.translate(
            text1 , src='en' , dest = 'fr'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################


    elif limbanr1 == "English" and limbanr2 == "Spanish":
        t = trans.translate(
            text1 , src='en' , dest = 'es'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "English" and limbanr2 == "German":
        t = trans.translate(
            text1 , src='en' , dest = 'de'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "English" and limbanr2 == "Hungarian":
        t = trans.translate(
            text1 , src='en' , dest = 'hu'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

        ### /// Toate cu Engls \\\ ###

        ### toate cu fr

    elif limbanr1 == "French" and limbanr2 == "Romanian":
        t = trans.translate(
            text1 , src='fr' , dest = 'ro'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "French" and limbanr2 == "English":
        t = trans.translate(
            text1 , src='fr' , dest = 'en'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "French" and limbanr2 == "Spanish":
        t = trans.translate(
            text1 , src='fr' , dest = 'es'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "French" and limbanr2 == "German":
        t = trans.translate(
            text1 , src='fr' , dest = 'de'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "French" and limbanr2 == "Hungarian":
        t = trans.translate(
            text1 , src='fr' , dest = 'hu'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    ### // french \\ ###

    ### germana ###

    elif limbanr1 == "German" and limbanr2 == "Romanian":
        t = trans.translate(
            text1 , src='de' , dest = 'ro'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "German" and limbanr2 == "English":
        t = trans.translate(
            text1 , src='de' , dest = 'en'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "German" and limbanr2 == "Spanish":
        t = trans.translate(
            text1 , src='de' , dest = 'es'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "German" and limbanr2 == "French":
        t = trans.translate(
            text1 , src='de' , dest = 'fr'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "German" and limbanr2 == "Hungarian":
        t = trans.translate(
            text1 , src='de' , dest = 'hu'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

        ### // germana \\ ###

        ### spaniola ###

    elif limbanr1 == "Spanish" and limbanr2 == "Romanian":
        t = trans.translate(
            text1 , src='es' , dest = 'ro'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "Spanish" and limbanr2 == "English":
        t = trans.translate(
            text1 , src='es' , dest = 'en'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "Spanish" and limbanr2 == "French":
        t = trans.translate(
            text1 , src='es' , dest = 'fr'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "Spanish" and limbanr2 == "German":
        t = trans.translate(
            text1 , src='es' , dest = 'de'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "Spanish" and limbanr2 == "Hungarian":
        t = trans.translate(
            text1 , src='es' , dest = 'hu'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

        ###// span \\\

        #hungarian

    elif limbanr1 == "Hungarian" and limbanr2 == "Romanian":
        t = trans.translate(
            text1 , src='hu' , dest = 'ro'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "Hungarian" and limbanr2 == "English":
        t = trans.translate(
            text1 , src='hu' , dest = 'en'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "Hungarian" and limbanr2 == "French":
        t = trans.translate(
            text1 , src='hu' , dest = 'fr'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "Hungarian" and limbanr2 == "Spanish":
        t = trans.translate(
            text1 , src='hu' , dest = 'es'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################

    elif limbanr1 == "Hungarian" and limbanr2 == "German":
        t = trans.translate(
            text1 , src='hu' , dest = 'de'
        )
        textnou = t.text

        entrytext2.delete(1.0, END)
        entrytext2.insert(1.0 , textnou)

        #################


translatebut = Button(root, text = "Translate" , font = "Century 18" , bg =bg , command = translate)
translatebut.grid(row = 3 , columnspan = 2 , column = 0 , pady = 10)

root.mainloop()