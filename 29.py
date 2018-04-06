import re

str = "Python PHP Marshmellow Meows Maths Muscle Great Brave"

searchObj = re.findall( r'[m|M][\d\w]{4}', str, re.I|re.M)

print(searchObj)
