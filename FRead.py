import json
with open('F.json', 'r') as file:
    data = json.load(file)
    for i in data['f_ver']:
        print("Freakifest Version: " + i)
    file.close