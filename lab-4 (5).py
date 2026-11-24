n = int(input())
period = input("Enter day or night: ")

if n <= 0:
    print("Invalid distance")

elif period != "day" and period != "night":
    print("Invalid period")

else:
    taxi_rate = 37.89

    if period == "night":
        taxi_rate = 43.17

    taxi = 33.58 + n * taxi_rate
    bus = n * 4.32
    train = n * 2.88

    cheapest = taxi

    if n >= 20 and bus < cheapest:
        cheapest = bus

    if n >= 100 and train < cheapest:
        cheapest = train

    print("Cheapest price:", round(cheapest, 2))