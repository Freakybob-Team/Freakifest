import json
print("Only approved Cus will show.")
with open('F.json', 'r') as file:
    data = json.load(file)
    print("Freakifest Version: " + data['f_ver'])
    # print("Is Greg: " + data['isGreg'])
    print("Name: " + data['name'])
    print("Software Version: " + data['soft_ver'])
    print("Description: " + data['description'])
    try:
        print("Rating (site.freakybob): " + data['site.freakybob.ratings'])
    except:
        None
    try:
        print("Website (via " + data['website.provider'] + "): " + data['website'])
    except:
        None
    file.close()