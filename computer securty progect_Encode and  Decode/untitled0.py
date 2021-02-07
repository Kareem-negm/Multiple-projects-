# Import Libraries
from tkinter import *
import base64

#make windos with tkinter
windio=Tk()
windio.geometry('500x300')
windio.resizable(0,0)
windio.title("Message Encode and Decode app")


Label(windio, text ='Everst Team Encode and Decode app', font = 'arial 10 bold').pack()

#define varianles wa will used
Text = StringVar() #to store the message to encode and decode
key = StringVar()#to store the key that we will uses to encode and decode 
mode = StringVar()#to determine whether what we're doing is encryption or decryption 
Result = StringVar()#to store the result


#make function to encod the txte

def Encode(key,message):
    enc=[]

    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


#make function to dencod the txte

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
    return "".join(dec)


#used Mode 
def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')
        
# exit window        
def Exit():
    windio.destroy()

#reset window
def Reset():
    Text.set("")
    key.set("")
    mode.set("")
    Result.set("")


Label(windio, font= 'arial 12 bold', text='MESSAGE').place(x= 60,y=60)
Entry(windio, font = 'arial 10', textvariable = Text, bg = 'ghost white').place(x=290, y = 60)

Label(windio, font = 'arial 12 bold', text ='KEY').place(x=60, y = 90)
Entry(windio, font = 'arial 10', textvariable = key , bg ='ghost white').place(x=290, y = 90)

Label(windio, font = 'arial 12 bold', text ='MODE(e-encode, d-decode)').place(x=60, y = 120)
Entry(windio, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)
Entry(windio, font = 'arial 10 bold', textvariable = Result, bg ='ghost white').place(x=290, y = 150)

Button(windio, font = 'arial 10 bold', text = 'RESULT'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=60, y = 150)

Button(windio, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=80, y = 190)

Button(windio, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=180, y = 190)

windio.mainloop()

