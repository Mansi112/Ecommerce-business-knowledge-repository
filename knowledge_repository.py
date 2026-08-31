import json

def load_knowledge(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

print("E-Commerce Business Knowledge Repository Loaded Successfully")
