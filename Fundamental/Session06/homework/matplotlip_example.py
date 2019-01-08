from matplotlib import pyplot

# Prepare data
machine_counts = [18, 4 ,2]

#  Prepare labels
machine_names = ["PC", "MAC", "Linux"]

# Draw pie
pyplot.pie(machine_counts, labels=machine_names, autopct="%.1f%%", shadow=True, explode=[0, 0.15, 0])
pyplot.title("PC vs MAC vs Linux useage")
pyplot.axis("equal")    

# Show
pyplot.show()

