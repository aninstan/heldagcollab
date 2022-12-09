import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import json

fig, axs = plt.subplots(1, 3, figsize=(10, 5), sharey=True)


with open(Path(__file__).parent / "Sivilstand.json", "r", encoding="utf-8") as file:
    data = json.load(file)["dataset"]

    x = []

    for i in data["dimension"]["Tid"]["category"]["label"]:
        x.append(int(i))

    width = 0.30
    xvals = np.arange(len(x))

    # Loop through all genders
    for gender_key, gender_val in data["dimension"]["Kjonn"]["category"]["index"].items():

        # Get gender label
        gender_label = data["dimension"]["Kjonn"]["category"]["label"][gender_key]
        axs[gender_val].set_title(gender_label)

        gender_index_start = gender_val*len(x)*len(data["dimension"]["EkteskStatus"]["category"]["label"])

        # Loop through all statuses
        for ekteskap_status_key, ekteskap_status_val in [["2", 1], ["4", 4]]:

            # Get status label
            ekteskap_status_label = data["dimension"]["EkteskStatus"]["category"]["label"][ekteskap_status_key]
            ekteskap_status_index_start = len(x)*ekteskap_status_val
            
            y = []

            for k, v in data["dimension"]["Tid"]["category"]["index"].items():
                h = data["value"][gender_index_start + ekteskap_status_index_start + v]
                if (h != None):
                    y.append(h)
                else: 
                    y.append(0)

            rect1 = axs[gender_val].bar(xvals - width, y, width, label=ekteskap_status_label)
        
            axs[gender_val].legend(loc='upper left')
            
            fig.tight_layout()


plt.show()
