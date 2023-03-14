# Write your solution here
import difflib

phrase= input("write text: ")
dex=[];lista=[];dex1={};contor=0
with open ("wordlist.txt") as file:
    parts=phrase.split(" ")
    for line in file:
        line=line.replace("\n",'')
        for i in range(len(parts)):
            if parts[i].lower()==line:
                dex.append(parts[i])
    for item in parts:
        if item not in dex:
            phrase=phrase.replace(item,"*"+item+"*")
            contor+=1
            lista.append(item)
print(phrase)
print("suggetions:")
for i in range(contor):
    with open("wordlist.txt") as file:
        x=difflib.get_close_matches(lista[i], file)
        x=list(map(lambda y: y.replace('\n', '' ) ,x))
        y=', '.join(x)
        print(lista[i]+": "+y)
        del x


    