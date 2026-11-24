color = input()
mode = input()

if color == "blue" and mode == "steady":
    print("Clear view")
elif color == "blue" and mode == "flashing":
    print("Clouds due")
elif color == "red" and mode == "steady":
    print("Rain ahead")
elif color == "red" and mode == "flashing":
    print("Snow instead")
else:
    print("Invalid Input")