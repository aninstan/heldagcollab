from pylab import *
from pathlib import Path
import csv


with open(Path(__file__).parent / "Befolkning.csv", "r", encoding="utf-8-sig") as file:
    
    fieldnames = []
    year = []
    population = []

    data = csv.reader(file, delimiter=";")

    for i in range(3):
        next(data)

    for row in data:
        year.append(int(row[0]))
        population.append(int(row[1]))

    plot(year, population)
    title("Befolkning i Norge")
    xlabel("År")
    ylabel("Befolkning (millioner)")

    show()