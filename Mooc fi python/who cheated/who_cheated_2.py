# Write your solution here
from datetime import timedelta

def final_points():
    dex={}
    dex1={}
    dex2={}
    with open("start_times.csv") as file:
        for line in file:
            line=line.replace("\n", "")
            parts=line.split(";")
            parts2=parts[1].split(":")
            startDATE=timedelta(hours=int(parts2[0]),minutes=int(parts2[1]))
            dex[parts[0]]=startDATE
    with open ("submissions.csv") as file:
        for line in file:
            line=line.replace("\n","")
            parts=line.split(";")
            parts2=parts[3].split(":")
            for key,value in dex.items():
                if parts[0]==key:
                    startDATE1=timedelta(hours=int(parts2[0]),minutes=int(parts2[1]))
                    dif=startDATE1-value
                    if (dif/timedelta(seconds=60))<=180:
                        if parts[0] not in dex2:
                            dex1[parts[1]]=parts[2]
                            dex2[parts[0]]=dex1.copy()
                            dex1.clear()
                        elif parts[0] in dex2:
                            if parts[1] in dex2[parts[0]]:
                                if dex2[parts[0]][parts[1]]<parts[2]:
                                    dex2[parts[0]][parts[1]]=parts[2]                       
                            elif parts[1] not in dex2[parts[0]]:
                                dex2[parts[0]][parts[1]]=parts[2]
                                dex1.clear() 
    for i,n in dex2.items():
        suma=0
        for key,value in n.items():
            suma=suma+int(value)
        dex1[i]=suma
    return(dex1)
                                


if __name__ == "__main__":
    final_points()
