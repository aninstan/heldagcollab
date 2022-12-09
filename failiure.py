from pylab import *
from pathlib import Path
import json

fig, axs = subplots(1, 3, figsize=(10, 2), sharey=True)

with open(Path(__file__).parent / "Sivilstand.json", "r", encoding="utf-8") as file:
    data = json.load(file)["dataset"]

    x = []

    for i in data["dimension"]["Tid"]["category"]["label"]:
        x.append(int(i))

    width = 0.20
    xvals = arange(len(x))

    print(len(data["value"]))

    for gender_key, gender_val in data["dimension"]["Kjonn"]["category"]["index"].items():

        gender_label = data["dimension"]["Kjonn"]["category"]["label"][gender_key]
        axs[gender_val].set_title(gender_label)

        gender_index_start = gender_val*len(x)*len(data["dimension"]["EkteskStatus"]["category"]["label"])

        for ekteskap_status_key, ekteskap_status_val in [["2", 1], ["4", 4]]:

            ekteskap_status_label = data["dimension"]["EkteskStatus"]["category"]["label"][ekteskap_status_key]
            ekteskap_status_index_start = len(x)*ekteskap_status_val
            
            y = []

            for k, v in data["dimension"]["Tid"]["category"]["index"].items():
                y.append(data["value"][gender_index_start + ekteskap_status_index_start + v])

            rect1 = axs[gender_val].bar(xvals - width/2, y, width, label=ekteskap_status_label)
            rect2 = axs[gender_val].bar(xvals + width/2, y, width, label=ekteskap_status_label)

            axs[gender_val].legend(loc='upper left')

            axs[gender_val].bar_label(rect1, padding=1)
            axs[gender_val].bar_label(rect2, padding=1)

            fig.tight_layout()

show()