seconds = int(input())

if 1 <= seconds <= 86400:

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60

    print(hours,":",minutes,":",seconds)

else:
    print("Invalid Input")