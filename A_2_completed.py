n = int(input("Enter Number of Students : "))

marks = []
print("Enter -1 for Absent Students\n")
for i in range(n):
    mk = int(input("Enter Marks of student "+str(i+1)+" : "))
    marks.append(mk)


# Average Marks Function

def avg(marks):
    sum = 0
    cnt = 0

    for i in range(len(marks)):
        if marks[i] != -1:
            sum += marks[i]
            cnt += 1

    avg = sum/cnt
    return avg

# Higest and Lowest Marks Function


def maxmin(marks):
    high = 0
    low = marks[0]

    for i in range(len(marks)):
        if high < marks[i]:
            high = marks[i]

    for i in range(len(marks)):
        if marks[i] != -1:
            if low > marks[i]:
                low = marks[i]
    return high, low

# Absent Students function


def absent(marks):
    cnt = 0
    for i in range(len(marks)):
        if marks[i] == -1:
            cnt += 1

    return cnt

# Mark Frequency Function


def freq(marks):
    frequency = {}

    for element in marks:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    print("Marks --> Frequency")
    for i in frequency:

        print(i, "-->", frequency[i])
    max_value = max(frequency.values())

    keys = [k for k, v in frequency.items() if v == max_value]
    print(keys, "is the higest frequency mark with", max_value, "Occurences.")


# Main Code
while (1):
    print("\n\t\t*****STUDENT'S RESULT*****\n")
    print("1.Average Score\n2.Higest and Lowest Score\n3.Absent Students\n4.Higest Frequency Marks\n5.Exit\n")
    ch = int(input("Enter Your Choice : "))
    print("")

    if ch == 1:
        print("Average is ", avg(marks))

    elif ch == 2:
        print("Higest and Lowest Score is ", maxmin(marks), "respectively")

    elif ch == 3:
        print("Number of Absent Students is ", absent(marks))

    elif ch == 4:
        freq(marks)

    elif ch == 5:
        print("\t\t*****TERMINATED SUCCESSFULLY*****\n")
        break

    else:
        print("Invalid Choice\n")

