import re

custom_dict = {'james hallow':92948489, 'James Crew':65783883, 'Joe Nami':48825929,'Han Nue':29948585,'Joe Nue':4848399999,'James Anderson':28949494}

for key in custom_dict.keys():
    name = key.split(' ')
    if(re.match(r'(^[J])', name[0]) != None and re.match(r'(Nue+)', name[1]) != None):
        print(key, ':', custom_dict[key]) 
