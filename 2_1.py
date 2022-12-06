# %%
from pylab import *
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



plot(year, population)
title("Befolkning i Norge")
xlabel("År")
ylabel("Befolkning (millioner)")

fig, axs = subplots(1, 3, figsize=(10, 2), sharey=True)

axs[0].plot(year, population, label = "Befolkning")
axs[0].set_title("")
axs[0].set_xlabel("")
axs[0].set_ylabel("")
axs[0].legend()

show()
