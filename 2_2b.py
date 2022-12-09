from pylab import *
from pathlib import Path
import json

fig, axs = subplots(1, 5, figsize=(10, 2), sharey=True)


with open(Path(__file__).parent / "Sivilstand.json", "r", encoding="utf-8") as file:    
    data = json.load(file)["dataset"]

    x = []

    for i in data["dimension"]["Tid"]["category"]["label"]:
        x.append(int(i))

    print(len(data["value"]))

    for ekteskap_status_key, ekteskap_status_val in data["dimension"]["EkteskStatus"]["category"]["index"].items():

        ekteskap_status_label = data["dimension"]["EkteskStatus"]["category"]["label"][ekteskap_status_key]
        ekteskap_status_index_start = len(x)*ekteskap_status_val
        
        axs[ekteskap_status_val].set_title(ekteskap_status_label)

        for gender_key, gender_val in data["dimension"]["Kjonn"]["category"]["index"].items():

            gender_label = data["dimension"]["Kjonn"]["category"]["label"][gender_key]
            gender_index_start = gender_val*len(x)*len(data["dimension"]["EkteskStatus"]["category"]["label"])

            y = []

            for k, v in data["dimension"]["Tid"]["category"]["index"].items():
                y.append(data["value"][gender_index_start + ekteskap_status_index_start + v])

            axs[ekteskap_status_val].plot(x, y, label=gender_label)
            
        axs[ekteskap_status_val].legend(loc='upper left')


show()