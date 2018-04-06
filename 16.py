import os

print("Current directory: " + os.getcwd())

for root, dirs, files in os.walk("./", topdown=True):
    print(files)

    for name in dirs:
        if name == 'mysub':
            for root, dirs, files in os.walk(name, topdown=True):
                for name in files:
                    print(name)