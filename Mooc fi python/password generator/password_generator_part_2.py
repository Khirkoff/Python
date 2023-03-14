# Write your solution here
import string
import random

def generate_strong_password(num: int,cuv1: bool, cuv2: bool):
    alphabet = list(string.ascii_lowercase)
    numb=list(string.digits)
    char= list('!?=+-()#')
    passw=""
    if cuv1==True and cuv2==True:
        x=random.randint(1,int(num/2))
        for i in range(x):
            passw=passw+ random.choice(alphabet)
        y=random.randint(1,num-x-1)
        for i in range(y):
            passw=passw+random.choice(numb)
        for i in range(num-x-y):
            passw=passw+random.choice(char)
        l=list(passw)
        random.shuffle(l)
        result=''.join(l)
        return result
     
    if cuv1==False and cuv2==False:
        for i in range(num):
            passw=passw+ random.choice(alphabet)
        return passw

    if cuv1==True and cuv2==False:
        x=random.randint(1,num-1)
        for i in range(x):
             passw=passw+ random.choice(alphabet)
        for i in range(num-x):
            passw=passw+random.choice(numb)
        l=list(passw)
        random.shuffle(l)
        result=''.join(l)
        return result

    if cuv1==False and cuv2==True:
        x=random.randint(1,num-1)
        for i in range(x):
             passw=passw+ random.choice(alphabet)
        for i in range(num-x):
            passw=passw+random.choice(char)
        l=list(passw)
        random.shuffle(l)
        result=''.join(l)
        return result

                        

if __name__ == "__main__":
    print(generate_strong_password(8, True, True))