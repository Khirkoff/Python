from datetime import datetime

def Game(player1: str, player2: str):
    table=[[" "," "," "],[" "," "," "],[" "," "," "]]
    stats=0
    for row in table:
        print(row)

    # Alegerile pentru a plasa X si O

    while True:
        if stats % 2== 0:
            player_choice=input(f"{player1} unde doresti sa pui X? (ex. stanga sus/centru jos/dreapta mijloc) ")
            if player_choice=="retry": # pentru a reseta jocul
                Game(player1,player2)
            if player_choice == "stanga sus":
                if table[0][0] == " ":
                    table[0][0] = "X"
                    stats += 1
            elif player_choice == "stanga mijloc":
                if table[1][0] == " ":
                    table[1][0] = "X"
                    stats += 1
            elif player_choice == "stanga jos":
                if table[2][0] == " ":
                    table[2][0] = "X"
                    stats += 1
            elif player_choice == "centru sus":
                if table[0][1] == " ":
                    table[0][1] = "X"
                    stats += 1
            elif player_choice == "centru":
                if table[1][1] == " ":
                    table[1][1] = "X"
                    stats += 1
            elif player_choice == "centru jos":
                if table[2][1] == " ":
                    table[2][1] = "X"
                    stats += 1
            elif player_choice == "dreapta sus":
                if table[0][2] == " ":
                    table[0][2] = "X"
                    stats += 1
            elif player_choice == "dreapta mijloc":
                if table[1][2] == " ":
                    table[1][2] = "X"
                    stats += 1
            elif player_choice == "dreapta jos":
                if table[2][2] == " ":
                    table[2][2] = "X"
                    stats += 1
            if stats % 2== 0:
                print("Mai incearca o data!")
                continue
        elif stats % 2== 1:
            player_choice=input(f"{player2} unde doresti sa pui 0? ")
            if player_choice=="retry": # pentru a reseta jocul
                Game(player1,player2)
            if player_choice=="stanga sus":
                if table[0][0] == " ":
                    table[0][0] = "0"
                    stats += 1
            elif player_choice=="stanga mijloc":
                if table[1][0] == " ":
                    table[1][0] = "0"
                    stats += 1
            elif player_choice=="stanga jos":
                if table[2][0] == " ":
                    table[2][0] = "0"
                    stats += 1
            elif player_choice=="centru sus":
                if table[0][1] == " ":
                    table[0][1] = "0"
                    stats += 1
            elif player_choice=="centru":
                if table[1][1] == " ":
                    table[1][1] = "0"
                    stats += 1
            elif player_choice=="centru jos":
                if table[2][1] == " ":
                    table[2][1] = "0"
                    stats += 1
            elif player_choice=="dreapta sus":
                if table[0][2] == " ":
                    table[0][2] = "0"
                    stats += 1
            elif player_choice=="dreapta mijloc":
                if table[1][2] == " ":
                    table[1][2] = "0"
                    stats += 1
            elif player_choice=="dreapta jos":
                if table[2][2]==" ":
                    table[2][2]="0"
                    stats += 1
            if stats % 2 == 1:
                print("Mai incearca o data!")
                continue
        for row in table:
            print(row)

        #     Conditiile de castig

        if (table[0][0]==table[0][1]==table[0][2] and table[0][0] != " ") or (table[1][0]==table[1][1]==table[1][2] and table[1][0] != " " ) or (table[2][0]==table[2][1]==table[2][2] and table[2][0] != " ") or (table[0][0]==table[1][0]==table[2][0] and table[0][0] != " ") or (table[0][1]==table[1][1]==table[2][1] and table[0][1] != " ") or (table[0][2]==table[1][2]==table[2][2] and table[0][2] != " ") or (table[0][0]==table[1][1]==table[2][2] and table[0][0] != " ") or (table[2][0]==table[1][1]==table[0][2] and table[2][0] != " "):
            if stats%2==0:
                print(f"{player2} wins!")
                return player2
            else:
                print(f"{player1} wins!")
                return player1
        draw=0

        # Conditia de egalitate

        for i in range(3):
            for j in range(3):
                if table[i][j]!=" ":
                    draw=1
                elif table[i][j]==" ":
                    draw=0
                    break
        if draw==1:
            print("Its a draw!")
            break
def tinutul_scorului():

    # Tabela de scor intr un fisier separat daca unul dintre playeri a castigat

    if joc!=None:
        with open("scor.txt") as file:
            for line in file:
                line=line.replace("\n","")
                lista.append(line)
        for i in range(len(lista)):
            if joc in lista[i]:
                parts=lista[i].split(":")
                parts[1]=int(parts[1])+1
                lista[i]=parts[0]+" : "+str(parts[1])
                with open("scor.txt","w") as file:
                    for i in lista:
                        file.write(i+"\n")
        count=0
        for i in range(len(lista)):
            if joc not in lista[i]:
                continue
            elif joc in lista[i]:
                count=1
                break
        if count==0:
            with open("scor.txt","a") as file:
                file.write(joc+":1\n")

def istoric():

    # se creeaza un istoric al jocurilor in fisierul istoric_jocuri.txt

    if joc!=0:
        currentTime=datetime.now()
        Time = currentTime.strftime("%d/%m/%Y %H:%M:%S")
        with open("istoric_jocuri.txt","a+") as file:
            if joc==player1:
                file.write(player1+" a castigat impotriva lui "+ player2 + " " +Time+"\n")
            elif joc==player2:
                file.write(player2 + " a castigat impotriva lui " + player1 + " " +Time+"\n")

if __name__=="__main__":
    lista=[]
    player1=input("Primul jucator: ")
    player2=input("Al doilea jucator: ")
    joc=Game(player1,player2)
    tinutul_scorului()
    istoric()