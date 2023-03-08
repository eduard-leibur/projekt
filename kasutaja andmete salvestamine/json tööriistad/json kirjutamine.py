import json

sõnastik = {"kasutaja1": "parool1",
            "kasutaja2": "parool2"}

with open("../kasutajate andmed.json", "w") as fail:
    json.dump(sõnastik, fail)
