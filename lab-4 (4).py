hours = int(input())
minutes = int(input())

if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
    print("Invalid time")
else:
    minutes = minutes + 15

    if minutes >= 60:
        minutes = minutes - 60
        hours = hours + 1

    if hours == 24:
        hours = 0

    print(hours, ":", end="")

    if minutes < 10:
        print("0", end="")

    print(minutes)