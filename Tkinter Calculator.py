#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import * #Importing libraries

#Function helping in getting desired result
def calculate():
    sentence = entry_1.get() #Input 
    d = dict() #Dictonary d
    for a, b in (elements.split(" ") for elements in sentence.split(", ")): #Loop for spliting the values
        if a in d.keys():
            d[a.strip()] =  int(d[a]) + int(b.strip()) #Adding duplicate values
        else:
            d[a.strip()] = int(b.strip())

    
    label_2 = Label(my_window)
    label_2["text"] = d
    label_2.grid(row=1,column=1)

    
my_window=Tk()
#headlabel=Label(root,text="Let's See How Much Have You Saved Today? :D" , fg="White" , bg="Black")
label_1 = Label(my_window, text="Please enter the items to be calculated: "  , fg="Black" , bg="LavenderBlush2") #Creating label for the entry frield
entry_1 = Entry(my_window) 
button_1 = Button(my_window, text="Result", bg="orchid1" ,fg="black", command = calculate) 

#headlabel.grid(row=0,column=1)
label_1.grid(row=0,column=0) #Arranging label
entry_1.grid(row=0,column=1)
button_1.grid(row=1,column=0)

my_window.configure(background= 'LavenderBlush2')
my_window.title('Customised Calculator') #Title of the calculator
my_window.geometry("400x200") #Dimension of the calculator

my_window.mainloop()

