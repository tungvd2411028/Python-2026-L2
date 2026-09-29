colors = ["Blue", "Yellow", "Black", "Red"]

color = input("What is your favorite color? ")

if color in colors:
    index = colors.index(color)
    print("Your color is at index", index, "in my list")
else:
    print("Sorry, I could not find your color")