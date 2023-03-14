# Write your solution here
def search_by_name(filename: str, word: str):
    lista=[]
    count=0
    n=""
    with open (filename) as file:
        for line in file:
            line=line.replace("\n","")
            if count==0:
                if word in line.lower():
                    lista.append(line)
                    count+=1
            if len(line)==0:
                count=0
    return(lista)

def search_by_time(filename: str, prep_time: int):
    dex={}
    lista=[]
    count=0
    with open (filename) as file:
        for line in file:
            line=line.replace("\n",'')
            if count==1:
                count+=1
                if prep_time>=int(line):
                    dex[n]=line
            if count==0:
                n=line
                count+=1
            if len(line)==0:
                count=0
    for key,value in dex.items():
        nume=key+", preparation time "+value+" min"
        lista.append(nume)
    return lista
                
def search_by_ingredient(filename: str, ingredient: str):
    dex={}
    lista=[]
    count=0
    count2=0
    with open (filename) as file:
        for line in file:
            line=line.replace("\n",'')
            if count==1:
                count+=1
                dex[n]=line
            if count==0:
                n=line
                count+=1
            if ingredient in line:
                count2+=1
            if len(line)==0:
                if count2==0:
                    del dex[n]
                count2=0
                count=0
    for key,value in dex.items():
        nume=key+", preparation time "+value+" min"
        lista.append(nume)
    return lista      


if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")
    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_time("recipes2.txt", 20)
    for recipe in found_recipes:
        print(recipe)
    
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    for recipe in found_recipes:
        print(recipe)