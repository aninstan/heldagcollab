from pathlib import Path
import json


with open(Path(__file__).parent / "Sivilstand.json", "r", encoding="utf-8") as file:
    data = json.load(file)["dataset"]


    print(data.keys())


    print(data["dimension"])