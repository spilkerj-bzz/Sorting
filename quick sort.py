from datetime import datetime

def main():

    def data_array(dataFile):
        data = []
        with open(dataFile, 'r') as file:
            for line in file:
                data.append(line.strip().split(','))
        return data

    data = data_array("./data/SortBig.txt")

    def quicksort_plz(array):

        less = []
        equal = []
        greater = []

        if len(array) > 1:
            pivot = array[0][4]
            for x in array:
                if x[4] < pivot:
                    less.append(x)
                elif x[4] == pivot:
                    equal.append(x)
                elif x[4] > pivot:
                    greater.append(x)

            return quicksort_plz(less)+equal+quicksort_plz(greater)
        else:
            return array

    def quicksort_name(array):

        less = []
        equal = []
        greater = []

        if len(array) > 1:
            pivot = array[0][2]
            for x in array:
                if x[2] < pivot:
                    less.append(x)
                elif x[2] == pivot:
                    equal.append(x)
                elif x[2] > pivot:
                    greater.append(x)

            return quicksort_name(less)+equal+quicksort_name(greater)
        else:
            return array

    def quicksort_assets(array):

        less = []
        equal = []
        greater = []

        if len(array) > 1:
            pivot = array[0][6]
            for x in array:
                if x[6] < pivot:
                    less.append(x)
                elif x[6] == pivot:
                    equal.append(x)
                elif x[6] > pivot:
                    greater.append(x)

            return quicksort_name(less)+equal+quicksort_name(greater)
        else:
            return array

    def quicksort_dates(array):

        less = []
        equal = []
        greater = []

        if len(array) > 1:
            pivot = datetime.strptime(array[0][5], "%d.%m.%Y")
            for x in array:
                if datetime.strptime(x[5], "%d.%m.%Y") < pivot:
                    less.append(x)
                elif datetime.strptime(x[5], "%d.%m.%Y") == pivot:
                    equal.append(x)
                elif datetime.strptime(x[5], "%d.%m.%Y") > pivot:
                    greater.append(x)

            return quicksort_dates(less)+equal+quicksort_dates(greater)
        else:
            return array

    time_now = datetime.now()
    array = quicksort_assets(data)
    diff = datetime.now() - time_now
    print(array)
    print(diff)


if __name__ == "__main__":
    main()