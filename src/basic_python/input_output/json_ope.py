import json

with open("b.txt", "r") as f:
    read_data = f.read()
print(json.dumps(read_data))

