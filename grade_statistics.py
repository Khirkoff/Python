# Write your solution here
def userInput():
    examPoints = []
    exercisesCompleted = []
    while True:
        word = input('Exam points and exercises completed: ')
        if word == '':
            break
        i = word.find(' ')
        examPoints.append(int(word[0:i]))
        exercisesCompleted.append(int(word[i+1:len(word)]))
    return examPoints , exercisesCompleted

def points(exam,exercises):
    totalPoints = []
    exercises_points_lists = []
    for item in exercises:
        exercises_points_lists.append(item//10)
    for i in range(len(exam)):
        totalPoints.append(exam[i]+exercises_points_lists[i])
    grades = [0 for i in range(6)]
    for i in range(len(totalPoints)):
        if exam[i] < 10:
            grades[0] = grades[0] + 1
        else:
            if 0 <= totalPoints[i] <= 14:
                grades[0] += 1
            elif 15 <= totalPoints[i] <= 17:
                grades[1] += 1
            elif 18 <= totalPoints[i] <= 20:
                grades[2] += 1
            elif 21 <= totalPoints[i] <= 23:
                grades[3] += 1
            elif 24 <= totalPoints[i] <= 27:
                grades[4] += 1
            elif 28 <= totalPoints[i] <= 30:
                grades[5] += 1
            
    return grades, totalPoints
 

def statistics(a,b):
    average = 0
    percentage = 0
    passed = 0
    for item in b:
        average += item
    average ="%.1f" %  (average / len(b))

    for item in a[1:]:
        passed += item
    total = passed + a[0]

    percentage = "%.1f" %  ((passed / total)*100)
    return average, percentage


    


def main():
    user = list(userInput())
    userExam = user[0]
    userExercises = user[1]
    output = points(userExam,userExercises)
    outputGrades = output[0]
    outputTotalPoints = output[1]
    statistic = statistics(outputGrades, outputTotalPoints)
    statistics1 = statistic[0]
    statistics2 = statistic[1]
    print('Statistics:')
    print(f'Points average: {statistics1}')
    print(f'Pass percentage: {statistics2}')
    print(f'Grade distribution:')
    print(f"5: {'*' * outputGrades[5]}")
    print(f"4: {'*' * outputGrades[4]}")
    print(f"3: {'*' * outputGrades[3]}")
    print(f"2: {'*' * outputGrades[2]}")
    print(f"1: {'*' * outputGrades[1]}")
    print(f"0: {'*' * outputGrades[0]}")

main()
