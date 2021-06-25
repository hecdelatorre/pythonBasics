colors = {"red", "green", "blue"}
print(type(colors))
print(colors)

print(f"red esta en colors: {'red' in colors}")
colors.add("violet")
print(colors)
colors.remove("red")
print(colors)

colors.clear()
print(colors)

del colors