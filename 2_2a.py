import matplotlib.pyplot as plt
from pathlib import Path
import json

fig, axs = plt.subplots(1, 3, figsize=(10, 5), sharey=True)


with open(Path(__file__).parent / "Sivilstand.json", "r", encoding="utf-8") as file:
    data = json.load(file)["dataset"]

    x = []

    for i in data["dimension"]["Tid"]["category"]["label"]:
        x.append(int(i))

    for gender_key, gender_val in data["dimension"]["Kjonn"]["category"]["index"].items():

        gender_label = data["dimension"]["Kjonn"]["category"]["label"][gender_key]
        axs[gender_val].set_title(gender_label)

        gender_index_start = gender_val*len(x)*len(data["dimension"]["EkteskStatus"]["category"]["label"])

        for ekteskap_status_key, ekteskap_status_val in data["dimension"]["EkteskStatus"]["category"]["index"].items():

            ekteskap_status_label = data["dimension"]["EkteskStatus"]["category"]["label"][ekteskap_status_key]
            ekteskap_status_index_start = len(x)*ekteskap_status_val
            
            y = []

            for k, v in data["dimension"]["Tid"]["category"]["index"].items():
                y.append(data["value"][gender_index_start + ekteskap_status_index_start + v])

            axs[gender_val].plot(x, y, label=ekteskap_status_label)
            axs[gender_val].legend(loc='upper left')


plt.show()
