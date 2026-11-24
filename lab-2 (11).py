pounds = float(input())
cash = float(input())

if pounds < 0 or cash < 0:
    print("Invalid Input")
else:
    total = pounds * 2.50

    print("Total cost = $%.2f" % total)

    if cash >= total:
        change = cash - total
        print("Change = $%.2f" % change)
    else:
        owe = total - cash
        print("You owe $%.2f more." % owe)