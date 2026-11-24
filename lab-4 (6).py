holidays = int(input("Enter number of holidays: "))

if holidays < 0 or holidays > 365:
    print("Invalid number of holidays")

else:
    workdays = 365 - holidays

    play_time = (workdays * 63) + (holidays * 127)

    difference = 30000 - play_time

    if difference >= 0:
        print("Tom sleeps well!")
        print("Difference:", difference, "minutes less than norm")
    else:
        print("Tom cannot sleep well!")
        print("Difference:", -difference, "minutes more than norm")