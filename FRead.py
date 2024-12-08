import json
with open('F.json', 'r') as file:
    data = json.load(file)
    print("Freakifest Version: " + data['f_ver'])
    print("Is Greg: " + data['isGreg'])
    file.close()