# Write your solution here


def add_student(database, name):
    database[name]=[]


def add_course(database: dict, name:str , grade: tuple ):
    if grade[1]>0:
        database[name].append(grade)
    count=0
    for i in range(len(database[name])-1):
        if grade[0] in database[name][i]:
            count+=1
        if count==1:
            if grade[1]<database[name][i][1]:
                database[name].remove(grade)
                break
            elif grade[1]>database[name][i][1]:
                database[name][i]=grade
                database[name].remove(grade)
                break
            elif grade[1]==database[name][i][1]:
                database[name].remove(grade)
                break

def summary(database: dict):
    stud=len(database)
    print(f"students {stud}")
    max=0
    num=0
    nume=""
    for key ,value in database.items():
        if (len(database[key])>max):
            max=len(database[key])
            nume = str(key)
    print(f"most courses completed {max} {nume}")
    nume=" "
    for key,value in database.items():
        avg=0
        suma=0
        num1=0
        for i in range(len(database[key])):
            suma+=database[key][i][1]
            num1+=1
        avg=float(suma/num1)
        if avg>num:
            num=avg
            nume=key
        else:
            avg=num
            
    print(f"best average grade {avg} {nume}")




def print_student(database,name):
    suma=0
    num=0
    if name in database:
        print(name+":")
        if len(database[name])==0:
            print(" no completed courses")
        else:
            print(f" {len(database[name])} completed courses:")
            for i in range(len(database[name])):
                print(f"  {database[name][i][0]} {database[name][i][1]}")
            for i in range(len(database[name])):
                suma+=database[name][i][1]
                num+=1
            if num>0:
                print(f" average grade {float(suma/num)}")
    elif name not in database:
        print(f"{name}: no such person in the database")


if __name__ == "__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)