# create a list
movies = []

movies.append('The Holy Grail')
movies.append('THe Life of Brain')
movies.append('The Meaning of Life')

print(movies)

year_list = [1975, 1979, 1983]
k = 0
for i in range(1, len(movies) + len(year_list), 2):
    movies.insert(i, year_list[k])
    k += 1

movies = movies[:2]

print(movies)

movies_cast = ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones']
director = ['Graham Chapman']

movies_cast.append(director)
movies.append(movies_cast)

print(movies)

for obj in movies:
    if type(obj) == list:
        print(obj)
        for obj1 in obj:
            if type(obj1) == list:
                print(obj1)
        



