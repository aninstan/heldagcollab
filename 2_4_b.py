from pathlib import Path
from pylab import *
import csv


with open(Path(__file__).parent / "Skilsmisser og ekteskap.csv", "r", encoding="utf-8-sig") as file:
    
    fieldnames = []
    data = []

    raw_data = csv.reader(file, delimiter=";")

    for i in range(2):
        next(raw_data)

    for i, row in enumerate(raw_data):

        fieldnames.append(row[0])
        data.append([])
        
        for j in row[1:]:
            data[i].append(int(j) if j != ".." else 0)
    

    barWidth = 1/len(fieldnames)

    # Set position of bar on X axis
    br1 = arange(len(data[0]))
    br2 = [x + barWidth for x in br1]

    # Make the plot
    bar(br1, data[1], color ='r', width = barWidth, edgecolor ='grey', label=fieldnames[1])
    bar(br2, data[2], color ='g', width = barWidth, edgecolor ='grey', label=fieldnames[2])


    xticks(br1 + barWidth/2, data[0])

    legend()
    show()

