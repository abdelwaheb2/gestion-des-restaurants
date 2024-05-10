
from datetime import datetime
from random import randint, random


def mot(ch):
    if len(ch)>3 and ch!='':
        return True
    return False

def mot_passe (ch):
    if ch=='' or ch.isalpha() or ch.isnumeric() or len(ch)<6 :
        return False
    return True

def dat(ch):
    if ch=='':
        return False
    else:
        x=datetime.now()
        if (int(x.year)-int(ch[:4])<10):
            return False
        return True

def tele(ch):
    if ch.isnumeric() and len(ch)==8 and ch!='':
        return True
    return False

def generateur():
    ch="resto|"
    for i in range(5):
        ch+=chr(randint(1,25)+ord('A'))
    return ch


    


    







