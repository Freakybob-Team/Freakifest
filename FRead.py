import json
with open('F.json', 'r') as file:
    data = json.load(file)
    print("Freakifest Version: " + data['f_ver'])
    print("Is Greg: " + data['isGreg'])
    print("Name: " + data['name'])
    print("Software Version: " + data['soft_ver'])
    print("Description: " + data['description'])
    file.close()