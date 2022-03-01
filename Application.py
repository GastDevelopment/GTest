from random import randint
import sys

def checkMarks(m):
    if m > 100 or m < 20:
        print("Too little or too many marks! Enter from 1-100!\nSystem shutting down...")
        sys.exit()
    else:
        pass

def checkPupils(p):
    if p > 60 or p < 20:
        print("Too little or too many pupils! Enter from 1-60!\nSystem shutting down...")
        sys.exit()
    else:
        pass

def checkDifficulty(d):
    if d == "EASY" or d == "MEDIUM" or d == "HARD":
        pass
    else:
        print("Unkown difficulty, enter either EASY, MEDIUM or HARD\nSystem shutting down...")
        sys.exit()

global results
results = []
def testRandomizer(r, m, p):
    global results
    if r == "EASY":
        for i in range(p):
            if m in range(20, 41):
                e1 = max(randint(5, m), randint(5, (m + 1)))
                results.append(e1)
            elif m in range(41, 61):
                e2 = max(randint(20, m), randint(20, (m + 1)))
                results.append(e2)
            elif m in range(60, 100):
                e3 = max(randint(28, m), randint(28, (m + 1)))
                results.append(e3)
    elif r == "MEDIUM":
        for i in range(p):
            if m in range(20, 41):
                s1 = max(randint(3, m), randint(3, (m + 1)))
                results.append(s1)
            elif m in range(41, 61):
                s2 = max(randint(16, m), randint(16, (m + 1)))
                results.append(s2)
            elif m in range(60, 100):
                s3 = max(randint(23, m), randint(23, (m + 1)))
                results.append(s3)
    elif r == "HARD":
        for i in range(p):
            if m in range(20, 41):
                f1 = min(randint(1, m), randint(1, (m + 1)))
                results.append(f1)
            elif m in range(41, 61):
                f2 = min(randint(9, m), randint(9, (m + 1)))
                results.append(f2)
            elif m in range(60, 100):
                f3 = min(randint(15, m), randint(15, (m + 1)))
                results.append(f3)
    else:
        pass
                
print("--------------------------------")
marks = int(input("Enter the amount of marks the test will have min(20) max(100): "))
checkMarks(marks)
pupils = int(input("Enter the amount of pupils attending the test min(20) max(60): "))
checkPupils(pupils)
difficulty = input("Should the difficulty be EASY, MEDIUM, HARD: ")
checkDifficulty(difficulty)

testRandomizer(difficulty, marks, pupils)
