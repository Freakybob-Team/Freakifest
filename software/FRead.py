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
        print("site.freakybob.ratings: " + data['site.freakybob.ratings'])
        print("This is a good example of a production environment use of Cus.")
    except:
        None
    try:
        print("Website (via " + data['website.provider'] + "): " + data['website'])
        print("Warning! This is a bad way to use Providers and should be used in *DEV* environments.")
    except:
        None
    file.close()