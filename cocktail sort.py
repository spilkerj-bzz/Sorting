from datetime import datetime


def read_file(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip().split(','))
    return data


def write_file(data):
    for line in data:
        print(','.join(line) + '\n')

def cocktailSort_date(a):
    timer = datetime.now()
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if datetime.strptime(a[i][5], '%d.%m.%Y') > datetime.strptime(a[i + 1][5], '%d.%m.%Y'):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if datetime.strptime(a[i][5], '%d.%m.%Y') > datetime.strptime(a[i + 1][5], '%d.%m.%Y'):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
    difference = datetime.now() - timer
    return a, difference

def cocktailSort(a):
    place=int(input(" 2 for Nachname \n 4 for PLZ \n 6 for vermögen \n "))
    timer = datetime.now()
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if a[i][place] > a[i + 1][place]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if a[i][place] > a[i + 1][place]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
    difference = datetime.now() - timer
    return a, difference

filename = './data/SortSmall.txt'
data = read_file(filename)
sorted_data, difference = cocktailSort_date(data)
write_file(sorted_data)
print(difference)

filename = './data/SortMedium.txt'
data = read_file(filename)
sorted_data, difference = cocktailSort_date(data)
write_file(sorted_data)
print(difference)

filename = './data/SortBig.txt'
data = read_file(filename)
sorted_data, difference = cocktailSort_date(data)
write_file(sorted_data)
print(difference)
