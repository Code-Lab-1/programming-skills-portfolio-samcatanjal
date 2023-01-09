capitals = {
    "Manila" : "Philippines",
    "Tokyo" : "Japan",
    "Seoul" : "South Korea",
    "Paris" : "France"
}

del capitals["Manila"]

capitals.update({"Madrid" : "Spain"})

for keys, values in capitals.items():
    print(keys, 'is the capital of', values) 