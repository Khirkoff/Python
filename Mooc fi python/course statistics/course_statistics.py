import urllib.request
import json

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    my_request1=my_request.read()
    date=json.loads(my_request1)
    lista=[]
    for data in date:
        if data["enabled"] is True:
            points=sum(data["exercises"])
            fullName=data["fullName"]
            name=data["name"]
            year=data["year"]
            tup=(fullName,name,year,points)
            lista.append(tup)
    return lista

def retrieve_course(course_name: str):
    my_request=urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses/"+str(course_name)+"/stats")
    my_request1=my_request.read()
    date=json.loads(my_request1)
    weeks=0;studMax=0;hours=0;exercises=0
    for data in date:
        if int(date[data]["students"])> studMax :
            studMax=int(date[data]["students"])
        hours+=date[data]["hour_total"]
        exercises+=date[data]["exercise_total"]
        weeks+=1
    hoursAvg=hours//studMax
    exercisesAvg=exercises//studMax
    dex={}
    dex["weeks"]=weeks
    dex["students"]=studMax
    dex["hours"]=hours
    dex["hours_average"]=hoursAvg
    dex["exercises"]=exercises
    dex["exercises_average"]=exercisesAvg
    return dex


if __name__ == "__main__":
    #print(retrieve_all())
    print(retrieve_course("CCFUN"))