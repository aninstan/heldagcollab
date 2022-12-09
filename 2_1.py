import matplotlib.pyplot as plt
from pathlib import Path
import csv


with open(Path(__file__).parent / "Befolkning.csv", "r", encoding="utf-8-sig") as file:
    
    fieldnames = []
    year = []
    population = []

    data = csv.reader(file, delimiter=";")

    # First three rows contain no usefull information
    for i in range(3):
        next(data)

    for row in data:
        year.append(int(row[0]))
        population.append(int(row[1]))

    plt.plot(year, population)
    plt.title("Befolkning i Norge")
    plt.xlabel("År")
    plt.ylabel("Befolkning (millioner)")


plt.show()
