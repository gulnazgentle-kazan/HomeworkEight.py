def printAll(path):
    data = open(path, 'r')
    for line in data:
        print(line)
    data.close()
