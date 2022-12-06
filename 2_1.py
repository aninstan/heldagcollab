import matplotlib.pyplot as plt
from pathlib import Path
import csv

plt.style.use("dark_background")

fieldnames = []
year = []
population = []


with open(Path(__file__).parent / "Befolkning.csv", "r", encoding="utf-8-sig") as file:
    
    data = csv.reader(file, delimiter=";")

    next(data)
    next(data)
    fieldnames = next(data)

    for row in data:
        year.append(int(row[0]))
        population.append(int(row[1]))


plt.plot(year, population)
plt.show()
