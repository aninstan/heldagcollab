import matplotlib.pyplot as plt
from pathlib import Path
import json
import csv

fig, axs = plt.subplots(1, 6, figsize=(10, 5), sharey=True)


# Get data from "Befolkning.csv"
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

    # Put data in subplot
    axs[0].plot(year, population, label="Befolkning")

    axs[0].set_title("Total Befolkning")
    axs[0].legend(loc='upper left')


# Get data from "Sivilstand.json"
with open(Path(__file__).parent / "Sivilstand.json", "r", encoding="utf-8") as file:
    data = json.load(file)["dataset"]

    x = []

    for i in data["dimension"]["Tid"]["category"]["label"]:
        x.append(int(i))

    # Loop through all statuses
    for ekteskap_status_key, ekteskap_status_val in data["dimension"]["EkteskStatus"]["category"]["index"].items():

        # Get status label
        ekteskap_status_label = data["dimension"]["EkteskStatus"]["category"]["label"][ekteskap_status_key]
        ekteskap_status_index_start = len(x)*ekteskap_status_val
        
        axs[ekteskap_status_val + 1].set_title(ekteskap_status_label)

        # Loop through all genders
        for gender_key, gender_val in data["dimension"]["Kjonn"]["category"]["index"].items():

            # Get gender label
            gender_label = data["dimension"]["Kjonn"]["category"]["label"][gender_key]
            gender_index_start = gender_val*len(x)*len(data["dimension"]["EkteskStatus"]["category"]["label"])

            y = []

            for k, v in data["dimension"]["Tid"]["category"]["index"].items():
                y.append(data["value"][gender_index_start + ekteskap_status_index_start + v])

            # Put data in subplot
            axs[ekteskap_status_val + 1].plot(x, y, label=gender_label)

        axs[ekteskap_status_val + 1].legend(loc='upper left')


plt.show()
