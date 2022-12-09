import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import csv


with open(Path(__file__).parent / "Skilsmisser og ekteskap.csv", "r", encoding="utf-8-sig") as file:
    
    na_values = [".."]

    fieldnames = []
    data = []

    raw_data = csv.reader(file, delimiter=";")

    # First two rows contain no usefull information
    for i in range(2):
        next(raw_data)

    for i, row in enumerate(raw_data):

        fieldnames.append(row[0])
        data.append([])
        
        for j in row[1:]:
            data[i].append(int(j) if j not in na_values else 0)
    

    barWidth = 0.33

    # Set position of bar on x-axis
    bar1 = np.arange(len(data[0]))
    bar2 = bar1 + barWidth

    # Make the plot
    plt.bar(bar1, data[1], color ='blue', width = barWidth, label=fieldnames[1])
    plt.bar(bar2, data[2], color ='orange', width = barWidth, label=fieldnames[2])

    plt.xticks(bar1 + barWidth/2, data[0])
    plt.legend(loc='upper left')


plt.show()
