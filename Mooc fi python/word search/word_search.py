# Write your solution here

def find_words(search_term: str):
    lista=[]
    with open("words.txt") as words:
        if "." in search_term:
            for line in words:
                line=line.replace("\n","")
                index1=0
                term=search_term
                term1=line
                if len(search_term)==len(line):
                    count=search_term.count(".")
                    for i in range(count):
                        index=search_term.find(".")
                        index1=index1+index
                        line=line[:index1]+"."+line[index1+1:]
                        index1=index1+1
                        search_term=search_term[index+1:]
                    if line==term:
                        lista.append(term1)
                search_term=term
        elif "*" in search_term:
            if "*"==search_term[0]:
                for line in words:
                    line=line.replace("\n","")
                    term=search_term
                    search_term=search_term[1:]
                    if line.endswith(search_term):
                        lista.append(line)
                    search_term=term
            elif "*" ==search_term[len(search_term)-1]:
                for line in words:
                    line=line.replace("\n","")
                    term=search_term
                    search_term=search_term[:len(search_term)-1]
                    if line.startswith(search_term):
                        lista.append(line)
                    search_term=term
        else:
            for line in words:
                line=line.replace("\n","")
                if line==search_term:
                    lista.append(line)
        return lista



if __name__ == "__main__":
    print(find_words("reson*"))