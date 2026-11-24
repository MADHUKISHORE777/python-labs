total = int(input())
attended = int(input())

if total <= 0 or attended < 0 or attended > total:
    print("Invalid Input")

else:
    percentage = (attended / total) * 100

    print("Attendance Percentage =", percentage, "%")

    if percentage >= 75:
        print("Eligible")
    else:
        print("Not Eligible")