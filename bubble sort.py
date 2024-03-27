from datetime import datetime

def bubble_sort(arr):
    place=int(input(" 2 for Nachname \n 4 for PLZ \n 6 for vermögen \n "))
    timer = datetime.now()
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j][place] > arr[j + 1][place]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    difference = datetime.now() - timer
    print(difference)
def bubble_sort_date(arr):

    timer = datetime.now()
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            date1 = datetime.strptime(arr[j][5], '%d.%m.%Y')
            date2 = datetime.strptime(arr[j + 1][5], '%d.%m.%Y')
            if date1 > date2:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    difference = datetime.now() - timer
    print(difference)


def read_file(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip().split(','))
    return data


def write_file(data):
    for line in data:
        print(','.join(line) + '\n')


filename = './data/SortSmall.txt'
data = read_file(filename)
bubble_sort(data)
write_file(data)
filename = './data/SortMedium.txt'
data = read_file(filename)
bubble_sort(data)
write_file(data)
filename = './data/SortBig.txt'
data = read_file(filename)
bubble_sort(data)
write_file(data)


