from datetime import datetime


def main():
    def data_array(dataFile):
        data = []
        with open(dataFile, 'r') as file:
            for line in file:
                data.append(line.strip().split(','))
        return data

    data = data_array("./data/SortBig.txt")

    for i in data:
        i[5] = datetime.strptime(i[5], "%d.%m.%Y")

    def heapify(array, arrayLen, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < arrayLen and array[i][5] < array[left][5]:
            largest = left

        if right < arrayLen and array[largest][5] < array[right][5]:
            largest = right

        if largest != i:
            array[i][5], array[largest][5] = array[largest][5], array[i][5]
            heapify(array, arrayLen, largest)

    def heapSort(array):

        array_len = len(array)

        for i in range(array_len // 2 - 1, -1, -1):
            heapify(array, array_len, i)

        for i in range(array_len - 1, 0, -1):
            array[i][5], array[0][5] = array[0][5], array[i][5]
            heapify(array, i, 0)

        return array

    timer_start = datetime.now()
    sorted_arr = heapSort(data)
    timer_stop = datetime.now() - timer_start

    print(sorted_arr)
    print(timer_stop)



if __name__ == "__main__":
    main()