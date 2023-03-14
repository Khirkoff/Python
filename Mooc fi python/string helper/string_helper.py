# Write your solution here
import string

def change_case(orig_string: str):
    mic=string.ascii_lowercase
    mare=string.ascii_uppercase
    for i in range(len(orig_string)):
        if orig_string[i] in mic:
            x=mic.find(orig_string[i])
            orig_string=orig_string[0:i]+mare[x]+orig_string[i+1:len(orig_string)]
        elif orig_string[i] in mare:
            x=mare.find(orig_string[i])
            orig_string=orig_string[0:i]+mic[x]+orig_string[i+1:len(orig_string)]
    return orig_string
def split_in_half(orig_string: str):
    x="";x1="";x2="";x3=""
    if len(orig_string)%2==0:
        for i in range(len(orig_string)//2):
            x=x+orig_string[i]
        for i in range(len(orig_string)//2,len(orig_string)):
            x1=x1+orig_string[i]
        tup=(x,x1)
    elif len(orig_string)%2>0:
        for i in range((len(orig_string)//2)):
            x2=x2+orig_string[i]
        for i in range((len(orig_string)//2),len(orig_string)):
            x3=x3+orig_string[i]
        tup=(x2,x3)
    return tup
def remove_special_characters(orig_string: str):
    Sp1=string.ascii_lowercase
    Sp2=string.ascii_uppercase
    Sp3=string.digits
    Sp4=" "
    for i in orig_string:
        if i not in Sp3 and i not in Sp2 and i not in Sp1 and i not in Sp4:
            orig_string=orig_string.replace(i,"")
    return orig_string

if __name__ == "__main__":
    print(remove_special_characters("This is not how you! do it?"))
    print(split_in_half("Buna cf baby"))
    print(change_case("Trec acasa acuM"))