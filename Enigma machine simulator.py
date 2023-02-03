import random
from tkinter import *
from tkinter import ttk
import time

alphabet = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'
r1=''
r2=''
r3=''
def choiceRotor():
    global r1,r2,r3
    cr1=choiceRotornum1.get()
    cr2=choiceRotornum2.get()
    cr3=choiceRotornum3.get()
    if cr1=='rotorA1':
        r1='sVwuqGkCh NpJrPlMABTajtLHgnWEIXxYQimSOcZvboeKfzdDyFUR'
    elif cr1=='rotorA2':
        r1='fvzlFmInXMpKTNkari qSsHAjgecOLCJdWbxBhZGtuQyPEYVDUowR'
    else:
        r1='bJakxYXgzMGZIesuLp rWUtVHoAKfliNjvdyTDwShEOCcmQqnRPBF'

    if cr2=='rotorB1':
        r2='sutNljAydExRqMez bITQYXGHUBgikaDVKvrchOpJPowLWZmnfCFS'
    elif cr2=='rotorB2':
        r2='AxriewdEFsWmDZyfoqgMIUbOTKRGBpYCPQza HvSultVJXjhnLkNc'
    else:
        r2='QfvSOIBMJmKcVyPXwzGljRrHaUueLobYAx giECnkDTspFtZqdhNW'

    if cr3=='rotorC1':
        r3='udiwURpMOkJBzxVAXmblSPsaQNYWErHFLZyKGcTegDCnqtjohI fv'
    elif cr3=='rotorC2':
        r3='TAjoIwzsZkYUlKbQWNRfHCyhXVaqmiJ xugPEOpMtSDnreGcBFdvL'
    else:
        r3='hKRkDETnpJorCVuePwdaNgt SFIivWYjXszZLAUqQlfbmcOMByGHx'
    ciphertext.config(text="rotors are set".format(cipher), fg='#FF00FF')
def reflector(c):
    return alphabet[len(alphabet)-alphabet.find(c)-1]
    
def enigma_one_char(c):
    global r1,r2,r3
    c1= r1[alphabet.find(c)]
    c2= r2[alphabet.find(c1)]
    c3= r3[alphabet.find(c2)]
    reflected=reflector(c3)
    c3=alphabet[r3.find(reflected)]
    c2=alphabet[r2.find(c3)]
    c1=alphabet[r1.find(c2)]
    return c1

def rotate_rotors():
    global r1,r2,r3
    r1=r1[1:]+r1[0]
    if state%26:
        r2=r2[1:]+r2[0]
    if state%26**2:
        r3=r3[1:]+r3[0]





cipher =''
state=0



def generation_ciphertext():
    global plaintext , cipher, state, alphabet
    px=plaintext.get()
    print(sorted(px))
    print(sorted(alphabet))
    t=True

    for w in px:
        for e in alphabet:
            if w==e:
                t=True
                break
            else:
                t=False
    if t:
        for c in px:
            state+=1
            cipher += enigma_one_char(c)
            rotate_rotors()
        ciphertext.config(text="ciphertext : {} ".format(cipher), fg='green')
        plaintext.delete(0,'end')
        cipher =''
        state=0
    else:
        ciphertext.config(text="Plaintext should be in alphabet ".format(cipher), fg='red')
                



Window = Tk()
Window.title('Enigma machine simulator')
Label(Window, text='Enigma machine simulator', font=('', 20), foreground='blue').pack()
Window.geometry("500x650")
Window.minsize(500, 650)
Window.maxsize(1080, 1080)
Label(Window, text="PLAIN TEXT",font=('Times', 10)).pack()
menubar = Menu(Window)
helpmenu = Menu(menubar)
helpmenu.add_command(label="First select the rotors")
helpmenu.add_command(label="Then press the set rotors button")
helpmenu.add_command(label="Then enter the word you want to encrypt or decrypt")
helpmenu.add_command(label="Finally, press the enter button")
menubar.add_cascade(label="Help", menu=helpmenu)
Window .config(menu=menubar)

plaintext = Entry(Window)
plaintext.pack(pady=10)

rotor_num1 = [ 'rotorA1','rotorA2','rotorA3']
choiceRotornum1 = ttk.Combobox(Window, values = rotor_num1,font=("Times", 12))
choiceRotornum1.set("Pick RotorA")
choiceRotornum1.pack(padx = 5, pady = 5)

rotor_num2 = [ 'rotorB1', 'rotorB2', 'rotorB3']
choiceRotornum2 = ttk.Combobox(Window, values = rotor_num2,font=("Times", 12))
choiceRotornum2.set("Pick RotorB")
choiceRotornum2.pack(padx = 5, pady = 5)

rotor_num3 = [ 'rotorC1', 'rotorC2','rotorC3']
choiceRotornum3 = ttk.Combobox(Window, values = rotor_num3,font=("Times", 12))
choiceRotornum3.set("Pick RotorC")
choiceRotornum3.pack(padx = 5, pady = 5)

ciphertext = Label(Window, text='CIPHER: ---  ',font=("Times", 12))
ciphertext.pack(pady=10)
Button(Window, text='set rotors', font=("Times", 12),bg='yellow',fg='black', command=choiceRotor).pack(pady=10)
Button(Window, text='Convert', font=("Times", 12), command=generation_ciphertext).pack(pady=10)
Window.mainloop()
