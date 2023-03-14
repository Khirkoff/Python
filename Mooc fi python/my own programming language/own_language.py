# Write your solution here

def run(commands):
    ls = []
    usedCommands = ["IF", 'ADD', 'MOV', 'PRINT', 'SUB','MUL','JUMP','END']
    dic = {}
    for i in range(len(commands)):
        parts = commands[i].split(' ')
        if len(parts) < 2:
            if ":" in commands[i]:
                dic[commands[i][:len(commands[i])-1]] = i
            else:
                dic[commands[i][:len(commands[i])]] = i
    i = 0
    while i < len(commands):
        if 'MOV' in commands[i]:
            parts = commands[i].split(' ')
            if parts[2] not in dic:
                dic[parts[1]] = parts[2]
            else:
                dic[parts[1]] = dic[parts[2]]
        if "PRINT" in commands[i]:
            parts = commands[i].split(' ')
            if parts[1].isnumeric():
                ls.append(int(parts[1]))
            else:
                if parts[1] in dic:
                    ls.append(int(dic[parts[1]]))
                else:
                    ls.append(0)
        if 'ADD' in commands[i]:
            parts = commands[i].split(' ')
            if parts[1] in dic:
                num1 = int(dic[parts[1]])
            else:
                dic[parts[1]] = 0
                num1 = 0
            if parts[2].isnumeric():
                num1 += int(parts[2])
                dic[parts[1]] = num1

            else:
                num1 += int(dic[parts[2]])
                dic[parts[1]] = num1

        if 'SUB' in commands[i]:
            parts = commands[i].split(' ')
            if parts[1] in dic:
                num1 = int(dic[parts[1]])
            else:
                dic[parts[1]] = 0
                num1 = 0
            if parts[2].isnumeric():
                num1 -= int(parts[2])
                dic[parts[1]] = num1

            else:
                num1 -= int(dic[parts[2]])
                dic[parts[1]] = num1

        if 'MUL' in commands[i]:
            parts = commands[i].split(' ')
            num1 = int(dic[parts[1]])
            if parts[2].isnumeric():
                num1 = num1 * int(parts[2])
                dic[parts[1]] = num1

            else:
                num1 = num1 * int(dic[parts[2]])
                dic[parts[1]] = num1

        if 'END' in commands[i]:
            break
        if 'JUMP' in commands[i]:
            parts = commands[i].split(' ')
            if len(parts) == 2:
                i = dic[parts[1]]

        if 'IF' in commands[i]:
            parts = commands[i].split(' ')
            if parts[3] not in dic:
                if parts[2] == "==":
                    if int(dic[parts[1]]) == int(parts[3]):
                        i = dic[parts[5]]
                if parts[2] == "!=":
                    if int(dic[parts[1]]) != int(parts[3]):
                        i = dic[parts[5]]
                if parts[2] == "<":
                    if int(dic[parts[1]]) < int(parts[3]):
                        i = dic[parts[5]]
                if parts[2] == "<=":
                    if int(dic[parts[1]]) <= int(parts[3]):
                        i = dic[parts[5]]
                if parts[2] == ">":
                    if int(dic[parts[1]]) > int(parts[3]):
                        i = dic[parts[5]]
                if parts[2] == ">=":
                    if int(dic[parts[1]]) >= int(parts[3]):
                        i = dic[parts[5]]
            else:
                if parts[2] == "==":
                    if int(dic[parts[1]]) == int(dic[parts[3]]):
                        i = dic[parts[5]]
                if parts[2] == "!=":
                    if int(dic[parts[1]]) != int(dic[parts[3]]):
                        i = dic[parts[5]]
                if parts[2] == "<":
                    if int(dic[parts[1]]) < int(dic[parts[3]]):
                        i = dic[parts[5]]
                if parts[2] == "<=":
                    if int(dic[parts[1]]) <= int(dic[parts[3]]):
                        i = dic[parts[5]]
                if parts[2] == ">":
                    if int(dic[parts[1]]) > int(dic[parts[3]]):
                        i = dic[parts[5]]
                if parts[2] == ">=":
                    if int(dic[parts[1]]) >= int(dic[parts[3]]):
                        i = dic[parts[5]]
                    

        else:
            if ":" in commands[i]:
                dic[commands[i][:len(commands[i])-1]] = i
            else:
                dic[commands[i][:len(commands[i])]] = i
        i+=1
    return ls

if __name__ == "__main__":
    program3 = []
    program3.append("MOV N 100")
    program3.append("PRINT 2")
    program3.append("MOV A 3")
    program3.append("start:")
    program3.append("MOV B 2")
    program3.append("MOV Z 0")
    program3.append("test:")
    program3.append("MOVE C B")
    program3.append("new:")
    program3.append("IF C == A JUMP virhe")
    program3.append("IF C > A JUMP pass_by")
    program3.append("ADD C B")
    program3.append("JUMP new")
    program3.append("virhe:")
    program3.append("MOVE Z 1")
    program3.append("JUMP pass_by2")
    program3.append("pass_by:")
    program3.append("ADD B 1")
    program3.append("IF B < A JUMP test")
    program3.append("pass_by2:")
    program3.append("IF Z == 1 JUMP pass_by3")
    program3.append("PRINT A")
    program3.append("pass_by3:")
    program3.append("ADD A 1")
    program3.append("IF A <= N JUMP start")
    result = run(program3)
    print(result)