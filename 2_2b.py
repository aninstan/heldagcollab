import matplotlib.pyplot as plt
from pathlib import Path
import json

fig, axs = plt.subplots(1, 5, figsize=(10, 5), sharey=True)


with open(Path(__file__).parent / "Sivilstand.json", "r", encoding="utf-8") as file:    
    data = json.load(file)["dataset"]

    x = []

    # Get all years
    for i in data["dimension"]["Tid"]["category"]["label"]:
        x.append(int(i))

    # Loop through all statuses
    for ekteskap_status_key, ekteskap_status_val in data["dimension"]["EkteskStatus"]["category"]["index"].items():

        # Get status label
        ekteskap_status_label = data["dimension"]["EkteskStatus"]["category"]["label"][ekteskap_status_key]
        ekteskap_status_index_start = len(x)*ekteskap_status_val
        
        axs[ekteskap_status_val].set_title(ekteskap_status_label)

        # Loop through all genders
        for gender_key, gender_val in data["dimension"]["Kjonn"]["category"]["index"].items():

            # Get gender label
            gender_label = data["dimension"]["Kjonn"]["category"]["label"][gender_key]
            gender_index_start = gender_val*len(x)*len(data["dimension"]["EkteskStatus"]["category"]["label"])

            y = []

            for k, v in data["dimension"]["Tid"]["category"]["index"].items():
                y.append(data["value"][gender_index_start + ekteskap_status_index_start + v])

            # Put data in subplot
            axs[ekteskap_status_val].plot(x, y, label=gender_label)
            
        axs[ekteskap_status_val].legend(loc='upper left')


plt.show()
