from random import randint
from numpy import sort
from scipy import stats
import sys

def checkMarks(m):
    if m > 100 or m < 20:
        print("Too little or too many marks! Enter from 1-100!\nSystem shutting down...")
        sys.exit()
    else:
        pass

def checkPupils(p):
    if p > 60 or p < 5:
        print("Too little or too many pupils! Enter from 1-60!\nSystem shutting down...")
        sys.exit()
    else:
        pass

def checkDifficulty(d):
    if d == "EASY" or d == "MEDIUM" or d == "HARD" or d == "easy" or d == "medium" or d == "hard" :
        pass
    else:
        print("Unkown difficulty, enter either EASY, MEDIUM or HARD\nSystem shutting down...")
        sys.exit()

global results
results = []
def testRandomizer(r, m, p):
    global results
    if r == "EASY" or r == "easy":
        for i in range(p):
            if m in range(20, 41):
                e1 = max(randint(5, m), randint(5, m))
                results.append(e1)
            elif m in range(41, 61):
                e2 = max(randint(20, m), randint(20, m))
                results.append(e2)
            elif m in range(60, 100):
                e3 = max(randint(28, m), randint(28, m))
                results.append(e3)
    elif r == "MEDIUM" or r == "medium":
        for i in range(p):
            if m in range(20, 41):
                s1 = max(randint(3, m), randint(3, m))
                results.append(s1)
            elif m in range(41, 61):
                s2 = max(randint(16, m), randint(16, m))
                results.append(s2)
            elif m in range(60, 100):
                s3 = max(randint(23, m), randint(23, m))
                results.append(s3)
    elif r == "HARD" or r == "hard":
        for i in range(p):
            if m in range(20, 41):
                f1 = min(randint(1, m), randint(1, m))
                results.append(f1)
            elif m in range(41, 61):
                f2 = min(randint(9, m), randint(9, m))
                results.append(f2)
            elif m in range(60, 100):
                f3 = min(randint(15, m), randint(15, m))
                results.append(f3)
    else:
        pass

def analyse(array, marks):
    length = len(array)
    sum = 0
    total = 0
    totalSum = length * marks
    average = 0
    ma = 0
    mi = 0
    common = stats.mode(array)
    sortedArray = sort(array)
    for i in range(0, length):
        sum = sum + array[i]
        average = sum / length
        total = total + array[i]
        ma = sortedArray[-1]
        mi = sortedArray[0]


    print("Total sum of test ---> " + str(total) + "/" + str(totalSum))
    print("Average ---> " + str(average))
    print("Highest score ---> " + str(ma))
    print("Lowest score ---> " + str(mi))
    print("Most common score ---> " + str(common[0]))
    print("Sorted scores with percentages: ")
    for i in range(0, length):
        percentage = (sortedArray[i] / marks) * 100
        print("Score: " + str(sortedArray[i]) + "/" + str(marks) + " Percentage: " + str(percentage) + "%")
    
print("--------------------------------")
marks = int(input("Enter the amount of marks the test will have min(20) max(100): "))
checkMarks(marks)
pupils = int(input("Enter the amount of pupils attending the test min(5) max(60): "))
checkPupils(pupils)
difficulty = input("Should the difficulty be EASY, MEDIUM, HARD: ")
checkDifficulty(difficulty)

testRandomizer(difficulty, marks, pupils)
print("---------------------------")
print("Test Result Analysis:")
analyse(results, marks)
